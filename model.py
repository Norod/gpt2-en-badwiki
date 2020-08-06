# -*- coding: utf-8 -*-

import random
import torch
import re
from torch.nn import functional as F
from pytorch_transformers import GPT2Tokenizer, GPT2LMHeadModel
torch.set_grad_enabled(False)

MODEL_PATH = './gpt2-en-badwiki-distil'

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
tokenizer = GPT2Tokenizer.from_pretrained(MODEL_PATH)
model = GPT2LMHeadModel.from_pretrained(MODEL_PATH).eval()
model = model.to(device)

def parseText(text):
    trimmed_string = ""
    regex = r"<\|endoftext\|>"
    matches = list(re.finditer(regex, text, re.MULTILINE))
    if len(matches) > 0:
        trimmed_string += text[0:matches[0].start()] + "\n"
    else:
        trimmed_string += text + "\n"

    parsedText = trimmed_string.replace("<|startoftext|>", "").replace("<|endoftext|>", "\n")
    return parsedText

def extend(text, max_size=20):
    if text.find("<|startoftext|>") == -1: 
        text = "<|startoftext|>" + str(text)
    tokens = tokenizer.encode(text)
    prediction, past = torch.tensor([tokens]).to(device), None
    for i in range(max_size):
        prediction, past = model(prediction, past=past)
        prediction = torch.multinomial(F.softmax(prediction[:, -1], dim=1), 1)
        prediction_item = prediction.item()
        tokens.append(prediction_item)
        decoded_tokens = tokenizer.decode(tokens)
        if decoded_tokens.find("<|endoftext|>") >= 0:
            print("break at i = " + str(i))
            break

    parsed_text = parseText(decoded_tokens)
    if len(parsed_text) <= 4:
        parsed_text = "Error, please try again"
    return parsed_text

if __name__ == "__main__":
    random.seed(None)
    test_text = ''
    extended = extend(test_text, 120)
    print(extended)

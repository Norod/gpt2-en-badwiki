
#!/bin/sh

wget https://norod78.s3-eu-west-1.amazonaws.com/models/gpt2-en-badwiki-distil.zip
mkdir gpt2-en-badwiki-distil
unzip -n -j gpt2-en-badwiki-distil.zip -d ./gpt2-en-badwiki-distil
rm gpt2-en-badwiki-distil.zip

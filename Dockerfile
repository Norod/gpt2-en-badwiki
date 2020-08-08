FROM python:3.7
ADD . /app
WORKDIR /app
RUN wget https://files.pythonhosted.org/packages/5d/5e/35140615fc1f925023f489e71086a9ecc188053d263d3594237281284d82/torch-1.6.0-cp37-cp37m-manylinux1_x86_64.whl
RUN pip3 install torch-1.6.0-cp37-cp37m-manylinux1_x86_64.whl
RUN pip3 install -r requirements.txt
RUN rm torch-1.6.0-cp37-cp37m-manylinux1_x86_64.whl
RUN sh ./download.sh
CMD python3 main.py

FROM python:3.8.10

WORKDIR /app
COPY . /app
COPY ./requirments.txt /requirments.txt

#RUN pip install -r requirments.txt

RUN apt-get update && \
    apt-get install -y \
        build-essential \
        python3-dev \
        python3-setuptools \
        tesseract-ocr \
        make \
        gcc \ 
    && python3 -m pip install  -r requirments.txt \
    && apt-get remove -y --purge make gcc  build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*
    



     
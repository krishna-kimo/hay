#FROM python:3.6


FROM python:3.6-stretch
#FROM python:3.6 as base
LABEL maintainer="Krishna Nallamilli <krishna@kimo.ai>"
LABEL version = 1.0.0

#RUN apt install gcc git
COPY requirements.txt /requirements.txt
#FROM base as builder

#RUN mkdir /install
#WORKDIR /install
WORKDIR /
#COPY requirements.txt /requirements.txt
#RUN pip install --no-cache tensorflow
#RUN pip install --no-cache torch
#RUN pip install --no-cache torchvision
RUN pip install --no-cache Flask==1.1.2
RUN pip install --no-cache gunicorn==20.0.4
#RUN pip install --no-cache transformers
RUN git clone https://github.com/deepset-ai/haystack.git
WORKDIR /haystack
RUN pip install .
#FROM base

#COPY --from=builder /install /usr/local
COPY . /app

WORKDIR /app
CMD ["gunicorn", "-w",  "1", "--timeout",  "0", "app:app"]

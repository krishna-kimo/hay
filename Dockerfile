#FROM python:3.6

FROM python:3.6 as base
LABEL maintainer="Krishna Nallamilli <krishna@kimo.ai>"
LABEL version = 1.0.0

FROM base as builder

RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --target=/install -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local
COPY . /app

WORKDIR /app
CMD ["gunicorn", "-w 4", "--timeout 0", "app:app"]

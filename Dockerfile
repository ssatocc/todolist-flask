FROM python:3.10

WORKDIR /usr/src

COPY /src/requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

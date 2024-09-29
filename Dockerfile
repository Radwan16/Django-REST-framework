FROM python:3.9
ENV PYTHONBUFFERED=1
WORKDIR /code
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
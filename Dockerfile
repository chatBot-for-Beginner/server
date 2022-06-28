FROM python:3

WORKDIR /Desktop

RUN pip install --upgrade pip
RUN pip freeze > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
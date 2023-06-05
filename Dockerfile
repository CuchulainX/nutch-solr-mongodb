FROM python:latest

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app.py .
COPY ./auth.json .

ENV PYTHONUNBUFFERED=1

CMD [ "python", "-u", "app.py" ]

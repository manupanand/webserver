FROM python:3.13.1-alpine3.21

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3.13","manage.py","runserver","0.0.0.0:8000" ]
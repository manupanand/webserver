#python official image
FROM python:3.13.1-alpine3.21

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 5000

ENV FLASK_APP=app/app.py 

CMD [ "flask","run","--host","0.0.0.0" ]
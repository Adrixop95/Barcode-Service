FROM python:3.8-alpine

WORKDIR /app
EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache build-base zlib-dev jpeg-dev g++ freetype-dev

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install gunicorn 

COPY . /app

CMD [ "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "-b", "0.0.0.0:8000", "main:app"]
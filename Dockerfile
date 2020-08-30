FROM python:3.8-slim

WORKDIR /app
EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install libdmtx-dev zbar-tools -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install gunicorn 

COPY . /app

RUN rm -rf /app/venv/
RUN rm -rf `find -type d -name __pycache__`
RUN rm -rf `find -type d -name .idea`
RUN rm -rf `find -name requirements.txt`

CMD [ "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "-b", "0.0.0.0:8000", "main:app"]
FROM python:3.8-slim

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir flask numpy pandas

CMD ["python", "app.py"]
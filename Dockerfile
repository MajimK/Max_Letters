FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends build-essential libxml2-dev libxslt-dev && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir lxml==4.6.3

RUN pip install --no-cache-dir transkribus-client

WORKDIR /app

CMD ["python", "app/Test.py"]
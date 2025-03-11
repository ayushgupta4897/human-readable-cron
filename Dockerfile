FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -e .

ENTRYPOINT ["human-readable-cron"]
CMD ["-i"] 
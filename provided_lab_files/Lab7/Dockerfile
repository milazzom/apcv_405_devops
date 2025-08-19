# Use official Python image
FROM python:3.10-slim

WORKDIR /app

COPY metrics_app.py .

RUN pip install prometheus_client

EXPOSE 8000

CMD ["python", "metrics_app.py"]
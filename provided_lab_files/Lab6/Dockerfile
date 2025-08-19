FROM python:3.11-slim

WORKDIR /app
COPY . .

# Install dependencies for all scripts
RUN pip install pyyaml

# Default command (can be overridden by docker-compose)
CMD ["python", "greeting_env.py"]
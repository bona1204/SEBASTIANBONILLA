FROM python:3.9-slim
WORKDIR /app
COPY 07_DOCKER/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY 07_DOCKER/pipeline.py .
COPY ../data ./data
CMD ["python", "pipeline.py"]

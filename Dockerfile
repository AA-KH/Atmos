FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["sh", "start.sh"]
HEALTHCHECK CMD curl --fail http://localhost:8501 || exit 1
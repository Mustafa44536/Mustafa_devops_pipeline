FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8501

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
  && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml /app/
COPY src/ /app/src/

RUN python -m pip install --upgrade pip \
  && pip install .

EXPOSE 8501
CMD ["streamlit", "run", "/app/src/webapp/app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# Base image with Python
FROM python:3.10-slim

# Install ffmpeg and other OS deps
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the code
COPY . .

# Expose port for Gradio
EXPOSE 7860

# Run app.py
CMD ["python", "app.py"]

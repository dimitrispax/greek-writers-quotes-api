# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY routes.py .
COPY server.py .
COPY data/ ./data/

# Expose port 8080 (used by waitress server)
EXPOSE 8080

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the production server using waitress
CMD ["python", "server.py"]


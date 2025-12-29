FROM python:3.11-slim

# Install system dependencies including ffmpeg and nodejs
RUN apt-get update && apt-get install -y \
    ffmpeg \
    wget \
    curl \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Install yt-dlp (latest version)
RUN curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp \
    && chmod a+rx /usr/local/bin/yt-dlp

# Update yt-dlp to latest
RUN yt-dlp -U || true

# Set working directory
WORKDIR /app

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose port
EXPOSE 8080

# Set environment variable
ENV FLASK_ENV=production

# Run the application
CMD ["python", "app.py"]

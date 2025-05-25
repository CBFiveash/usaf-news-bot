# Use official Python image
FROM python:alpine

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the bot code
COPY . .

# Set environment variables (override with .env or at runtime)
ENV PYTHONUNBUFFERED=1

# Run the bot
CMD ["python", "bot.py"]

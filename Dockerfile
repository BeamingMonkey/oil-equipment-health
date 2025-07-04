# Use official Python image
FROM python:3.11-slim

# Set work directory inside container
WORKDIR /app

# Copy files to container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

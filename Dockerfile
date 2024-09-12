# Use the official Python image from the Docker Hub
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Install Tesseract OCR
RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev

# Copy the rest of your application code into the container
COPY . .

# Set environment variable for Django
ENV DJANGO_SETTINGS_MODULE=visiting_card_app.settings

# Expose port 8000 for the application
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "visiting_card_app.wsgi:application", "--bind", "0.0.0.0:8000"]

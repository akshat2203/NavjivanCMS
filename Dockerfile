# Use the official Python image as the base image
FROM python:3.10-slim

# Update package lists and install system dependencies
RUN apt-get update && apt-get install -y \
    python-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    libxmlsec1-dev \
    pkg-config \
    gettext \
    vim


# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application code into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run Django migrations
RUN python manage.py migrate

# Create a superuser
RUN python manage.py createsuperuser --noinput \
    --username $SUPER_USER \
    --email $SUPER_USER_EMAIL \
    --password $SUPERUSER_PASSWORD

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

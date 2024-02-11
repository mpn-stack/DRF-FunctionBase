FROM python:3.9.7-slim

# Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory files (on your machine) to the container
ADD . /app/

# Install any needed packages specified in requirements.txt
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install --upgrade pip
RUN /opt/venv/bin/pip install -r requirements.txt
RUN chmod +x entrypoint.sh
#RUN python manage.py makemigrations
#RUN python manage.py migrate

# Start the server
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["/app/entrypoint.sh"]
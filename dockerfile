# Use an official Python runtime as a parent image
FROM python

# Set the working directory in the container
WORKDIR app

# Copy the current directory contents into the container at app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port 8000 for the Django development server
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
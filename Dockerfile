# Use an official Python runtime as the base image
FROM tjshake/foosball-flask:0.1.0
# Set the working directory in the container
WORKDIR /app

ENV mysql_user=root  \
    mysql_password=admin  \
    mysql_db=mydb


# Copy the requirements file into the container
COPY requirements.txt .

# Copy the rest of the application code
COPY . .

# Specify the command to run your application
CMD ["python", "app.py"]

# Use a Python image as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /

# Copy requirements.txt (make sure to create one)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app code to the container
COPY . .

# Expose port 8000 for FastAPI
EXPOSE 8000

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "app/backend/api:app", "--host", "0.0.0.0", "--port", "8000"]

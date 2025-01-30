# Use a Python image as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt (make sure it's created and includes Streamlit)
COPY requirements.txt .

# Install dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit app code to the container
COPY . .

# Expose port 8501 for Streamlit (default port for Streamlit)
EXPOSE 8501

# Run the Streamlit app using the streamlit command
CMD ["streamlit", "run", "frontend/app.py"]

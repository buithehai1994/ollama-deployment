# Use the Ollama base image
FROM ollama/ollama

# Copy the script to pull the model
COPY ./pull-llama3.sh /pull-llama3.sh

# Make the script executable
RUN chmod +x /pull-llama3.sh

# Run the script to start the Ollama service and pull the model
ENTRYPOINT ["/pull-llama3.sh"]

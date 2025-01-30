from fastapi import FastAPI, HTTPException
import ollama

# Initialize FastAPI
app = FastAPI()

# Initialize the model variable
ollama_model = "deepseek-r1:1.5b"

@app.get("/")
def read_root():
    return {"message": "Ollama model is ready!"}

@app.get("/generate")
async def generate_text(prompt: str):
    try:
        # Generate response from the Ollama model
        result = ollama.chat(model=ollama_model, messages=[{"role": "user", "content": prompt}])
        return {"generated_text": result['message']['content']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Text generation failed: {str(e)}")

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FortiAgent API")

class Prompt(BaseModel):
    prompt: str

@app.post("/generate")
async def generate(prompt: Prompt):
    """Generate test steps from a prompt (placeholder)."""
    return {"message": f"Received: {prompt.prompt}"}

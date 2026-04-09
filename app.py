from fastapi import FastAPI
from pydantic import BaseModel
from llm_service import analyze_resume
from prompt_templates import build_prompt

app = FastAPI()

class ResumeRequest(BaseModel):
    resume: str
    job_description: str

@app.post("/analyze")
def analyze(data: ResumeRequest):
    prompt = build_prompt(data.resume, data.job_description)
    result = analyze_resume(prompt)

    return {
        "analysis": result
    }
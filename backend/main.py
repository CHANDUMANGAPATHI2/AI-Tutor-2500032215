
from fastapi import FastAPI

klu = FastAPI(
    title="AI Tutor",
    description="AI Tutor PBL Project",
    version="1.0.0"
)

@klu.get("/")
def home():
    return {"message": "Welcome to AI Tutor Project"}

@klu.get("/demo")
def demo():
    return {"message": "KL University"}

@klu.get("/askQuestion")
def ask():
    return {
        "Question": "What is LLM?",
        "Answer": "Large Language Model"
    }

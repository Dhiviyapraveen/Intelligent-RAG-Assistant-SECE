from fastapi import FastAPI

app = FastAPI(
    title="SECE Intelligent RAG Assistant",
    description="AI-powered RAG chatbot for Sri Eshwar College of Engineering",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to the SECE Intelligent RAG Assistant 🚀"
    }

@app.get("/health")
def health_check():
    return {
        "status": "Healthy",
        "server": "Running"
    }
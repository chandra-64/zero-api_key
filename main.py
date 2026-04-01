from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "status": "Secure",
        "message": "Zero-KEY Pipeline Active",
        "environment": os.getenv("K_SERVICE", "Local")
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
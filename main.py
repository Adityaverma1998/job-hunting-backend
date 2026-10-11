import os
import uvicorn
from fastapi import FastAPI

app = FastAPI(title="AI Job Hunter API")


@app.get("/")
def read_root():
    return {
        "message": "AI Job Hunter API is running",
        "status": "success",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)

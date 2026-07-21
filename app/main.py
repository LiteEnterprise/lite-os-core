from fastapi import FastAPI

app = FastAPI(
    title="LITE OS",
    description="Enterprise AI Operating System",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "project": "LITE OS",
        "status": "running",
        "version": "0.1.0",
        "message": "Welcome to LITE OS"
    }

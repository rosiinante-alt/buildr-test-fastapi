"""Minimal FastAPI test application."""
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Buildr Test FastAPI")

@app.get("/health")
async def health():
    """Health check endpoint."""
    return JSONResponse(
        content={"status": "healthy", "service": "buildr-test-fastapi"},
        status_code=200
    )

@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "FastAPI test app deployed via Buildr System"}

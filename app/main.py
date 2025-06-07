from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Mount the static directory to serve all its content
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve index.html at the root path
@app.get("/")
async def serve_index():
    index_file = Path("static/index.html")
    if index_file.exists():
        return FileResponse(index_file)
    return {"detail": "index.html not found"}

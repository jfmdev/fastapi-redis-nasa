from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import httpx
import os
from pathlib import Path

load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
NASA_APOD_URL = "https://api.nasa.gov/planetary/apod"

app = FastAPI(
  title="Simple FastAPI application",
  description="A lightweight application that demonstrates how to build a RESTful API using FastAPI.",
  version="1.0.0"
)

# Mount the static directory to serve all its content.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve index.html at the root path.
@app.get("/")
async def serve_index():
  index_file = Path("static/index.html")
  if index_file.exists():
    return FileResponse(index_file)
  return {"detail": "index.html not found"}

# Image endpoint.
@app.get("/image", summary="Get NASA Astronomy Picture of the Day", response_model=dict)
async def get_nasa_apod():
  """
  Fetches the Astronomy Picture of the Day (APOD) from the NASA API.
  """
  params = {"api_key": NASA_API_KEY}

  try:
    async with httpx.AsyncClient() as client:
      response = await client.get(NASA_APOD_URL, params=params)
      response.raise_for_status() 
      return response.json()
  except httpx.RequestError as exc:
    raise HTTPException(
      status_code=500,
      detail=f"An unexpected error occurred while requesting the image: {exc}"
    )
  except httpx.HTTPStatusError as exc:
    raise HTTPException(
      status_code=exc.response.status_code,
      detail=f"An error occurred while requesting the imager: {exc.response.text}"
    )
  except Exception as exc:
    raise HTTPException(
      status_code=500,
      detail=f"An unexpected error occurred: {exc}"
    )

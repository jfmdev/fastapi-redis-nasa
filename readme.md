# FastAPI example

> A simple project that showcases how to create and run a FastAPI application.

## Requirements

1. Create a `.env` file in the "/app" folder.
2. Visit [api.nasa.gov](https://api.nasa.gov/) and request a free API key.
3. Add the key to your `.env` file like this:

```
NASA_API_KEY=your_api_key_here
```

## Running locally

You can run the project using a Python virtual environment or Docker.

### Using a Virtual Environment

```
# Create a virtual environment (only once)
python3 -m venv ./my-env

# Activate the virtual environment
source ./my-env/bin/activate

# Install dependencies (only once)
pip install -r ./app/requirements.txt

# Navigate to the app directory
cd app

# Run the FastAPI application
uvicorn main:app --reload
```

The app will be available at http://localhost:8000

### Using Docker

```
# Build the Docker image (only once)
docker build -t fastapi-example ./app

# Run the Docker container
docker run -p 8000:8000 fastapi-example
```

The app will be accessible at http://localhost:8000

## License

This application is free software; you can redistribute it and/or modify it under the terms of the Mozilla Public License v2.0. You should have received a copy of the MPL 2.0 along with this library, otherwise you can obtain one at http://mozilla.org/MPL/2.0/.
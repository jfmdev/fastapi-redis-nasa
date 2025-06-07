# FastAPI example

> A simple project that showcases how to create and run a FastAPI application.

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

# FastAPI example

> A simple project that showcases how to create and run a FastAPI application (integrated with an external API and Redis).

## Requirements

To run this application, you'll need the following:

* An API key from [api.nasa.gov](https://api.nasa.gov/) (you can request one for free).
* A running Redis instance.

After obtaining these, create a `.env` file inside the `/app` directory with the following content:

```env
NASA_API_KEY=your_nasa_api_key_here
REDIS_HOST=your_redis_host
REDIS_PORT=your_redis_port
```

Make sure the API key and Redis URL are correct and accessible from your environment.

> Note that you don’t need to set the Redis variables manually if you're using Docker Compose (on this case the environment is configured automatically).

## Running locally

You can run the project using a Python virtual environment or Docker.

### Using a Virtual Environment

```bash
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

> Nota that you can install Redis via the [official installer](https://redis.io/) or use Docker as described bellow.

### Using Docker

You can run both the FastAPI application and Redis using Docker Compose (recommended), or you can manage containers manually.

#### Docker Compose

```bash
docker compose up
```

This will build and start both the FastAPI app and Redis service automatically.

#### Manual Docker setup

##### Start Redis with Docker

```bash
# Run Redis container (first time)
docker run -d --name fastapi-example-redis -p 6379:6379 redis

# Start Redis if it's already created
docker start fastapi-example-redis
```

Redis will be available at: `redis://localhost:6379`

> To stop the Redis container when you're done: `docker stop fastapi-example-redis`

##### Main application

```bash
# Build the Docker image (only once)
docker build -t fastapi-example-main ./app

# Run the Docker container
docker run -p 8000:8000 fastapi-example-main
```

The app will be accessible at http://localhost:8000

## License

This application is free software; you can redistribute it and/or modify it under the terms of the Mozilla Public License v2.0. You should have received a copy of the MPL 2.0 along with this library, otherwise you can obtain one at http://mozilla.org/MPL/2.0/.
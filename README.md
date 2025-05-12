# update-noip-ddns

A simple Python script to update No-IP Dynamic DNS service with your current public IP address.

## Features
- Periodically updates your No-IP DDNS every 5 minutes
- Loads credentials from a `.env` file or environment variables
- Easy to run locally or in Docker

## Requirements
- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (for dependency management and running)
- Docker (optional, for containerized usage)

## Setup

1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd update-noip-ddns
   ```

2. Create a `.env` file in the project root:
   ```env
   NOIP_USERNAME=your_noip_username
   NOIP_PASSWORD=your_noip_password
   NOIP_HOSTNAME=yourhostname.ddns.net
   ```

3. Install dependencies (if running locally):
   ```sh
   uv sync
   ```

4. Run the script (if running locally):
   ```sh
   uv run main.py
   ```

## Docker Usage

You can run everything with Docker Compose:

1. Build and start the service:
   ```sh
   docker compose up --build
   ```

2. The script will run and update your No-IP DDNS every 5 minutes.

### Environment Variables

Make sure to provide your `.env` file in the project root, or set the variables in your Docker Compose file.

## Dockerfile Example

```
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install uv
RUN uv sync
CMD ["uv", "run", "main.py"]
```

## docker-compose.yml Example

```
version: '3.8'
services:
  ddns-updater:
    build: .
    env_file:
      - .env
    restart: unless-stopped
```

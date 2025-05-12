# Use official Python image
FROM python:3.13-slim

# Set work directory
WORKDIR /app

# Copy project files
COPY . /app

# Install uv (universal virtualenv/pip replacement)
RUN pip install uv

# Install dependencies
RUN uv sync

# Default command
CMD ["uv", "run", "main.py"]

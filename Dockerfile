# 1. Base Stage
FROM python:3.12-slim as base
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1
RUN pip install uv
WORKDIR /app

# 2. Dependencies Stage
FROM base as deps
# Copy the project definition file
COPY pyproject.toml ./
# Install all dependencies from pyproject.toml to the system python
# We install the 'dev' dependencies as well to have tools like pytest available
RUN uv pip install --system '.[dev]'

# 3. Runtime Stage
FROM python:3.12-slim as runtime
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
# Copy installed packages and their executables from the deps stage
COPY --from=deps /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=deps /usr/local/bin /usr/local/bin
# Copy application source code
COPY src/ /app/src/
# Create a non-root user to run the application
RUN useradd --create-home --shell /bin/bash appuser
# Change ownership of the app directory to the new user
RUN chown -R appuser:appuser /app
USER appuser
WORKDIR /app
EXPOSE 8000
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]

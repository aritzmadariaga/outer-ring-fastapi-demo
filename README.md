# Outer Ring FastAPI Base

A fully containerized, secure, and reproducible FastAPI platform — built for scalability, observability, and developer efficiency.

## Overview

This project provides a production-grade FastAPI architecture, entirely containerized with Docker. It uses MariaDB as the database, SQLAlchemy for the ORM, Alembic for migrations, and `uv` for fast dependency management.

The architecture follows clean separation of concerns, with distinct layers for API, services, repositories, and data models. The entire development lifecycle, from running the application to testing and building documentation, is managed through `make` commands that execute within Docker containers.

## Features

- **Python 3.12 & FastAPI**: Modern, high-performance backend.
- **`uv` for Package Management**: A fast, Rust-based package manager.
- **Docker & Docker Compose**: Fully containerized for development and production.
- **SQLAlchemy 2.0 & Alembic**: Typed ORM and versioned database migrations.
- **Pydantic V2**: Robust data validation and serialization.
- **Clean Architecture**: Separated layers for maintainability.
- **Pytest**: Unit and integration testing with coverage enforcement.
- **Sphinx**: Automated technical documentation generation.
- **CI/CD Ready**: GitHub Actions workflows for linting, testing, and building.
- **Observability**: Structured logging and health check endpoints.

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- `make`

### Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    # Outer Ring FastAPI Base

    A fully containerized, secure, and reproducible FastAPI platform — built for scalability, observability, and developer efficiency.

    ## Overview

    This project provides a production-grade FastAPI architecture, entirely containerized with Docker. It uses MariaDB as the database, SQLAlchemy for the ORM, Alembic for migrations, and `uv` for fast dependency management.

    The architecture follows clean separation of concerns, with distinct layers for API, services, repositories, and data models. The entire development lifecycle, from running the application to testing and building documentation, is managed through `make` commands that execute within Docker containers.

    ## Features

    - **Python 3.12 & FastAPI**: Modern, high-performance backend.
    - **`uv` for Package Management**: A fast, Rust-based package manager.
    - **Docker & Docker Compose**: Fully containerized for development and production.
    - **MariaDB/MySQL**: Uses MariaDB as the database (compatible with MySQL drivers via `pymysql`).
    - **SQLAlchemy 2.0 & Alembic**: Typed ORM and versioned database migrations.
    - **Pydantic V2**: Robust data validation and serialization.
    - **Clean Architecture**: Separated layers for maintainability.
    - **Pytest**: Unit and integration testing with coverage enforcement.
    - **Sphinx**: Automated technical documentation generation.
    - **CI/CD Ready**: GitHub Actions workflows for linting, testing, and building.
    - **Observability**: Structured logging and health/readiness endpoints.

    ## Getting Started

    ### Prerequisites

    - Docker
    - Docker Compose
    - `make`

    ### Setup

    1.  **Clone the repository:**
        ```bash
        git clone <repository-url>
        cd outer-ring-fastapi-base
        ```

    2.  **Create the environment file:**
        The Makefile will automatically copy `.env.example` to `.env` if it doesn't exist. No changes are needed for local development.

    3.  **Build and start the services:**
        This command will build the Docker images and start the `app`, `db`, and `adminer` containers.
        ```bash
        make up
        ```

    The API will be available at `http://localhost:8000`.
    The auto-generated API documentation (Swagger UI) will be at `http://localhost:8000/docs`.
    Redoc is available at `http://localhost:8000/redoc`.
    Adminer, the database management tool, will be at `http://localhost:8080`.

    ## Health & Readiness

    - `GET /healthz`: Returns 200 if the service process is running (liveness probe).
    - `GET /readyz`: Returns 200 if the service is ready (database reachable), 503 otherwise (readiness probe).

    ## Documentation

    - Run `make docs` to build the technical documentation with Sphinx.
    - The generated HTML docs are in `docs/build/index.html` (open in your browser).

    ## Local Development with uv

    If you want to install dependencies locally (outside Docker):

    ```bash
    uv pip install --system '.[dev]'
    ```

    You can then run the app with:

    ```bash
    uvicorn src.app.main:app --reload
    ```

    ## Development Workflow

    All commands are run from the project root directory.

    | Command           | Description                                               |
    | ----------------- | --------------------------------------------------------- |
    | `make up`         | Build and start containers in detached mode.              |
    | `make down`       | Stop and remove containers, networks, and volumes.        |
    | `make logs`       | Follow the logs from the FastAPI application container.   |
    | `make migrate`    | Generate and apply database migrations.                   |
    | `make seed`       | Populate the database with initial seed data.             |
    | `make test`       | Run all unit and integration tests with coverage.         |
    | `make unit`       | Run only the unit tests.                                  |
    | `make integration`| Run only the integration tests.                           |
    | `make docs`       | Build the Sphinx documentation (output in `docs/build`).  |
    | `make lint`       | Check the code for style and quality issues with Ruff.    |
    | `make format`     | Automatically format the code with Black and isort.       |
    | `make check-types`| Perform static type checking with Mypy.                   |

    ## License

    This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

    ## Contact

    Maintainer: Aritz Madariaga (<aritzmadariaga@deusto.es>)


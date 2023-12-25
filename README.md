# Airplane Calculator API

This document provides instructions on setting up and running the Airplane Calculator API project.

## Overview

The Airplane Calculator API offers an endpoint for calculating fuel consumption and max fly minutes for a list of airplanes. The project utilizes Docker and Docker Compose to containerize the Python/Django application and services.

## Technologies
- Make
- Docker
- Docker Compose

## Getting Started

### Prerequisites
- Make
- Docker Desktop
- Docker Compose

### Initial Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/paakwasi317/kami-airline.git
    ```

2. Change to the project directory:

    ```bash
    cd kami-airline/
    ```

3. Create `.env` file in the project root directory with these database config:

    ```bash
    DJANGO_SECRET_KEY=some_secret
    DB_USER=postgres
    DB_PASSWORD=postgres
    DB_HOST=db
    DB_PORT=5432
    DB_NAME=postgres
    ```

4. Build and start the Docker containers:

    ```bash
    make up
    ```

    This command will build the necessary Docker images and start all required services in the background.

### Running Tests

To run the test suite:

```bash
make test
```

### Shutting down all resources

To shut down docker containers:

```bash
make down
```

# Airplane Calculator API

This document provides instructions on setting up and running the Airplane Calculator API project.

## Overview

The Airplane Calculator API offers an endpoint for calculating fuel consumption and max fly minutes for a list of airplanes. The project utilizes Docker and Docker Compose to containerize the Python/Django application and services.

## Technologies
- Docker
- Docker Compose

## Getting Started

### Prerequisites

- Docker Desktop
- Docker Compose

### Initial Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-repo/airplane-calculator-api.git
    ```

2. Change to the project directory:

    ```bash
    cd airplane-calculator-api
    ```

3. Build and start the Docker containers:

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
make test
```

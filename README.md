**Flask Docker Azure CI/CD**

This is a mini DevOps project that demonstrates a complete CI/CD pipeline using a simple Flask application, Docker, GitHub Actions, and Azure Web App for Containers.

**Tech Stack**

- Python + Flask – basic web application

- Docker – containerization

- GitHub Actions – CI pipeline

- GitHub Container Registry (GHCR) – container image hosting

- Azure Web App for Containers – application deployment platform

**CI/CD Pipeline Overview**

1. The application code is located in app.py

2. On every git push to the main branch, a GitHub Actions workflow is triggered

3. The workflow:

    - Builds a Docker image using the provided Dockerfile

    - Pushes the image to GitHub Container Registry (GHCR)

4. Azure Web App automatically pulls the image from GHCR and runs the container

**Live Application**

Available at:

https://flask-krystian-app-fxg2g6evaydzcxaj.northeurope-01.azurewebsites.net/


**Key Learnings**

- Building a minimal web application with Flask

- Writing and understanding a basic Dockerfile

- Creating a GitHub Actions workflow for building and publishing Docker images

- Using GitHub Container Registry (GHCR)

- Deploying Docker containers to Azure Web App for Containers

- Connecting all components into a functional CI/CD pipeline

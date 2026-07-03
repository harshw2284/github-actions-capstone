#  GitHub Actions CI/CD Pipeline for a Python Flask Application

This project demonstrates a production-inspired CI/CD pipeline using **GitHub Actions**, **Docker**, and **reusable workflows**. The pipeline automates code validation, Docker image creation, deployment simulation, and scheduled health checks, following DevOps best practices.

## 📌 Features

- ✅ Pull Request validation before merging into `main`
- ✅ Reusable GitHub Actions workflows
- ✅ Automated Python environment setup
- ✅ Automated test execution using `pytest`
- ✅ Docker image build and push to Docker Hub
- ✅ Image versioning using Git commit SHA
- ✅ Scheduled Docker image health checks
- ✅ GitHub Step Summary reporting

## 🔄 Workflow Overview

### 1. Pull Request Pipeline (`pr-pipeline.yml`)
Runs whenever a Pull Request is opened or updated.

**Pipeline Steps**
- Checkout source code
- Setup Python environment
- Install dependencies
- Execute unit tests
- Display PR validation summary

  [![PR pipeline](https://github.com/harshw2284/GitHub-Actions-Capstone/actions/workflows/pr-pipeline.yml/badge.svg)](https://github.com/harshw2284/GitHub-Actions-Capstone/actions/workflows/pr-pipeline.yml)

---

### 2. Main Pipeline (`main-pipeline.yml`)
Triggered on every push to the `main` branch.

**Pipeline Stages**
1. Run reusable build workflow
2. Execute automated tests
3. Build Docker image
4. Push Docker image to Docker Hub
5. Generate image URL as workflow output
6. Simulate deployment to the production environment

[![Main Pipeline](https://github.com/harshw2284/GitHub-Actions-Capstone/actions/workflows/main-pipeline.yml/badge.svg)](https://github.com/harshw2284/GitHub-Actions-Capstone/actions/workflows/main-pipeline.yml)

---

### 3. Reusable Build Workflow (`reusable-build.yml`)

This reusable workflow handles application validation by:

- Setting up Python
- Installing dependencies
- Running unit tests
- Returning test status as workflow outputs

---

### 4. Reusable Docker Workflow (`reusable-docker.yml`)

Responsible for containerization.

Functions include:

- Docker Hub authentication
- Building Docker images
- Pushing images to Docker Hub
- Returning the full Docker image URL as an output

---

### 5. Health Check Workflow (`health-check.yml`)

Runs manually or every 12 hours using GitHub Actions Scheduler.

It performs the following tasks:

- Pull the latest Docker image
- Start the container
- Wait for application startup
- Stop and remove the container
- Generate a GitHub Step Summary report

[![Health Check](https://github.com/harshw2284/GitHub-Actions-Capstone/actions/workflows/health-check.yml/badge.svg)](https://github.com/harshw2284/GitHub-Actions-Capstone/actions/workflows/health-check.yml)

---

## 🛠️ Technologies Used

- GitHub Actions
- Python 3.13
- Flask
- Pytest
- Docker
- Docker Hub
- YAML

---

## 📂 Workflow Architecture

```text
Pull Request
      │
      ▼
Reusable Build
      │
      ▼
Run Tests
      │
      ▼
────────────── Merge ──────────────
                │
                ▼
         Main Pipeline
                │
                ▼
      Reusable Build
                │
                ▼
      Docker Build & Push
                │
                ▼
     Production Deployment
                │
                ▼
 Scheduled Health Check (Every 12 Hours)
```

---

## 🎯 Learning Objectives

This project demonstrates how to:

- Create reusable GitHub Actions workflows
- Share outputs between workflows
- Automate testing in CI
- Build and publish Docker images
- Use GitHub Secrets and Variables securely
- Structure a real-world CI/CD pipeline
- Implement scheduled workflow automation

---

> This project was built as a hands-on DevOps learning exercise to understand modern CI/CD practices using GitHub Actions and Docker.

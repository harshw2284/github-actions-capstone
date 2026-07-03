# 🚀 DevSecOps CI/CD Pipeline with GitHub Actions

![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-blue?logo=githubactions\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?logo=flask)

<!-- Replace <USERNAME> and <REPOSITORY> with your own -->

## Workflow Status

[![Main Pipeline](https://github.com/<USERNAME>/<REPOSITORY>/actions/workflows/main-pipeline.yml/badge.svg)](https://github.com/<USERNAME>/<REPOSITORY>/actions/workflows/main-pipeline.yml)

[![PR Checks](https://github.com/<USERNAME>/<REPOSITORY>/actions/workflows/pr.yml/badge.svg)](https://github.com/<USERNAME>/<REPOSITORY>/actions/workflows/pr.yml)

[![Health Check](https://github.com/<USERNAME>/<REPOSITORY>/actions/workflows/health-check.yml/badge.svg)](https://github.com/<USERNAME>/<REPOSITORY>/actions/workflows/health-check.yml)

---

# 📖 Project Overview

This project demonstrates a **real-world DevSecOps CI/CD pipeline** built using **GitHub Actions**, **Docker**, and a **Python Flask** application.

The pipeline automatically:

* ✅ Builds the application
* ✅ Runs automated tests
* ✅ Builds a Docker image
* ✅ Pushes the image to Docker Hub
* ✅ Simulates deployment to Production
* ✅ Performs scheduled health checks
* ✅ Uses reusable GitHub workflows to avoid duplication

The goal of this project is to learn industry-standard CI/CD practices using GitHub Actions.

---

# 🛠 Tech Stack

* Python 3.13
* Flask
* Pytest
* Docker
* GitHub Actions
* Docker Hub

---

# 📂 Project Structure

```text
.
├── .github
│   └── workflows
│       ├── reusable-build.yml
│       ├── reusable-docker.yml
│       ├── pr-pipeline.yml
│       ├── main-pipeline.yml
│       └── health-check.yml
│
├── tests
│   └── test_app.py
│
├── app.py
├── requirements.txt
├── dockerfile
├── .dockerignore
└── README.md
```

---

# ⚙️ Workflows

## 1️⃣ Reusable Build & Test

**File**

```text
.github/workflows/reusable-build-test.yml
```

### Trigger

* workflow_call

### Responsibilities

* Checkout source code
* Setup Python
* Install dependencies
* Run Pytest
* Return test result

Output

```text

```

---

## 2️⃣ Reusable Docker Workflow

**File**

```text
.github/workflows/reusable-docker.yml
```

### Trigger

* workflow_call

### Responsibilities

* Checkout repository
* Login to Docker Hub
* Build Docker image
* Push image
* Return image URL

Output

```text
image_url
```

---

## 3️⃣ Pull Request Workflow

**File**

```text
.github/workflows/pr.yml
```

### Trigger

```text
pull_request
```

### Runs on

* opened
* synchronize

### Pipeline

```
PR Opened
      │
      ▼
Reusable Build & Test
      │
      ▼
PR Checks Passed
```

Docker images are **NOT** built during Pull Requests.

---

## 4️⃣ Main CI/CD Pipeline

**File**

```text
.github/workflows/main-pipeline.yml
```

### Trigger

```text
push
```

Branch

```text
main
```

### Pipeline

```
Push to main
      │
      ▼
Reusable Build & Test
      │
      ▼
Reusable Docker Build & Push
      │
      ▼
Deploy to Production
```

Docker Tags

```
latest

sha-<short-commit-hash>
```

Deployment uses the GitHub Environment

```
production
```

If protection rules are enabled, deployment requires manual approval.

---

## 5️⃣ Scheduled Health Check

**File**

```text
.github/workflows/health-check.yml
```

### Triggers

Every 12 Hours

```
0 */12 * * *
```

Manual

```
workflow_dispatch
```

### Health Check Flow

```
Pull latest image
        │
        ▼
Run Docker container
        │
        ▼
Wait 5 seconds
        │
        ▼
Call /health endpoint
        │
        ▼
PASS / FAIL
        │
        ▼
Stop container
        │
        ▼
Generate GitHub Summary
```

---

# 🐳 Docker

Build Image

```bash
docker build -t flask-app .
```

Run Container

```bash
docker run -d -p 8080:80 flask-app
```

Health Endpoint

```
http://localhost:8080/health
```

---

# 🧪 Running Tests

Install dependencies

```bash
pip install -r requirements.txt
```

Run tests

```bash
pytest
```

---

# 🌐 Flask Endpoints

| Endpoint  | Description           |
| --------- | --------------------- |
| `/`       | Home Page             |
| `/health` | Health Check Endpoint |

---

# 🔄 Complete Pipeline Architecture

```
                     Pull Request
                           │
                           ▼
                Reusable Build & Test
                           │
                           ▼
                  PR Checks Passed



                     Push to main
                           │
                           ▼
                Reusable Build & Test
                           │
                           ▼
                 Docker Build & Push
                           │
                           ▼
               Deploy to Production



                 Every 12 Hours
                           │
                           ▼
               Pull Docker Image
                           │
                           ▼
                Run Container
                           │
                           ▼
               Health Endpoint
                           │
                           ▼
              PASS / FAIL Report
```

---

# 📋 Features

* Reusable GitHub Workflows
* Docker Image Build & Push
* Pull Request Validation
* Automatic Testing
* Production Deployment
* Environment Protection
* Docker Health Checks
* GitHub Step Summary
* Scheduled Workflows
* Manual Workflow Dispatch
* Docker Hub Integration

---

# 📚 GitHub Actions Concepts Used

* workflow_call
* workflow_dispatch
* schedule
* push
* pull_request
* jobs
* needs
* outputs
* inputs
* secrets
* environments
* reusable workflows
* docker/login-action
* docker/build-push-action
* actions/checkout
* actions/setup-python
* if conditions
* always()
* GitHub Step Summary
* GitHub Secrets

---

# 🚀 Future Improvements

* Kubernetes Deployment
* Helm Charts
* Trivy Container Scanning
* SonarQube Analysis
* CodeQL Security Scanning
* Slack Notifications
* AWS EC2 Deployment
* Kubernetes Health Checks
* Terraform Infrastructure
* ArgoCD Continuous Delivery

---

# 👨‍💻 Author

**Harsh Bhagat**

Learning DevOps • DevSecOps • Cloud • Docker • GitHub Actions

---

## ⭐ If you found this project helpful, don't forget to star the repository!

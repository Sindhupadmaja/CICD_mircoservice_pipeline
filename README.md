# Project 2 — CI/CD Microservice Pipeline

## Real-world problem
A development team needs repeatable releases for a small API while reducing deployment errors and enabling safe rollback.

## Engineering goals
- Automated test/build/package pipeline
- Docker image
- Kubernetes deployment
- Terraform infrastructure definition
- Secrets pattern
- Health checks
- Environment promotion
- Rollback-ready deployment

## Run locally
```bash
docker build -t orders-api:local .
docker run --rm -p 8080:8080 orders-api:local
```

## Kubernetes
```bash
kubectl apply -f k8s/
kubectl rollout status deployment/orders-api
```

## Terraform
The Terraform files demonstrate the infrastructure contract and intentionally avoid provider-specific cloud credentials.

## Portfolio story
Explain this as a reliability problem: the objective is not simply "deploy an API", but make releases repeatable, observable and recoverable.

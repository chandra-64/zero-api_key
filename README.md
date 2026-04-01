# ZERO-KEY_API: Secure CI/CD to Google Cloud

A high-performance Python API deployed to Google Cloud Run using a fully automated, Zero-Key CI/CD pipeline via GitHub Actions and Workload Identity Federation (WIF).

---

## Architecture & Tech Stack

- **Language:** Python (FastAPI / Flask)
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Cloud Provider:** Google Cloud Platform (GCP)
- **Registry:** Artifact Registry
- **Compute:** Cloud Run (Serverless)
- **Security:** Workload Identity Federation (OIDC-based keyless authentication)

---

## Security Highlights (WIF)

Unlike traditional methods that rely on long-lived Service Account JSON keys, this project uses **Workload Identity Federation**.

- **Keyless Authentication:** GitHub Actions exchanges a short-lived OIDC token for GCP credentials
- **Least Privilege:** Service Account is restricted to:
  - Artifact Registry Writer
  - Cloud Run Developer
- **No Secret Leakage:** No Google Cloud keys stored in GitHub Secrets

---

## CI/CD Pipeline Flow

Every push to the `main` branch triggers:

1. **Authenticate**
   - Connects to GCP using Workload Identity Federation

2. **Build**
   - Builds a production-ready Docker image

3. **Push**
   - Tags image with GitHub SHA
   - Pushes to Artifact Registry

4. **Deploy**
   - Updates Cloud Run service with the latest image

---

## Project Structure

```plaintext
zero-key-api/
├── .github/workflows/deploy.yml  # CI/CD pipeline
├── app/                          # Application source code
├── Dockerfile                    # Container configuration
├── requirements.txt              # Python dependencies
└── .dockerignore                 # Optimizes image size
```

---

## Local Development

Run the project locally using Docker:

```bash
# Build the Docker image
docker build -t zero-key-api .

# Run the container
docker run -p 8080:8080 zero-key-api
```

---

## Notes

- Ensure Docker is installed and running
- Default app runs on port `8080`
- Configure environment variables if required by your app

---


## License

This project is licensed under the MIT License.
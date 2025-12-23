# Docker commands used (with purpose)

## Core workflow

- `docker compose up -d --build --force-recreate`  
  Purpose: Build images (if needed) and recreate containers so the running containers use the latest images.

- `docker compose down`  
  Purpose: Stop and remove containers/networks created by Compose (volumes remain unless `-v` is used).

- `docker compose ps`  
  Purpose: Verify running status and health of services.

## Debugging

- `docker compose logs --no-color --tail=200 backend`  
  Purpose: Inspect backend logs to diagnose boot failures (e.g., Gunicorn import errors).

## Image analysis (assignment requirement)

- `docker images`  
  Purpose: Record image sizes.

- `docker history <image:tag>`  
  Purpose: Record number of layers and per-layer sizes.  
  Evidence: Paste outputs in `docs/image-analysis.md`.

## Registry / Docker Hub (assignment requirement)

- `docker login`  
  Purpose: Authenticate to Docker Hub before pushing images.

- `docker compose push frontend backend`  
  Purpose: Push service images to Docker Hub registries defined by `image:` in compose.  
  Evidence: Paste outputs in `docs/dockerhub-push.md`.

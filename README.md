# TNA Python FastAPI Application

## Quickstart

```sh
# Build and start the container
docker compose up -d
```

### Endpoints

- Docs: http://localhost:83/docs
- OpenAPI schema: http://localhost:83/openapi.json
- Build details: http://localhost:83/api/version/
- Healthcheck: http://localhost:83/healthcheck/live/
- Example: http://localhost:83/api/v1/hello/

### Run tests

```sh
docker compose exec app poetry run python -m pytest
```

### Format and lint code

```sh
docker compose exec app format
```

## Environment variables

In addition to the [base Docker image variables](https://github.com/nationalarchives/docker/blob/main/docker/tna-python/README.md#environment-variables), this application has support for:

| Variable      | Purpose                    | Default             |
| ------------- | -------------------------- | ------------------- |
| `CONFIG`      | The configuration to use   | `config.Production` |
| `BASE_URI`    | The base URI for the API   | `/api/`             |
| `FORCE_HTTPS` | Redirect requests to HTTPS | _none_              |

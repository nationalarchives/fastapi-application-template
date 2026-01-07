# TNA Python FastAPI Application

## Quickstart

```sh
# Build and start the container
docker compose up -d
```

### Endpoints

- Docs: http://localhost:83/docs (Do not remove)
- OpenAPI schema: http://localhost:83/openapi.json (Do not remove)
- Build details: http://localhost:83/build/ (Do not remove - requires `CONTAINER_IMAGE` and `BUILD_VERSION` from CI/CD)
- Healthcheck: http://localhost:83/healthcheck/live/ (Do not remove)
- Application example endpoint: http://localhost:83/api/v1/hello/

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

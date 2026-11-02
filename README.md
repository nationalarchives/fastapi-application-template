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

### Server logging

The container's `tna-asgi` launcher passes the `LOG_LEVEL` environment variable
to Uvicorn's `--log-level` option. `LOG_LEVEL` can be configured via environment variables
to change the logging level.
Supported levels are `critical`, `error`, `warning`, `info`, `debug` and `trace`.
The base Docker image defaults to `warning` - set `LOG_LEVEL` in the environment to override it.

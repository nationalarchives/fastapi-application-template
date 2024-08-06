# TNA Python FastAPI Application

## Quickstart

```sh
# Build and start the container
docker compose up -d
```

### Docs

http://localhost:83/docs

### Run tests

```sh
docker compose exec dev poetry run python -m pytest
```

### Format and lint code

```sh
docker compose exec dev format
```

## Environment variables

In addition to the [base Docker image variables](https://github.com/nationalarchives/docker/blob/main/docker/tna-python/README.md#environment-variables), this application has support for:

| Variable      | Purpose                                       | Default             |
| ------------- | --------------------------------------------- | ------------------- |
| `CONFIG`      | The configuration to use                      | `config.Production` |
| `BASE_URI`    | The base URI for the API                      | `/api/v1`           |
| `FORCE_HTTPS` | Redirect requests to HTTPS as part of the CSP | _none_              |

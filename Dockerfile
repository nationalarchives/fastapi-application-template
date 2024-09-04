ARG IMAGE=ghcr.io/nationalarchives/tna-python
ARG IMAGE_TAG=latest

FROM "$IMAGE":"$IMAGE_TAG"

ARG BUILD_VERSION
ENV BUILD_VERSION="$BUILD_VERSION"

# Copy in the dependencies config
COPY --chown=app pyproject.toml poetry.lock ./

# Install the dependencies
RUN tna-build

# Copy in the application code
COPY --chown=app . .

# Delete tests and docs
RUN rm -fR /app/test /app/docs

# Run the application
CMD ["tna-run", "-a", "fastapi_app:app"]

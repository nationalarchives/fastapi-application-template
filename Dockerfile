ARG IMAGE=ghcr.io/nationalarchives/tna-python
ARG IMAGE_TAG=1

FROM "$IMAGE":"$IMAGE_TAG"

ARG CONTAINER_IMAGE
ENV CONTAINER_IMAGE="$CONTAINER_IMAGE"
ARG BUILD_VERSION
ENV BUILD_VERSION="$BUILD_VERSION"

# Copy in the dependencies config
COPY --chown=app pyproject.toml poetry.lock ./

# Install the dependencies
RUN tna-build

# Copy in the application code
COPY --chown=app . .

# Clean up build dependencies
RUN tna-clean

# Run the application
CMD ["tna-asgi", "main:app"]

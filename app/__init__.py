from app.lib.get_config import get_config
from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware


def create_app(config_class):
    config = get_config(config_class)

    app = FastAPI(title="TNA FastAPI Application", log_level=config.get("LOG_LEVEL"))
    app.state.config = {"BASE_URI": config.get("BASE_URI")}
    if config.get("FORCE_HTTPS"):
        app.add_middleware(HTTPSRedirectMiddleware)

    @app.get("/", tags=["home"], include_in_schema=False)
    async def home():
        return {
            "title": app.title,
            "description": "Get started building a National Archives FastAPI application.",
            "useful_links": [
                {
                    "url": "https://nationalarchives.github.io/engineering-handbook/",
                    "description": "The National Archives Engineering Handbook",
                },
                {
                    "url": "https://github.com/nationalarchives/docker",
                    "description": "The National Archives base Docker images",
                },
                {
                    "url": "https://github.com/nationalarchives/ds-docker-actions",
                    "description": "Digital Services Docker build actions",
                },
            ],
            "api_endpoints": [
                {
                    "url": "http://localhost:83/docs",
                    "description": "API documentation and testing interface",
                    "note": "Do not remove",
                },
                {
                    "url": "http://localhost:83/redoc",
                    "description": "Alternative API documentation interface",
                    "note": "Do not remove",
                },
                {
                    "url": "http://localhost:83/openapi.json",
                    "description": "OpenAPI schema for the application",
                    "note": "Do not remove",
                },
                {
                    "url": "http://localhost:83/build/",
                    "description": "Build details for the application",
                    "note": "Do not remove",
                },
                {
                    "url": "http://localhost:83/healthcheck/live/",
                    "description": "Healthcheck endpoint for the application",
                    "note": "Do not remove",
                },
            ],
        }

    from .build import routes as build_routes
    from .healthcheck import routes as healthcheck_routes
    from .hello import routes as hello_routes

    def prefix_url(path: str, version: int = 0) -> str:
        return f"/{config['BASE_URI'].strip('/')}{f'/v{version}' if version else ''}/{path.strip('/')}"

    app.include_router(
        healthcheck_routes.router,
        prefix="/healthcheck",
        tags=["Debug"],
        include_in_schema=False,
    )
    app.include_router(build_routes.router, prefix="/build", tags=["Debug"])
    app.include_router(
        hello_routes.router,
        prefix=prefix_url("hello", 1),
        tags=["Application"],
    )

    return app

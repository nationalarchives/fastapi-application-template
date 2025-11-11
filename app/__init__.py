from app.lib.get_config import get_config
from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware


def create_app(config_class):
    config = get_config(config_class)

    app = FastAPI(title="TNA FastAPI Application", log_level=config.get("LOG_LEVEL"))
    app.state.config = {"BASE_URI": config.get("BASE_URI")}
    if config.get("FORCE_HTTPS"):
        app.add_middleware(HTTPSRedirectMiddleware)

    @app.get("/", tags=["home"])
    async def home():
        return {
            "title": app.title,
            "description": "Get started building a National Archives FastAPI application.",
            "useful_links": [
                {
                    "The National Archives Engineering Handbook": "https://nationalarchives.github.io/engineering-handbook/"
                },
                {
                    "Backend resources": [
                        {
                            "The National Archives base Docker images": "https://github.com/nationalarchives/docker",
                            "Digital Services Docker build actions": "https://github.com/nationalarchives/ds-docker-actions",
                        }
                    ]
                },
            ],
        }

    from .healthcheck import routes as healthcheck_routes
    from .hello import routes as hello_routes
    from .version import routes as version_routes

    def prefix_url(path: str, version: int = 0) -> str:
        return f"/{config.get('BASE_URI').strip('/')}{f'/v{version}' if version else ''}/{path.strip('/')}"

    app.include_router(healthcheck_routes.router, prefix="/healthcheck")
    app.include_router(version_routes.router, prefix=prefix_url("version"))
    app.include_router(
        hello_routes.router,
        prefix=prefix_url("hello", 1),
        tags=["Example"],
    )

    return app

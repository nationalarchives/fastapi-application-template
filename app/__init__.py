from app.lib.get_config import get_config
from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware


def create_app(config_class):
    config = get_config(config_class)

    app = FastAPI(
        title="TNA FastAPI Application", log_level=config.get("LOG_LEVEL")
    )
    app.state.config = {"BASE_URI": config.get("BASE_URI")}
    if config.get("FORCE_HTTPS"):
        app.add_middleware(HTTPSRedirectMiddleware)

    from .greetings import routes as greetings_routes
    from .healthcheck import routes as healthcheck_routes

    app.include_router(healthcheck_routes.router, prefix="/healthcheck")
    app.include_router(
        greetings_routes.router,
        prefix=f"{config.get('BASE_URI')}/greetings",
        tags=["Examples"],
    )

    return app

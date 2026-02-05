


from app.api.v1.prices import router as price_router


def include_routers(app):
    app.include_router(price_router)

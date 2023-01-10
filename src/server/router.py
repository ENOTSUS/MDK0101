from src.server.routers import user, order, cuisine, dish, menu

routers = (
    user.router,
    order.router,
    cuisine.router,
    dish.router,
    menu.router,
    )

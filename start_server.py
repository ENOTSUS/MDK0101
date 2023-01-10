import uvicorn
import fastapi
from fastapi.responses import RedirectResponse
from src.server.router import routers
from src.database.dbmanager import DbManager
import settings

app = fastapi.FastAPI()

[app.include_router(router) for router in routers]


@app.router.get('/', include_in_schema=False)
def index() -> RedirectResponse:
    return RedirectResponse('/docs')


if __name__ == '__main__':
    DbManager(settings.DATABASE_PATH).create_db(f'{settings.SQL_SCRIPTS_DIR}/create.sql')

    uvicorn.run('start_server:app', reload=True, host=settings.SERVER_HOST, port=settings.SERVER_PORT)

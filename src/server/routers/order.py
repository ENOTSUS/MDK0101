import fastapi
from src.server.resolves import order as resolve
from src.database.models import Orders as Model

router = fastapi.APIRouter(prefix='/order', tags=['Order'])


@router.get('/get/{id_}', response_model=Model | None)
def get(id_: int) -> Model | None:
    return resolve.get(id_)


@router.get('/get_all', response_model=list[Model] | dict)
def get_all() -> list[Model] | dict:
    return resolve.get_all()


@router.delete('/delete/{id_}', response_model=None)
def remove(id_: int) -> None:
    return resolve.delete(id_)


@router.post('/create/', response_model=Model | dict)
def create(new: Model) -> Model | dict:
    return resolve.create(new)


@router.put("/update/{id_}", response_model=None)
def update(id_: int, new_data: Model):
    return resolve.update(id_, new_data)

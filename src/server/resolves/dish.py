from src.database.models import Dish as Model
from src.server.resolves.order import dbmanager


def get(id_: int) -> Model | None:
    res = dbmanager.execute_query(
        query=f'select * from {Model.__name__} where id=(?)',
        args=(id_,))

    return None if not res else Model(
        id=res[0],
        name=res[1],
        cooking_time=res[2],
        cuisine_id=res[3]
    )


def get_all() -> list[Model] | dict:
    l = dbmanager.execute_query(
        query=f"select * from {Model.__name__}",
        fetchone=False)

    result = []

    if l:
        for res in l:
            res.append(Model(
                id=res[0],
                name=res[1],
                cooking_time=res[2],
                cuisine_id=res[3]
            ))

    return result


def delete(id_: int) -> None:
    return dbmanager.execute_query(
        query=f'delete from {Model.__name__} where id=(?)',
        args=(id_,))


def create(new: Model) -> int | dict:
    res = dbmanager.execute_query(
        query=f"insert into {Model.__name__} (name, cooking_time, cuisine_id) values(?,?,?) returning id",
        args=(new.name, new.cooking_time, new.cuisine_id))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(id_: int, new: Model) -> None:
    return dbmanager.execute_query(
        query=f"update {Model.__name__} set (name, cooking_time, cuisine_id) values(?,?,?) where id=(?)",
        args=(new.name, new.cooking_time, new.cuisine_id, id_))

from src.database.models import Menu as Model
from src.server.resolves.order import dbmanager


def get(id_: int) -> Model | None:
    res = dbmanager.execute_query(
        query=f'select * from {Model.__name__} where id=(?)',
        args=(id_,))

    return None if not res else Model(
        id=res[0],
        price=res[1],
        dish_id=res[2]
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
                price=res[1],
                dish_id=res[2]
            ))

    return result


def delete(id_: int) -> None:
    return dbmanager.execute_query(
        query=f'delete from {Model.__name__} where id=(?)',
        args=(id_,))


def create(new: Model) -> int | dict:
    res = dbmanager.execute_query(
        query=f"insert into {Model.__name__} (price, dish_id) values(?,?) returning id",
        args=(new.price, new.dish_id))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(id_: int, new: Model) -> None:
    return dbmanager.execute_query(
        query=f"update {Model.__name__} set (price, dish_id) = (?,?) where id=(?)",
        args=(new.price, new.dish_id, id_))

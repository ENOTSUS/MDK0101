from src.database.models import Orders as Model
from src.database.dbmanager import DbManager
import settings

dbmanager = DbManager(db_path=settings.DATABASE_PATH)


def get(id_: int) -> Model | None:
    res = dbmanager.execute_query(
        query=f'select * from {Model.__name__} where id=(?)',
        args=(id_,))

    return None if not res else Model(
        id=res[0],
        datetime=res[1],
        menu_position_id=res[2],
        user_id=res[3]
    )


def get_all() -> list[Model] | dict:
    l = dbmanager.execute_query(
        query=f"select * from {Model.__name__}",
        fetchone=False)

    result = []

    if l:
        for res in l:
            result.append(Model(
                id=res[0],
                datetime=res[1],
                menu_position_id=res[2],
                user_id=res[3]
            ))

    return result


def delete(id_: int) -> None:
    return dbmanager.execute_query(
        query=f'delete from {Model.__name__} where id=(?)',
        args=(id_,))


def create(new: Model) -> int | dict:
    res = dbmanager.execute_query(
        query=f"insert into {Model.__name__} (datetime, menu_positionID, userID) values(?,?,?) returning id",
        args=(new.datetime, new.menu_position_id, new.user_id))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(id_: int, new: Model) -> None:
    return dbmanager.execute_query(
        query=f"update {Model.__name__} set (datetime, menu_positionID, userID) = (?,?,?) where id=(?)",
        args=(new.datetime, new.menu_position_id, new.user_id, id_))

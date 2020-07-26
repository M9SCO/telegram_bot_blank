from logging import info, error
from typing import Optional, Tuple, Any

from psycopg2 import connect, InterfaceError

from bin.config import db_host, db_name, db_user, db_pass


def connection_to_database() -> Tuple[connect, connect]:
    cnx: connect = connect(host=db_host, dbname=db_name, user=db_user, password=db_pass)
    cnx.set_session(autocommit=True)
    return cnx, cnx.cursor()


def get_one_row(req: str, args: Optional[Tuple[Any]] = None) -> Optional[Tuple[Any]]:
    global cnx, cursor
    try:
        cursor.execute(req, args)
        return cursor.fetchone()
    except InterfaceError:
        info("reconnect to database")
        cnx, cursor = connection_to_database()
        return get_one_row(req, args)
    except Exception as e:
        error(e)
        return None


def get_all_row(req: str, args: Optional[Tuple[Any]] = None) -> Optional[Tuple[Any]]:
    global cnx, cursor
    try:
        cursor.execute(req, args)
        return cursor.fetchall()
    except InterfaceError:
        info("reconnect to database")
        cnx, cursor = connection_to_database()
        return get_all_row(req, args)
    except Exception as e:
        error(e)
        return None


def sql_set(req: str, args: Optional = None) -> bool:
    global cnx, cursor
    try:
        cursor.execute(req, args)
        cnx.commit()
        return True
    except InterfaceError:
        info("reconnect to database")
        cnx, cursor = connection_to_database()
        return sql_set(req, args)
    except Exception as e:
        error(e)
        return False

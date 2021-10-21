# pylint: disable=E1101
from src.infra.config import DBConnectionHandler
from src.infra.entities import Empresas


class FakerRepo:
    """Simple Repository"""

    @classmethod
    def insert_empresa(cls):
        """something"""

    with DBConnectionHandler() as db_connection:
        try:
            new_empresa = Empresas(name="Empresa Teste 2")
            db_connection.session.add(new_empresa)
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

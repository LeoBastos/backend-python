# pylint: disable=E1101
from collections import namedtuple
from src.infra.config import DBConnectionHandler
from src.infra.entities import Empresas


class EmpresaRepository:
    """Empresa Repository"""

    @classmethod
    def insert_empresa(cls, name: str) -> Empresas:
        """
        Insert data in Table Empresa
        :param - name: nome da empresa
        :return - tuple with new Company inserted
        """

        InsertData = namedtuple("Empresas", "id, name, dataEmpresa")

        with DBConnectionHandler() as db_connection:
            try:
                new_empresa = Empresas(name=name)
                db_connection.session.add(new_empresa)
                db_connection.session.commit()
                return InsertData(
                    id=new_empresa.id,
                    name=new_empresa.name,
                    dataEmpresa=new_empresa.dataEmpresa,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

# pylint: disable=E1101
from typing import List
from sqlalchemy.exc import DisconnectionError
from src.domain.models import Empresas
from src.infra.config import DBConnectionHandler
from src.infra.entities import Empresas as EmpresasModel


class EmpresaRepository:
    """Empresa Repository"""

    @classmethod
    def insert_empresa(cls, name: str) -> EmpresasModel:
        """
        Insert data in Table Empresa
        :param - name: nome da empresa
        :return - tuple with new Company inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_empresa = EmpresasModel(name=name)
                db_connection.session.add(new_empresa)
                db_connection.session.commit()
                return Empresas(
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

    @classmethod
    def select_empresa(
        cls, empresa_id: int = None, name: str = None
    ) -> List[EmpresasModel]:
        """
        Select data in empresa entity by id and/or name
        :params: - empresa_id: Id
                - name: empresa name
        :return  - List with Empresas Selected
        """
        try:
            query_data = None

            if empresa_id and not name:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(EmpresasModel)
                        .filter_by(id=empresa_id)
                        .one()
                    )
                    query_data = [data]

            elif not empresa_id and name:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(EmpresasModel)
                        .filter_by(name=name)
                        .one()
                    )
                    query_data = [data]

            elif empresa_id and name:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(EmpresasModel)
                        .filter_by(id=empresa_id, name=name)
                        .one()
                    )
                    query_data = [data]

            return query_data

        except Exception as ex:
            DisconnectionError.session.rollback()
            print(ex)
            raise
        finally:
            db_connection.session.close()

        return None

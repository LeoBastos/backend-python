from faker import Faker
from src.infra.config import DBConnectionHandler
from .empresa_repository import EmpresaRepository


faker = Faker()
empresa_repository = EmpresaRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_user():
    """Should Insert Empresa"""

    name = faker.name()
    engine = db_connection_handler.get_engine()

    # SQL Commands
    new_empresa = empresa_repository.insert_empresa(name)
    query_empresa = engine.execute(
        "SELECT * FROM empresas WHERE id='{}';".format(new_empresa.id)
    ).fetchone()

    engine.execute("DELETE FROM empresas WHERE id='{}';".format(new_empresa.id))

    assert new_empresa.id == query_empresa.id
    assert new_empresa.name == query_empresa.name

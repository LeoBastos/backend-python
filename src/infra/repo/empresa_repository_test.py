from faker import Faker
from src.infra.config import DBConnectionHandler
from .empresa_repository import EmpresaRepository
from src.infra.entities import Empresas as EmpresasModel


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


def test_select_empresa():
    """Should returns data from company table and compare it"""

    empresa_id = faker.random_number(digits=5)
    name = faker.name()
    data = EmpresasModel(id=empresa_id, name=name)

    engine = db_connection_handler.get_engine()
    engine.execute(
        "INSERT INTO empresas(id, name) VALUES ('{}', '{}');".format(empresa_id, name)
    )

    query_empresa1 = empresa_repository.select_empresa(empresa_id=empresa_id)
    query_empresa2 = empresa_repository.select_empresa(name=name)
    query_empresa3 = empresa_repository.select_empresa(empresa_id=empresa_id, name=name)

    assert data in query_empresa1
    assert data in query_empresa2
    assert data in query_empresa3

    engine.execute("DELETE FROM empresas WHERE id='{}';".format(empresa_id))

from datetime import datetime
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DATETIME
from src.infra.config import Base


class Empresas(Base):
    """Empresa Entity"""

    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    dataEmpresa = Column(DATETIME, default=datetime.now())
    id_modulo = relationship("Modulos")

    def __repr__(self) -> str:
        return f"User [name={self.name}]"

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from src.infra.config import Base


class Modulos(Base):
    """Modulos Entity"""

    __tablename__ = "modulos"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    version = Column(Integer, nullable=False)
    url = Column(String, nullable=False)
    isActive = Column(Boolean, unique=False, default=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))

    def __rep__(self):
        return f"Modulo:[name={self.name},version={self.version},isActive={self.isActive},empresa_id={self.empresa_id}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
            and self.version == other.version
            and self.isActive == other.isActive
            and self.empresa_id == other.empresa_id
        ):
            return True
        return False

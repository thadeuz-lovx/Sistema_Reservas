from backend.database import Base
from sqlalchemy import Column, String, Integer

class ClientSave(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    referencia = Column(String, nullable=False)
    email = Column(String, nullable=False)
    codigo = Column(String, nullable=False)
    estado = Column(String, nullable=False)
from backend.database import Base, engine
from sqlalchemy import Column, String, Integer

class AdminSave(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    estado = Column(String, nullable=False)


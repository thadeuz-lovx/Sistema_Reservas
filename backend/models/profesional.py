from sqlalchemy import Column, String, Integer
from backend.database import Base

class ProfessionalSave(Base):
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    especialidad = Column(String, nullable=False)
    codigo = Column(String, nullable=False)
    estado = Column(String, nullable=False)

from sqlalchemy.orm import Session
from backend.models.profesional import ProfessionalSave
from src.profesional.schemas import ProfessionalUptade 

class ProfessionalCRUDs:
    @staticmethod
    def crear(
        db: Session, 
        nombre: str, 
        apellido: str, 
        especialidad: str, 
        codigo: str, 
        estado: str
    ):
        nuevo_prof = ProfessionalSave(
            nombre=nombre, 
            apellido=apellido, 
            especialidad=especialidad, 
            codigo=codigo, 
            estado=estado
        )
        db.add(nuevo_prof)
        db.commit()
        db.refresh(nuevo_prof)
        return nuevo_prof

    @staticmethod
    def ver(db: Session):
        return db.query(ProfessionalSave).all()

    @staticmethod
    def ver_id(db: Session, id_prf: int):
        return db.query(ProfessionalSave).filter(ProfessionalSave.id == id_prf).first()

    @staticmethod
    def actualizar(db: Session, id_prf: int, user_prf: ProfessionalUptade):
        busqueda = db.query(ProfessionalSave).filter(ProfessionalSave.id == id_prf).first()
        if not busqueda:
            return None
        
        datos_actualizar = user_prf.model_dump(exclude_unset=True)
        
        for k, v in datos_actualizar.items():
            setattr(busqueda, k, v)
            
        db.commit()
        db.refresh(busqueda)
        return busqueda

    @staticmethod
    def borrar(db: Session, id_prf: int):
        busqueda = db.query(ProfessionalSave).filter(ProfessionalSave.id == id_prf).first()
        if not busqueda:
            return False
            
        db.delete(busqueda)
        db.commit()
        return True

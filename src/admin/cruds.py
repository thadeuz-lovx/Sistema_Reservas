from backend.models.admin import AdminSave
from src.admin.schemas import AdminUptdate
from sqlalchemy.orm import Session

class AdminCRUDs:
    @staticmethod
    def crear_a(
        db: Session,
        nombre: str,
        apellido: str,
        estado: str
    ):
        nuevo_admin = AdminSave(
            nombre=nombre,
            apellido=apellido,
            estado=estado
        )

        db.add(nuevo_admin)
        db.commit()
        db.refresh(nuevo_admin)
        return nuevo_admin
    
    @staticmethod
    def ver_admins(db: Session):
        return db.query(AdminSave).all()
    
    @staticmethod
    def ver_admin_id(db: Session, id_adm: int):
        busqueda = db.query(AdminSave).filter(AdminSave.id == id_adm).first()

        if busqueda is None:
            return False
        
        return busqueda
    
    @staticmethod
    def actualizar_adm(db: Session, id_adm: int, admin_update: AdminUptdate):
        busqueda = db.query(AdminSave).filter(AdminSave.id == id_adm).first()

        if busqueda is None:
            return False
        
        update_data = admin_update.model_dump(exclude_unset=True)
                                        
        for k, v in update_data.items():
            setattr(busqueda, k, v)

        db.commit()
        db.refresh(busqueda)
        return True
    
    @staticmethod
    def borrar_adm(db: Session, id_adm: int):
        busqueda = db.query(AdminSave).filter(AdminSave.id == id_adm).first()
        if not busqueda:
            return False
        
        db.delete(busqueda)
        db.commit()
        return True
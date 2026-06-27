from src.cliente.schemas import ClientUpdate
from backend.models.cliente import ClientSave
from sqlalchemy.orm import Session

class ClientCRUDs:
    @staticmethod
    def crear(
        db: Session,
        nombre: str,
        apellido: str,
        referencia: str,
        email: str,
        estado: str,
        codigo: str
    ):
        nuevo_usuario = ClientSave(
            nombre=nombre,
            apellido=apellido,
            referencia=referencia,
            email=email,
            estado=estado,
            codigo=codigo
        )

        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)
        return nuevo_usuario
    
    @staticmethod
    def ver(db: Session):
        return db.query(ClientSave).all()
    
    @staticmethod
    def ver_por(db: Session, id_usr: int):
        busqueda = db.query(ClientSave).filter(ClientSave.id == id_usr).first()

        if not busqueda:
            return None
        
        return busqueda
    @staticmethod
    def actualizar(db: Session, id_usr: int, user_upd: ClientUpdate):
        busqueda = db.query(ClientSave).filter(ClientSave.id == id_usr).first()

        if not busqueda:
            return None
        
        actualizar_usuario = user_upd.model_dump(exclude_unset=True)

        for k, v in actualizar_usuario.items():
            setattr(actualizar_usuario, k, v)

        db.commit()
        db.refresh(busqueda)
        return busqueda
    
    @staticmethod
    def eliminar(db: Session, id_usr: int):
        busqueda = db.query(ClientSave).filter(ClientSave.id == id_usr).first()
        if not busqueda:
            return None
        
        db.delete(busqueda)
        db.commit()

        return True

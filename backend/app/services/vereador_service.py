"""Service para operações com Vereadores"""
from sqlalchemy.orm import Session
from app.models.vereador import Vereador
from app.schemas.vereador_schema import VereadorCreate, VereadorUpdate
from typing import List, Optional


class VereadorService:
    """Serviço de Vereador"""

    @staticmethod
    def criar(db: Session, vereador: VereadorCreate) -> Vereador:
        """Cria um novo vereador"""
        db_vereador = Vereador(**vereador.dict())
        db.add(db_vereador)
        db.commit()
        db.refresh(db_vereador)
        return db_vereador

    @staticmethod
    def obter_por_id(db: Session, vereador_id: int) -> Optional[Vereador]:
        """Obtém vereador por ID"""
        return db.query(Vereador).filter(Vereador.id == vereador_id).first()

    @staticmethod
    def listar(
        db: Session,
        skip: int = 0,
        limit: int = 10,
        partido: Optional[str] = None
    ) -> tuple[List[Vereador], int]:
        """Lista vereadores com filtros opcionais"""
        query = db.query(Vereador)
        
        if partido:
            query = query.filter(Vereador.partido == partido)
        
        total = query.count()
        vereadores = query.offset(skip).limit(limit).all()
        
        return vereadores, total

    @staticmethod
    def atualizar(
        db: Session,
        vereador_id: int,
        vereador_update: VereadorUpdate
    ) -> Optional[Vereador]:
        """Atualiza um vereador"""
        db_vereador = db.query(Vereador).filter(Vereador.id == vereador_id).first()
        
        if db_vereador:
            update_data = vereador_update.dict(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_vereador, field, value)
            db.commit()
            db.refresh(db_vereador)
        
        return db_vereador

    @staticmethod
    def deletar(db: Session, vereador_id: int) -> bool:
        """Deleta um vereador"""
        db_vereador = db.query(Vereador).filter(Vereador.id == vereador_id).first()
        
        if db_vereador:
            db.delete(db_vereador)
            db.commit()
            return True
        
        return False

    @staticmethod
    def obter_ranking_presenca(db: Session) -> List[dict]:
        """Retorna ranking de presença dos vereadores"""
        vereadores = db.query(Vereador).order_by(
            Vereador.presenca_sessoes.desc()
        ).all()
        
        return [
            {
                "id": v.id,
                "nome": v.nome,
                "presenca": v.presenca_sessoes,
                "total_sessoes": v.total_sessoes,
                "percentual": (v.presenca_sessoes / v.total_sessoes * 100) if v.total_sessoes > 0 else 0
            }
            for v in vereadores
        ]

    @staticmethod
    def obter_ranking_produtividade(db: Session) -> List[dict]:
        """Retorna ranking de produtividade dos vereadores"""
        vereadores = db.query(Vereador).order_by(
            Vereador.projetos_aprovados.desc()
        ).all()
        
        return [
            {
                "id": v.id,
                "nome": v.nome,
                "projetos_apresentados": v.projetos_apresentados,
                "projetos_aprovados": v.projetos_aprovados,
                "taxa_aprovacao": (v.projetos_aprovados / v.projetos_apresentados * 100) if v.projetos_apresentados > 0 else 0
            }
            for v in vereadores
        ]

"""Schemas Pydantic para Projeto de Lei"""
from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional
from enum import Enum


class ProjetoStatus(str, Enum):
    """Status do Projeto de Lei"""
    EM_TRAMITACAO = "em_tramitacao"
    APROVADO = "aprovado"
    VETADO = "vetado"
    ARQUIVADO = "arquivado"


class ProjetoLeiBase(BaseModel):
    """Base schema para Projeto de Lei"""
    numero: str
    titulo: str
    descricao: Optional[str] = None
    status: ProjetoStatus = ProjetoStatus.EM_TRAMITACAO
    data_protocolamento: Optional[date] = None
    autor: Optional[str] = None


class ProjetoLeiCreate(ProjetoLeiBase):
    """Schema para criar Projeto de Lei"""
    pass


class ProjetoLeiUpdate(BaseModel):
    """Schema para atualizar Projeto de Lei"""
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    status: Optional[ProjetoStatus] = None
    data_protocolamento: Optional[date] = None
    data_aprovacao: Optional[date] = None
    data_veto: Optional[date] = None
    autor: Optional[str] = None
    explicacao_ia: Optional[str] = None


class ProjetoLeiResponse(ProjetoLeiBase):
    """Schema de resposta para Projeto de Lei"""
    id: int
    data_aprovacao: Optional[date]
    data_veto: Optional[date]
    explicacao_ia: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ProjetoLeiDetailResponse(ProjetoLeiResponse):
    """Schema detalhado de Projeto de Lei com votações"""
    votos: Optional[dict] = None
    votacoes_por_vereador: Optional[list] = None


class ProjetoLeiListResponse(BaseModel):
    """Schema para listagem de Projetos de Lei"""
    total: int
    items: list[ProjetoLeiResponse]

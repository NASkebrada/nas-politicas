"""Schemas Pydantic para Vereador"""
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, Dict, Any


class VereadorBase(BaseModel):
    """Base schema para Vereador"""
    nome: str
    partido: Optional[str] = None
    contato: Optional[str] = None
    redes_sociais: Optional[Dict[str, Any]] = None
    historico_politico: Optional[str] = None
    foto_url: Optional[str] = None


class VereadorCreate(VereadorBase):
    """Schema para criar Vereador"""
    pass


class VereadorUpdate(BaseModel):
    """Schema para atualizar Vereador"""
    nome: Optional[str] = None
    partido: Optional[str] = None
    contato: Optional[str] = None
    redes_sociais: Optional[Dict[str, Any]] = None
    historico_politico: Optional[str] = None
    foto_url: Optional[str] = None
    presenca_sessoes: Optional[int] = None
    total_sessoes: Optional[int] = None
    projetos_apresentados: Optional[int] = None
    projetos_aprovados: Optional[int] = None
    indicacoes: Optional[int] = None
    requerimentos: Optional[int] = None


class VereadorResponse(VereadorBase):
    """Schema de resposta para Vereador"""
    id: int
    presenca_sessoes: int
    total_sessoes: int
    projetos_apresentados: int
    projetos_aprovados: int
    indicacoes: int
    requerimentos: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class VereadorListResponse(BaseModel):
    """Schema para listagem de Vereadores"""
    total: int
    items: list[VereadorResponse]

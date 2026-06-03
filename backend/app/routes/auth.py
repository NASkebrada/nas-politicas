"""Rotas de Autenticação"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import Usuario
from app.schemas.usuario_schema import (
    UsuarioCreate,
    UsuarioResponse,
    UsuarioLogin,
    Token
)
from app.auth import (
    obter_hash_senha,
    verificar_senha,
    criar_access_token,
    criar_refresh_token,
    verificar_token
)
from fastapi.security import HTTPBearer, HTTPAuthCredentials

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])
security = HTTPBearer()


@router.post("/register", response_model=UsuarioResponse, status_code=201)
async def registrar(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    """Registra um novo usuário"""
    # Verificar se email já existe
    db_usuario = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if db_usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já cadastrado"
        )
    
    # Criar novo usuário
    novo_usuario = Usuario(
        email=usuario.email,
        nome=usuario.nome,
        senha_hash=obter_hash_senha(usuario.senha)
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    
    return novo_usuario


@router.post("/login", response_model=Token)
async def login(usuario: UsuarioLogin, db: Session = Depends(get_db)):
    """Faz login e retorna tokens"""
    # Buscar usuário
    db_usuario = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    
    if not db_usuario or not verificar_senha(usuario.senha, db_usuario.senha_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos"
        )
    
    if not db_usuario.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuário inativo"
        )
    
    # Criar tokens
    access_token = criar_access_token({"sub": db_usuario.email, "user_id": db_usuario.id})
    refresh_token = criar_refresh_token({"sub": db_usuario.email, "user_id": db_usuario.id})
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "expires_in": 1800
    }


@router.post("/refresh", response_model=Token)
async def refresh_token(credentials: HTTPAuthCredentials = Depends(security), db: Session = Depends(get_db)):
    """Atualiza o token de acesso usando o refresh token"""
    token_data = verificar_token(credentials.credentials)
    
    if not token_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado"
        )
    
    # Buscar usuário
    db_usuario = db.query(Usuario).filter(Usuario.email == token_data.email).first()
    
    if not db_usuario or not db_usuario.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuário não encontrado ou inativo"
        )
    
    # Criar novo token
    access_token = criar_access_token({"sub": db_usuario.email, "user_id": db_usuario.id})
    
    return {
        "access_token": access_token,
        "refresh_token": credentials.credentials,
        "token_type": "bearer",
        "expires_in": 1800
    }


@router.get("/me", response_model=UsuarioResponse)
async def obter_usuario_atual(credentials: HTTPAuthCredentials = Depends(security), db: Session = Depends(get_db)):
    """Obtém informações do usuário autenticado"""
    token_data = verificar_token(credentials.credentials)
    
    if not token_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado"
        )
    
    db_usuario = db.query(Usuario).filter(Usuario.email == token_data.email).first()
    
    if not db_usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )
    
    return db_usuario

"""Autenticação JWT"""
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from app.config import get_settings

settings = get_settings()

# Contexto de criptografia para senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class TokenData(BaseModel):
    """Dados do token JWT"""
    email: Optional[str] = None
    user_id: Optional[int] = None


class Token(BaseModel):
    """Schema de resposta de token"""
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int


def verificar_senha(senha_plana: str, senha_hash: str) -> bool:
    """Verifica se a senha corresponde ao hash"""
    return pwd_context.verify(senha_plana, senha_hash)


def obter_hash_senha(senha: str) -> str:
    """Gera hash da senha"""
    return pwd_context.hash(senha)


def criar_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Cria um token de acesso JWT"""
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    
    return encoded_jwt


def criar_refresh_token(data: dict) -> str:
    """Cria um token de atualização JWT"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    
    return encoded_jwt


def verificar_token(token: str) -> Optional[TokenData]:
    """Verifica e decodifica um token JWT"""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            return None
        token_data = TokenData(email=email)
    except JWTError:
        return None
    
    return token_data

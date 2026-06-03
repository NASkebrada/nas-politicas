"""Testes para Vereadores"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_criar_vereador():
    """Testa criação de vereador"""
    vereador_data = {
        "nome": "João Silva",
        "partido": "PT",
        "contato": "(67) 3232-1234",
        "historico_politico": "Vereador desde 2021"
    }
    response = client.post("/api/v1/vereadores", json=vereador_data)
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == "João Silva"
    assert data["partido"] == "PT"


def test_listar_vereadores():
    """Testa listagem de vereadores"""
    response = client.get("/api/v1/vereadores")
    assert response.status_code == 200
    data = response.json()
    assert "total" in data
    assert "items" in data


def test_obter_vereador_nao_encontrado():
    """Testa obtenção de vereador inexistente"""
    response = client.get("/api/v1/vereadores/999")
    assert response.status_code == 404


def test_ranking_presenca():
    """Testa obtenção de ranking de presença"""
    response = client.get("/api/v1/vereadores/ranking/presenca")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data


def test_ranking_produtividade():
    """Testa obtenção de ranking de produtividade"""
    response = client.get("/api/v1/vereadores/ranking/produtividade")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data

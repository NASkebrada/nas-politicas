# 📚 Documentação da API - NAS POLÍTICAS

## Base URL
```
http://localhost:8000/api/v1
```

## Autenticação

Todos os endpoints (exceto `GET /health` e `POST /auth/login`) requerem autenticação via JWT.

### Login
```http
POST /auth/login
Content-Type: application/json

{
  "email": "usuario@example.com",
  "senha": "password123"
}
```

**Response (200)**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 1800
}
```

### Header de Autenticação
```
Authorization: Bearer {access_token}
```

## Endpoints

### Health Check

#### GET /health
Verifica se a API está funcionando.

**Response (200)**
```json
{
  "status": "ok",
  "version": "1.0.0",
  "timestamp": "2024-06-03T10:30:00Z"
}
```

---

### Vereadores

#### GET /vereadores
Lista todos os vereadores.

**Query Parameters**
- `skip`: Número de registros a pular (padrão: 0)
- `limit`: Número de registros a retornar (padrão: 10, máximo: 100)
- `partido`: Filtrar por partido (opcional)

**Response (200)**
```json
{
  "total": 25,
  "items": [
    {
      "id": 1,
      "nome": "João Silva",
      "partido": "PT",
      "contato": "(67) 3232-1234",
      "redes_sociais": {
        "facebook": "joao.silva",
        "instagram": "@joaosilva",
        "email": "joao@example.com"
      },
      "historico_politico": "Vereador desde 2021...",
      "foto_url": "https://...",
      "presenca_sessoes": 35,
      "total_sessoes": 40,
      "projetos_apresentados": 5,
      "projetos_aprovados": 3,
      "indicacoes": 12,
      "requerimentos": 8,
      "created_at": "2024-01-01T00:00:00Z",
      "updated_at": "2024-06-03T00:00:00Z"
    }
  ]
}
```

#### GET /vereadores/{id}
Obtém detalhes de um vereador específico.

**Response (200)**
```json
{
  "id": 1,
  "nome": "João Silva",
  "partido": "PT",
  "contato": "(67) 3232-1234",
  "redes_sociais": {
    "facebook": "joao.silva",
    "instagram": "@joaosilva",
    "email": "joao@example.com"
  },
  "historico_politico": "Vereador desde 2021...",
  "foto_url": "https://...",
  "presenca_sessoes": 35,
  "total_sessoes": 40,
  "projetos_apresentados": 5,
  "projetos_aprovados": 3,
  "indicacoes": 12,
  "requerimentos": 8,
  "historico_votacoes": [
    {
      "projeto_id": 1,
      "projeto_numero": "PL 001/2024",
      "projeto_titulo": "Autoriza compra de equipamentos",
      "voto": "favoravel",
      "data_votacao": "2024-05-15"
    }
  ],
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-06-03T00:00:00Z"
}
```

---

### Projetos de Lei

#### GET /projetos
Lista todos os projetos de lei.

**Query Parameters**
- `skip`: Número de registros a pular (padrão: 0)
- `limit`: Número de registros a retornar (padrão: 10)
- `status`: Filtrar por status (em_tramitacao, aprovado, vetado, arquivado)
- `busca`: Buscar por título ou número

**Response (200)**
```json
{
  "total": 42,
  "items": [
    {
      "id": 1,
      "numero": "PL 001/2024",
      "titulo": "Autoriza a compra de equipamentos para as unidades de saúde",
      "descricao": "Este projeto autoriza a compra de novos equipamentos...",
      "status": "em_tramitacao",
      "data_protocolamento": "2024-03-15",
      "data_aprovacao": null,
      "data_veto": null,
      "autor": "Vereador João Silva",
      "explicacao_ia": "Este projeto autoriza a compra de novos equipamentos para as unidades de saúde do município.",
      "votos": {
        "favoraveis": 18,
        "contra": 5,
        "abstencoes": 2,
        "ausentes": 0
      },
      "created_at": "2024-03-15T00:00:00Z",
      "updated_at": "2024-06-03T00:00:00Z"
    }
  ]
}
```

#### GET /projetos/{id}
Obtém detalhes de um projeto específico.

**Response (200)**
```json
{
  "id": 1,
  "numero": "PL 001/2024",
  "titulo": "Autoriza a compra de equipamentos para as unidades de saúde",
  "descricao": "Este projeto autoriza a compra de novos equipamentos...",
  "status": "em_tramitacao",
  "data_protocolamento": "2024-03-15",
  "data_aprovacao": null,
  "data_veto": null,
  "autor": "Vereador João Silva",
  "explicacao_ia": "Este projeto autoriza a compra de novos equipamentos para as unidades de saúde do município.",
  "votos": {
    "favoraveis": 18,
    "contra": 5,
    "abstencoes": 2,
    "ausentes": 0
  },
  "votacoes_por_vereador": [
    {
      "vereador_id": 1,
      "vereador_nome": "João Silva",
      "voto": "favoravel",
      "data_votacao": "2024-05-15T14:30:00Z"
    }
  ],
  "created_at": "2024-03-15T00:00:00Z",
  "updated_at": "2024-06-03T00:00:00Z"
}
```

---

### Votações

#### GET /votacoes
Lista todas as votações.

**Query Parameters**
- `skip`: Número de registros a pular (padrão: 0)
- `limit`: Número de registros a retornar (padrão: 10)
- `projeto_id`: Filtrar por projeto
- `vereador_id`: Filtrar por vereador
- `voto`: Filtrar por voto (favoravel, contra, abstencao, ausente)

**Response (200)**
```json
{
  "total": 1250,
  "items": [
    {
      "id": 1,
      "projeto": {
        "id": 1,
        "numero": "PL 001/2024",
        "titulo": "Autoriza a compra de equipamentos"
      },
      "vereador": {
        "id": 1,
        "nome": "João Silva",
        "partido": "PT"
      },
      "voto": "favoravel",
      "data_votacao": "2024-05-15T14:30:00Z"
    }
  ]
}
```

#### GET /votacoes/projeto/{projeto_id}
Obtém todas as votações de um projeto específico.

**Response (200)**
```json
{
  "projeto_numero": "PL 001/2024",
  "projeto_titulo": "Autoriza a compra de equipamentos",
  "resultado": {
    "favoraveis": 18,
    "contra": 5,
    "abstencoes": 2,
    "ausentes": 0
  },
  "votacoes": [
    {
      "vereador_id": 1,
      "vereador_nome": "João Silva",
      "partido": "PT",
      "voto": "favoravel"
    }
  ]
}
```

---

### Despesas

#### GET /despesas
Lista todas as despesas da prefeitura.

**Query Parameters**
- `skip`: Número de registros a pular (padrão: 0)
- `limit`: Número de registros a retornar (padrão: 10)
- `categoria`: Filtrar por categoria
- `data_inicio`: Data inicial (YYYY-MM-DD)
- `data_fim`: Data final (YYYY-MM-DD)
- `valor_minimo`: Valor mínimo
- `valor_maximo`: Valor máximo

**Response (200)**
```json
{
  "total": 5420,
  "total_gasto": 25500000.50,
  "items": [
    {
      "id": 1,
      "descricao": "Combustível - Veículos oficiais",
      "valor": 15000.00,
      "categoria": "Combustíveis e lubrificantes",
      "data_despesa": "2024-06-01",
      "fornecedor": "Posto XYZ",
      "fonte_dados": "Portal da Transparência",
      "created_at": "2024-06-01T00:00:00Z"
    }
  ]
}
```

#### GET /despesas/resumo
Retorna um resumo das despesas.

**Query Parameters**
- `agrupado_por`: month, category, year

**Response (200)**
```json
{
  "periodo": "2024-06",
  "total_gasto": 2500000.00,
  "por_categoria": [
    {
      "categoria": "Saúde",
      "total": 800000.00,
      "percentual": 32
    }
  ]
}
```

---

### Receitas

#### GET /receitas
Lista todas as receitas da prefeitura.

**Response (200)**
```json
{
  "total": 342,
  "total_receita": 125600000.00,
  "items": [
    {
      "id": 1,
      "descricao": "IPTU - Imposto sobre propriedade predial",
      "valor": 2500000.00,
      "tipo": "Tributária",
      "data_receita": "2024-05-31"
    }
  ]
}
```

---

### Obras

#### GET /obras
Lista todas as obras da cidade.

**Response (200)**
```json
{
  "total": 12,
  "items": [
    {
      "id": 1,
      "titulo": "Pavimentação da Rua Principal",
      "descricao": "Pavimentação da rua principal do centro...",
      "localizacao": "Centro",
      "coordenadas": {
        "latitude": -22.1234,
        "longitude": -55.5678
      },
      "valor": 500000.00,
      "empresa_responsavel": "Construtora ABC",
      "data_inicio": "2024-03-15",
      "data_fim_prevista": "2024-09-30",
      "percentual_concluido": 45,
      "status": "em_execucao"
    }
  ]
}
```

---

### Notícias

#### GET /noticias
Lista todas as notícias.

**Response (200)**
```json
{
  "total": 342,
  "items": [
    {
      "id": 1,
      "titulo": "Prefeitura inicia obras de pavimentação",
      "resumo": "A prefeitura iniciou ontem as obras de pavimentação...",
      "conteudo": "A prefeitura iniciou ontem as obras de pavimentação da rua principal...",
      "fonte": "prefeitura",
      "url": "https://...",
      "data_publicacao": "2024-06-03T10:30:00Z"
    }
  ]
}
```

---

### Licitações

#### GET /licitacoes
Lista todas as licitações.

**Response (200)**
```json
{
  "total": 8,
  "items": [
    {
      "id": 1,
      "numero": "LIC 001/2024",
      "descricao": "Fornecimento de material de expediente",
      "status": "aberta",
      "data_abertura": "2024-06-01",
      "data_encerramento": "2024-06-30",
      "valor_estimado": 50000.00
    }
  ]
}
```

---

### IA Cidadã

#### POST /ia/pergunte
Faz uma pergunta à IA Cidadã.

**Request**
```json
{
  "pergunta": "Quanto a prefeitura gastou com combustível este mês?"
}
```

**Response (200)**
```json
{
  "pergunta": "Quanto a prefeitura gastou com combustível este mês?",
  "resposta": "De acordo com os dados do Portal da Transparência, a prefeitura gastou R$ 45.000,00 com combustível e lubrificantes em junho de 2024.",
  "fontes": [
    {
      "tipo": "despesa",
      "id": 123,
      "descricao": "Combustível - Veículos oficiais",
      "valor": 45000.00
    }
  ],
  "timestamp": "2024-06-03T10:30:00Z"
}
```

---

## Códigos de Status HTTP

| Código | Significado |
|--------|-------------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

---

**Última atualização**: 2024-06-03

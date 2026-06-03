# 🏗️ Arquitetura do Projeto NAS POLÍTICAS

## Visão Geral da Arquitetura

```
┌─────────────────────────────────────────────────────────────────┐
│                      FRONTEND (Flutter)                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐   │
│  │   Mobile    │  │     Web      │  │   Responsivo Design  │   │
│  │  (Android)  │  │  (Browser)   │  │                      │   │
│  └──────────────┘  └──────────────┘  └──────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              ↓ HTTP/REST
┌─────────────────────────────────────────────────────────────────┐
│                    BACKEND (FastAPI)                             │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              API REST com Autenticação                    │   │
│  │  • /api/v1/vereadores                                    │   │
│  │  • /api/v1/projetos                                      │   │
│  │  • /api/v1/votacoes                                      │   │
│  │  • /api/v1/despesas                                      │   │
│  │  • /api/v1/obras                                         │   │
│  │  • /api/v1/noticias                                      │   │
│  │  • /api/v1/licitacoes                                    │   │
│  │  • /api/v1/ia/pergunte                                   │   │
│  └──────────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │         Camada de Lógica de Negócio (Services)           │   │
│  │  • VereadorService                                        │   │
│  │  • ProjetoService                                         │   │
│  │  • VotacaoService                                         │   │
│  │  • TransparenciaService                                   │   │
│  │  • ObraService                                            │   │
│  │  • NotificacaoService                                     │   │
│  └──────────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │         Scrapers (Coleta de Dados)                        │   │
│  │  • CamaraScraperService                                   │   │
│  │  • PrefeituraScraperService                               │   │
│  │  • TransparenciaScraperService                            │   │
│  │  • (Executados em jobs agendados)                         │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              ↓ SQL
┌─────────────────────────────────────────────────────────────────┐
│                    BANCO DE DADOS (PostgreSQL)                   │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  Tabelas Principais:                                     │    │
│  │  • vereadores                                           │    │
│  │  • projetos_lei                                         │    │
│  │  • votacoes                                             │    │
│  │  • despesas                                             │    │
│  │  • receitas                                             │    │
│  │  • obras                                                │    │
│  │  • licitacoes                                           │    │
│  │  • noticiarios                                          │    │
│  │  • usuarios                                             │    │
│  │  • notificacoes                                         │    │
│  │  • historico_dados                                      │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

## Componentes Principais

### 1. Frontend (Flutter)

#### Camadas
- **Presentation Layer**: Telas, Widgets, Controllers
- **Business Logic Layer (BLoC/Riverpod)**: Gerenciamento de estado
- **Data Layer**: Repositórios, APIs, Cache local

#### Estrutura de Pastas
```
lib/
├── main.dart
├── config/
│   ├── theme.dart              # Tema verde e amarelo
│   ├── routes.dart             # Rotas da aplicação
│   └── constants.dart          # Constantes
├── models/
│   ├── vereador.dart
│   ├── projeto_lei.dart
│   ├── votacao.dart
│   ├── despesa.dart
│   ├── obra.dart
│   ├── noticia.dart
│   └── licitacao.dart
├── screens/
│   ├── home_screen.dart        # Tela inicial
│   ├── politico_screen.dart    # Perfil do vereador
│   ├── votacoes_screen.dart    # Como votou?
│   ├── projetos_screen.dart    # Projetos de lei
│   ├── despesas_screen.dart    # Dinheiro público
│   ├── obras_screen.dart       # Obras da cidade
│   ├── observatorio_screen.dart # Observatório do mandato
│   └── ia_screen.dart          # IA Cidadã
├── widgets/
│   ├── projeto_card.dart
│   ├── vereador_card.dart
│   ├── obra_map.dart
│   ├── despesa_chart.dart
│   └── notificacao_banner.dart
├── services/
│   ├── api_service.dart        # Cliente HTTP
│   ├── cache_service.dart      # Cache local
│   └── notification_service.dart
└── providers/                  # Riverpod providers
    ├── vereador_provider.dart
    ├── projeto_provider.dart
    ├── votacao_provider.dart
    └── etc...
```

### 2. Backend (FastAPI)

#### Camadas

```
app/
├── main.py                     # Entrypoint da API
├── config.py                   # Configurações
├── models/                     # ORM SQLAlchemy
│   ├── vereador.py
│   ├── projeto_lei.py
│   ├── votacao.py
│   ├── despesa.py
│   ├── obra.py
│   ├── noticia.py
│   └── etc...
├── schemas/                    # Pydantic schemas (request/response)
│   ├── vereador_schema.py
│   ├── projeto_schema.py
│   └── etc...
├── routes/                     # Endpoints da API
│   ├── vereadores.py
│   ├── projetos.py
│   ├── votacoes.py
│   ├── despesas.py
│   ├── obras.py
│   ├── noticias.py
│   ├── licitacoes.py
│   ├── ia.py
│   └── health.py
├── services/                   # Lógica de negócio
│   ├── vereador_service.py
│   ├── projeto_service.py
│   ├── votacao_service.py
│   ├── transparencia_service.py
│   ├── obra_service.py
│   └── notificacao_service.py
├── scrapers/                   # Coleta de dados
│   ├── camara_scraper.py       # Portal da Câmara
│   ├── prefeitura_scraper.py   # Prefeitura
│   ├── transparencia_scraper.py # Portal da Transparência
│   └── scraper_base.py
├── jobs/                       # Tarefas agendadas
│   ├── sync_jobs.py            # Atualizar dados periodicamente
│   └── notification_jobs.py
├── database/
│   ├── database.py             # Conexão com PostgreSQL
│   └── migrations/             # Alembic migrations
├── auth/
│   ├── auth.py                 # JWT, OAuth, etc
│   └── permissions.py
└── utils/
    ├── logger.py
    ├── validators.py
    └── helpers.py
```

#### Stack Tecnológico Backend
- **FastAPI**: Framework web
- **SQLAlchemy**: ORM para database
- **Pydantic**: Validação de dados
- **APScheduler**: Agendamento de tarefas
- **Beautiful Soup / Scrapy**: Web scraping
- **OpenAI API**: Processamento de linguagem natural (IA Cidadã)
- **JWT**: Autenticação

### 3. Banco de Dados (PostgreSQL)

#### Principais Entidades

```sql
-- Vereadores
CREATE TABLE vereadores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    partido VARCHAR(100),
    contato VARCHAR(255),
    redes_sociais JSONB,
    historico_politico TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- Projetos de Lei
CREATE TABLE projetos_lei (
    id SERIAL PRIMARY KEY,
    numero VARCHAR(50) UNIQUE,
    titulo VARCHAR(500),
    descricao TEXT,
    status VARCHAR(50),
    data_protocolamento DATE,
    data_aprovacao DATE,
    explicacao_ia TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- Votações
CREATE TABLE votacoes (
    id SERIAL PRIMARY KEY,
    projeto_lei_id INTEGER REFERENCES projetos_lei,
    vereador_id INTEGER REFERENCES vereadores,
    voto VARCHAR(50),
    data_votacao DATE,
    created_at TIMESTAMP
);

-- Despesas
CREATE TABLE despesas (
    id SERIAL PRIMARY KEY,
    descricao VARCHAR(500),
    valor DECIMAL(12, 2),
    categoria VARCHAR(100),
    data_despesa DATE,
    origem_dados VARCHAR(100),
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- Obras
CREATE TABLE obras (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255),
    descricao TEXT,
    localizacao VARCHAR(255),
    latitude DECIMAL(9, 6),
    longitude DECIMAL(9, 6),
    valor DECIMAL(12, 2),
    empresa_responsavel VARCHAR(255),
    data_inicio DATE,
    data_fim_prevista DATE,
    percentual_concluido INT,
    fotos JSONB,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- Notícias
CREATE TABLE noticias (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(500),
    conteudo TEXT,
    fonte VARCHAR(100),
    url VARCHAR(500),
    data_publicacao TIMESTAMP,
    created_at TIMESTAMP
);

-- Licitações
CREATE TABLE licitacoes (
    id SERIAL PRIMARY KEY,
    numero VARCHAR(50),
    descricao TEXT,
    status VARCHAR(50),
    data_abertura DATE,
    data_encerramento DATE,
    valor_estimado DECIMAL(12, 2),
    created_at TIMESTAMP
);

-- Usuários
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    senha_hash VARCHAR(255),
    nome VARCHAR(255),
    preferencias JSONB,
    created_at TIMESTAMP
);

-- Notificações
CREATE TABLE notificacoes (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios,
    tipo VARCHAR(100),
    titulo VARCHAR(255),
    mensagem TEXT,
    lida BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP
);
```

## Fluxo de Dados

### 1. Coleta de Dados (Scrapers)
```
Portais Oficiais
    ↓
Scrapers (jobs agendados a cada 6 horas)
    ↓
Processamento e normalização
    ↓
PostgreSQL
```

### 2. Consulta de Dados (API)
```
Frontend (Flutter)
    ↓
Request HTTP para API
    ↓
FastAPI Route Handler
    ↓
Service (lógica de negócio)
    ↓
SQLAlchemy Query
    ↓
PostgreSQL
    ↓
JSON Response
```

### 3. IA Cidadã
```
Pergunta do usuário
    ↓
Processamento de linguagem natural (OpenAI)
    ↓
Geração de SQL/Query
    ↓
Busca no banco de dados
    ↓
Formatação da resposta em linguagem simples
    ↓
Resposta ao usuário
```

## Segurança

### Autenticação
- JWT com refresh tokens
- OAuth 2.0 (opcional: Google, GitHub)

### Autorização
- Role-based access control (RBAC)
- Usuários anônimos podem ver dados públicos
- Usuários autenticados podem salvar favoritos e preferências

### Proteção de Dados
- HTTPS em produção
- Sanitização de inputs
- Rate limiting
- CORS configurado

## Performance

### Caching
- Redis para cache de dados frequentemente acessados
- Cache local no Flutter com Hive
- Cache HTTP com headers apropriados

### Otimizações
- Paginação em listagens
- Índices no banco de dados
- Queries otimizadas
- Lazy loading no frontend

## Deployment

### Frontend
- Build web: Flutter Web
- Build mobile: Android e iOS
- Distribuição via stores (Play Store, App Store)

### Backend
- Docker container
- Deployment em cloud (AWS, DigitalOcean, Heroku, etc)
- PostgreSQL em managed database
- CI/CD com GitHub Actions

## Escalabilidade

- Microserviços para scrapers (separados da API principal)
- Message queue (Celery) para tarefas assíncronas
- Load balancing
- Database replication
- CDN para assets estáticos

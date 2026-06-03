# 🚀 Guia de Setup - NAS POLÍTICAS

## Pré-requisitos

### Sistema Operacional
- Windows, macOS ou Linux

### Ferramentas Necessárias

#### Para Backend
- **Python 3.11+** ([Download](https://www.python.org/downloads/))
- **PostgreSQL 14+** ([Download](https://www.postgresql.org/download/))
- **Git** ([Download](https://git-scm.com/))

#### Para Frontend
- **Flutter SDK 3.10+** ([Download](https://flutter.dev/docs/get-started/install))
- **Android Studio** (para Android emulator)
- **Xcode** (para iOS, apenas macOS)

## Setup do Backend

### 1. Clonar o repositório
```bash
git clone https://github.com/NASkebrada/nas-politicas.git
cd nas-politicas/backend
```

### 2. Criar ambiente virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente
```bash
# Copiar arquivo de exemplo
cp .env.example .env

# Editar arquivo .env com suas configurações
# Exemplo de .env:
DATABASE_URL=postgresql://user:password@localhost:5432/nas_politicas
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
OPENAI_API_KEY=your-openai-key-here
DEBUG=True
```

### 5. Criar banco de dados
```bash
# No PostgreSQL
psql -U postgres -c "CREATE DATABASE nas_politicas;"
```

### 6. Executar migrations
```bash
alembic upgrade head
```

### 7. Iniciar o servidor
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

O servidor estará disponível em: **http://localhost:8000**
Documentação da API: **http://localhost:8000/docs**

## Setup do Frontend

### 1. Verificar instalação do Flutter
```bash
flutter doctor
```

Todos os items devem ter um checkmark ✓

### 2. Clonar o repositório
```bash
git clone https://github.com/NASkebrada/nas-politicas.git
cd nas-politicas/frontend
```

### 3. Obter dependências
```bash
flutter pub get
```

### 4. Configurar API URL
Editar `lib/config/constants.dart`:
```dart
const String API_BASE_URL = 'http://localhost:8000/api/v1';
```

### 5. Executar em emulador (Android)
```bash
# Iniciar emulador do Android Studio ou
flutter emulators --launch Pixel_4_API_30

# Executar aplicativo
flutter run
```

### 6. Executar em dispositivo físico
```bash
# Conectar dispositivo via USB e ativar debug
flutter devices

# Executar
flutter run
```

### 7. Executar como web
```bash
flutter run -d chrome
```

## Estrutura de Pastas

```
nas-politicas/
├── backend/
│   ├── app/
│   ├── tests/
│   ├── requirements.txt
│   ├── .env.example
│   └── main.py
├── frontend/
│   ├── lib/
│   ├── assets/
│   ├── pubspec.yaml
│   └── test/
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API.md
│   └── SETUP.md
└── README.md
```

## Verificar Instalação

### Backend
```bash
cd backend
python -m pytest tests/
```

### Frontend
```bash
cd frontend
flutter test
```

## Desenvolvimento

### Hot Reload (Frontend)
Durante o desenvolvimento, Flutter suporta hot reload:
```
Pressione 'r' para hot reload
Pressione 'R' para hot restart
Pressione 'q' para sair
```

### Hot Reload (Backend)
FastAPI com `--reload` já suporta auto-reload quando você edita os arquivos.

## Variáveis de Ambiente

### Backend (.env)
```
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/nas_politicas

# JWT
SECRET_KEY=your-super-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# IA (OpenAI)
OPENAI_API_KEY=sk-...

# Scrapers
SCRAPER_INTERVAL_HOURS=6

# Email (para notificações)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-password

# Debug
DEBUG=False
LOG_LEVEL=INFO
```

### Frontend (constants.dart)
```dart
const String API_BASE_URL = 'https://api.nas-politicas.com/api/v1';
const String TIMEOUT_SECONDS = 30;
const bool DEBUG_MODE = false;
```

## Docker (Opcional)

### Build da imagem
```bash
docker build -t nas-politicas-backend .
```

### Executar container
```bash
docker run -p 8000:8000 \
  -e DATABASE_URL=postgresql://user:password@db:5432/nas_politicas \
  -e SECRET_KEY=your-secret-key \
  nas-politicas-backend
```

## Troubleshooting

### Backend
| Problema | Solução |
|----------|---------|
| Erro ao conectar PostgreSQL | Verifique DATABASE_URL em .env |
| Módulos não encontrados | Execute `pip install -r requirements.txt` |
| Porta 8000 já em uso | Use `lsof -i :8000` (Linux/Mac) ou `netstat -ano \| findstr :8000` (Windows) |

### Frontend
| Problema | Solução |
|----------|---------|
| Flutter não encontrado | Adicione Flutter bin ao PATH |
| Emulador não inicia | Execute `flutter doctor` e siga as instruções |
| API não conecta | Verifique API_BASE_URL em constants.dart |

## Próximos Passos

1. ✅ Configurar banco de dados
2. ✅ Iniciar backend
3. ✅ Iniciar frontend
4. 📖 Leia a documentação da API: [API.md](API.md)
5. 🔧 Comece a desenvolver features
6. 🧪 Escreva testes
7. 🚀 Faça deploy

## Recursos Úteis

- [Flutter Documentation](https://flutter.dev/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

## Suporte

Se tiver dúvidas, abra uma [issue](https://github.com/NASkebrada/nas-politicas/issues) no repositório.

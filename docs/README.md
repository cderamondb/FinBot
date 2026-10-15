# FinBot - Agente Financiero IA

Aplicacion de agente conversacional que ayuda a construir casos de negocio completos para productos basados en inteligencia artificial.

## Funcionalidades

- **Caso de negocio**: Recopila informacion del proyecto del cliente
- **Ficha de producto**: Genera ficha tecnica con stack, features y diferenciadores
- **Calculo de CapEx**: Gastos de capital (infraestructura, licencias, desarrollo)
- **Calculo de OpEx**: Gastos operativos (APIs, cloud, mantenimiento, soporte)
- **Roadmap**: Plan de ejecucion con fases, hitos y entregables
- **KPIs y OKRs**: Metricas de exito y objetivos medibles
- **Documento final**: Consolidacion del caso de negocio completo

## Stack tecnologico

- Python 3.12
- FastAPI + Uvicorn
- OpenAI API (GPT-4o-mini)
- HTML/CSS/JS (interfaz conversacional)

## Estructura del proyecto

```
FinBot/
├── app/
│   ├── agent.py          # Agente financiero con tool calling
│   ├── main.py           # Servidor FastAPI
│   └── static/
│       └── index.html    # Interfaz web conversacional
├── docs/
│   └── README.md
├── Dockerfile
├── Procfile
├── fly.toml
├── requirements.txt
└── .env.example
```

## Instalacion local

```bash
pip install -r requirements.txt
cp .env.example .env
# Editar .env con tu OPENAI_API_KEY
cd app
uvicorn main:app --reload --port 8000
```

Abrir http://localhost:8000

## Deploy

### Google Cloud Run
```bash
gcloud run deploy finbot --source . --set-env-vars OPENAI_API_KEY=tu-key --region us-central1 --allow-unauthenticated
```

### Heroku
```bash
heroku create finbot
heroku config:set OPENAI_API_KEY=tu-key
git push heroku main
```

### Fly.io
```bash
fly launch
fly secrets set OPENAI_API_KEY=tu-key
fly deploy
```

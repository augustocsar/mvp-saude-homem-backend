from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.router import router  # suas rotas gerais já existentes
from app.routes.reminder_routes import router as reminder_router  # rota de lembretes

app = FastAPI(
    title="MVP Saúde do Homem - CheckMen",
    description="API para aplicativo de saúde preventiva masculina",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique os domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir todas as rotas existentes
app.include_router(router)

# Incluir rotas de lembretes
app.include_router(reminder_router)

@app.get("/")
async def root():
    return {
        "message": "CheckMen API - MVP Saúde do Homem",
        "status": "online",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "CheckMen API"}

@app.get("/api/test")
async def test_endpoint():
    return {
        "message": "API funcionando!",
        "backend": "FastAPI + Oracle NoSQL"
    }

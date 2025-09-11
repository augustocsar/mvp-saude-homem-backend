from fastapi import APIRouter
from app.controllers.rss_controller import router as rss_router
from app.controllers.user_controller import router as user_router

# Router principal que agrega todos os sub-routers
router = APIRouter()

# Incluir routers
router.include_router(rss_router)
router.include_router(user_router)  # ← ADICIONAR ESTA LINHA
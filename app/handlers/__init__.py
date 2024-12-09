from aiogram import Router
from .commands import router as commands_router
from .reg import router as reg_router
from .other import router as other_router
from .task_state import router as task_router
from .aneks import router as anek_router

# Объединяем все роутеры
main_router = Router()
main_router.include_router(commands_router)
main_router.include_router(reg_router)
main_router.include_router(other_router)
main_router.include_router(task_router)
main_router.include_router(anek_router)
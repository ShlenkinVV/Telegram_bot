from aiogram import Router
from .commands import router as commands_router
from .states import router as states_router
from .other import router as other_router
from .task_state import router as task_router

# Объединяем все роутеры
main_router = Router()
main_router.include_router(commands_router)
main_router.include_router(states_router)
main_router.include_router(other_router)
main_router.include_router(task_router)
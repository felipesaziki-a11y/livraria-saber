from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.controllers import genero_controller, livro_controller, cliente_controller, estoque_controller

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # em produção, restrinja aos domínios necessários
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ... resto dos seus include_router aqui

app.include_router(genero_controller.router)
app.include_router(livro_controller.router)
app.include_router(cliente_controller.router)
app.include_router(estoque_controller.router)
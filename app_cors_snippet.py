from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # em produção, restrinja aos domínios necessários
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ... resto dos seus include_router aqui

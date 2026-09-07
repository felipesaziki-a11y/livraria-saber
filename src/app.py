from fastapi import FastAPI
from pathlib import Path
import sys

# Permite rodar com `py src/app.py`: coloca a raiz do projeto no sys.path
# para que os imports `from src import .` funcionem corretamente
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.controllers import categoria_controller


app = FastAPI(
    title="Livraria Saber",
    description="Projeto CRUD",
    version="0.1.0"
)

app.include_router(categoria_controller.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.app:app", host="127.0.0.1", port=8000, reload=True)
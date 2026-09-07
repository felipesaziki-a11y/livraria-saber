from fastapi import FastAPI
from pathlib import Path
import sys

# Permite rodar com `py src/app.py`: coloca a raiz do projeto no sys.path
# para que os imports `from src import .` funcionem corretamente
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.controllers import genero_controller, livro_controller, cliente_controller, estoque_controller


app = FastAPI(
    title="Livraria Saber",
    description="Projeto CRUD",
    version="0.1.0"
)

app.include_router(genero_controller.router)
app.include_router(livro_controller.router)
app.include_router(cliente_controller.router)
app.include_router(estoque_controller.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.app:app", host="127.0.0.1", port=8000, reload=True)
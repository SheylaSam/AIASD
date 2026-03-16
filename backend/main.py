from fastapi import FastAPI
from app.infrastructure.database import create_tables
from app.interfaces.user_router import router as user_router
from app.interfaces.document_router import router as document_router

app = FastAPI(
    title="AIASD Lernplattform API",
    description="Kollaborative Lernplattform mit KI-generierten Quizzes",
    version="0.1.0",
)


@app.on_event("startup")
def startup():
    create_tables()


app.include_router(user_router)
app.include_router(document_router)


@app.get("/")
def health_check():
    return {"status": "ok", "message": "AIASD API läuft"}

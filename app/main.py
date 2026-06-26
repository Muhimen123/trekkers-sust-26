from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Ticket Analyzer",
    description="Analyzes support tickets",
    version="0.0.1",
)

app.include_router(router)

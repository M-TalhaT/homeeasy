# app/main.py

from fastapi import FastAPI
from app.routers.rep_performance import router as rep_performance_router
from app.routers.team_performance import router as team_performance_router
from app.routers.performance_trends import router as performance_trends_router

app = FastAPI()

app.include_router(rep_performance_router)
app.include_router(team_performance_router)
app.include_router(performance_trends_router)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting EASA FSTD Compliance Manager API")
    yield
    # Shutdown
    print("Shutting down API")


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="EASA FSTD Regulation Compliance Manager for ATOs",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "message": "EASA FSTD Compliance Manager API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/api/programmes")
async def list_programmes():
    return []


@app.get("/api/fstds")
async def list_fstds():
    return []

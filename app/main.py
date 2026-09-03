from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.routers.health import router as health_router
from app.routers.qna import router as qna_router

settings = get_settings()

app = FastAPI(
    title=settings.service_name,
    description="A minimal FastAPI service for restaurant stock-inventory QnA",
    version=settings.app_version,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": 200, "message": "ok"}


app.include_router(health_router)
app.include_router(qna_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import APIRouter, Depends

from app.dependencies import SettingsDependency
from app.schemas import HealthResponse

router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Health check",
    tags=["health"],
)
async def health_check(settings: SettingsDependency) -> HealthResponse:
    return HealthResponse(
        status="ok",
        version=settings.app_version,
        environment=settings.environment,
        service_name=settings.service_name,
    )

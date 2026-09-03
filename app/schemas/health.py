from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = Field(..., description="Overall health status", examples=["ok"])
    version: str = Field(..., description="Application version", examples=["0.1.0"])
    environment: str = Field(
        ..., description="Deployment environment", examples=["development"]
    )
    service_name: str = Field(..., description="Service identifier")

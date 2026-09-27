"""Application entry point for the CloudCost AI API."""

from fastapi import FastAPI

from cloudcost_ai.api.routes.health import router as health_router

app = FastAPI(
    title="CloudCost AI API",
    description="Backend foundation for the CloudCost AI platform.",
    version="0.1.0",
)

app.include_router(health_router)

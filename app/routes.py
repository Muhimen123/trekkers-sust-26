from fastapi import APIRouter
from app.models import (
    TicketRequest,
    TicketResponse,
    EvidenceVerdict,
    CaseType,
    Severity,
    Department
)
from app.services import test_ai_connection, analyze_ticket_service

router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.get("/test-ai")
async def test_ai():
    result = test_ai_connection()
    return {"message": "AI test complete.", "ai_response": result}


@router.post("/analyze-ticket", response_model=TicketResponse)
async def analyze_ticket(request: TicketRequest):
    return analyze_ticket_service(request)

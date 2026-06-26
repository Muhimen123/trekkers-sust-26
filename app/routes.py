from fastapi import APIRouter
from app.models import (
    TicketRequest,
    TicketResponse,
    EvidenceVerdict,
    CaseType,
    Severity,
    Department
)

router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.post("/analyze-ticket", response_model=TicketResponse)
async def analyze_ticket(request: TicketRequest):
    return TicketResponse(
        ticket_id=request.ticket_id,
        evidence_verdict=EvidenceVerdict.insufficient_data,
        case_type=CaseType.other,
        severity=Severity.low,
        department=Department.customer_support,
        agent_summary="Placeholder summary",
        recommended_next_action="Review",
        customer_reply="Placeholder reply",
        human_review_required=False
    )

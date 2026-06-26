from pydantic import BaseModel
from typing import Optional
from app.enums import * 


class TransactionHistory(BaseModel):
    transaction_id: str
    timestamp: str                  # ISO 8601
    type: TransactionType
    amount: float                   # BDT
    counterparty: str
    status: TransactionStatus


class TicketRequest(BaseModel):
    ticket_id: str
    complaint: str
    language: Optional[Language] = None
    channel: Optional[Channel] = None
    user_type: Optional[UserType] = None
    campaign_context: Optional[str] = None
    transaction_history: Optional[list[TransactionHistory]] = []
    metadata: Optional[dict] = None


class TicketResponse(BaseModel):
    ticket_id: str
    relevant_transaction_id: Optional[str] = None
    evidence_verdict: EvidenceVerdict
    case_type: CaseType
    severity: Severity
    department: Department
    agent_summary: str
    recommended_next_action: str
    customer_reply: str
    human_review_required: bool
    confidence: Optional[float] = None
    reason_codes: Optional[list[str]] = []

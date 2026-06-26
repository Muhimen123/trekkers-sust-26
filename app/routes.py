from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.post("/analyze-ticket")
async def analyze_ticket():
    return {"message": "analyze-ticket endpoint is working"}



## Setup

### Prerequisites

* Python 3.10+
* Git

## Repository

GitHub Repository: https://github.com/Muhimen123/trekkers-sust-26

## Clone the Repository

```bash
git clone https://github.com/Muhimen123/trekkers-sust-26.git
cd trekkers-sust-26
```


### Create and Activate a Virtual Environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

The following sections will be included below:

### Sample Request
```json 
{
    "ticket_id": "TKT-12345",
    "complaint": "I transferred money to the wrong agent.",
    "language": "en",
    "channel": "in_app_chat",
    "user_type": "customer",
    "campaign_context": "referral_promo_2026",
    "transaction_history": [
    {
        "transaction_id": "TXN-98765",
        "timestamp": "2026-06-26T10:00:00Z",
        "type": "transfer",
        "amount": 500.0,
        "counterparty": "agent_007",
        "status": "completed"
    }
    ],
    "metadata": {
    "device": "android",
    "ip_address": "192.168.1.1"
    }
}
```

### Sample Response
```json 
{
  "ticket_id": "TKT-12345",
  "relevant_transaction_id": null,
  "evidence_verdict": "insufficient_data",
  "case_type": "other",
  "severity": "low",
  "department": "customer_support",
  "agent_summary": "Placeholder summary",
  "recommended_next_action": "Review",
  "customer_reply": "Placeholder reply",
  "human_review_required": false,
  "confidence": null,
  "reason_codes": []
}
```

* AI / Model Usage
* Safety Logic
* Limitations

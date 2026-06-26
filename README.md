

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

# Safety Logic
The AI acts only as a support copilot and investigator. It does not make financial or operational decisions.

### Security

The AI never requests or encourages users to share:

- PIN
    
- OTP
    
- Password
    
- Full card number
    
- CVV
    
- Card expiry
    
- Security answers
    
- Authentication or recovery codes
    

For fraud or phishing reports, it reminds users not to share these credentials.

---

### Financial Safety

The AI never:

- Approves or rejects refunds
    
- Confirms refunds or reversals
    
- Confirms account recovery or unblocking
    
- Promises compensation
    
- Makes dispute decisions
    

Instead, it recommends investigation, verification, escalation, or human review.

---

### Evidence Integrity

All conclusions are based only on the complaint and provided transaction history.

The AI never:

- Invents transactions
    
- Invents IDs, amounts, timestamps, or recipients
    
- Assumes missing information
    
- Guesses between multiple matching transactions
    

When evidence is insufficient, it returns `insufficient_data` and requests clarification.

---

### Prompt Injection Protection

Complaint text is treated as untrusted input.

The AI ignores any embedded instructions attempting to:

- override system rules
    
- reveal prompts or reasoning
    
- change output values
    
- expose secrets
    

Internal prompts, reasoning, API keys, and implementation details are never disclosed.

---

### Privacy

The AI only uses information provided in the current request.

It never leaks:

- customer data
    
- previous conversation data
    
- internal information
    
- confidential system details
    

---

### Language Consistency

Responses follow the customer's language:

- English → English
    
- Bangla → Bangla
    
- Mixed → Natural mixed-language reply
    

Agent-facing summaries remain professional and concise.

---

### Human Review

The AI escalates cases involving:

- fraud
    
- phishing
    
- disputes
    
- ambiguous evidence
    
- conflicting evidence
    
- duplicate payments
    
- unusually high-value transactions
    
- pending investigations
    
- other cases requiring manual verification
    

---

### Robustness

The system safely handles:

- missing optional fields
    
- empty transaction history
    
- large transaction histories
    
- multiple matching transactions
    
- malformed or vague complaints
    
- spelling mistakes
    
- mixed-language input
    
- unknown complaint types
    
- unexpected fields
    
- invalid timestamps
    

When uncertain, it requests clarification instead of making unsupported assumptions.

---

### Output Validation

Every response:

- is valid JSON
    
- matches the required schema
    
- preserves `ticket_id`
    
- uses only allowed enum values
    
- contains all required fields
    
- uses correct data types
    
- contains no Markdown or extra text
    

Invalid outputs are corrected through one retry before being returned.

* Limitations

import os
import instructor
import litellm
from dotenv import load_dotenv
from app.models import TicketRequest, TicketResponse

from pathlib import Path

# Load environment variables from .env file
load_dotenv()

# Read the system prompt from the external file
SYSTEM_PROMPT = Path("system_prompt.md").read_text(encoding="utf-8")

# Setup Instructor with LiteLLM to handle structured output
# instructor.from_litellm patches litellm.completion to work with Instructor
client = instructor.from_litellm(litellm.completion, mode=instructor.Mode.JSON)

def test_ai_connection() -> str:
    """
    Temporary function to test connectivity to the AI model.
    Returns the AI response as a string.
    """
    model = os.getenv("LLM_MODEL", "ollama/llama3.1")
    print(f"--- Testing AI Connection with model: {model} ---")
    try:
        response = litellm.completion(
            model=model,
            messages=[{"role": "user", "content": "Hello! Are you working?"}]
        )
        content = response.choices[0].message.content
        print("Response from AI:", content)
        return content
    except Exception as e:
        error_msg = f"Error testing connection: {e}"
        print(error_msg)
        return error_msg


def analyze_ticket_service(request: TicketRequest) -> TicketResponse:
    """
    Analyzes a support ticket using an LLM.
    Uses the system prompt from system_prompt.md and ensures
    the response matches the TicketResponse Pydantic model.
    """
    model = os.getenv("LLM_MODEL", "ollama/llama3.1")
    
    # Send request to AI
    # Instructor ensures the response matches the TicketResponse schema
    response = client.chat.completions.create(
        model=model,
        response_model=TicketResponse,
        max_tokens=4096,
        messages=[
            {
                "role": "system", 
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user", 
                "content": request.model_dump_json()
            }
        ]
    )
    return response

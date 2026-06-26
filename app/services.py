import os
import instructor
import litellm
from dotenv import load_dotenv
from app.models import TicketRequest, TicketResponse

# Load environment variables from .env file
load_dotenv()

# Setup Instructor with LiteLLM to handle structured output
# instructor.from_litellm patches litellm.completion to work with Instructor
client = instructor.from_litellm(litellm.completion)

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
    The LLM is prompted to return a response matching the TicketResponse Pydantic model.
    """
    model = os.getenv("LLM_MODEL", "ollama/llama3.1")
    
    response = client.chat.completions.create(
        model=model,
        response_model=TicketResponse,
        messages=[
            {
                "role": "system", 
                "content": "You are an expert ticket analyzer. Analyze the provided ticket data and return a JSON object that strictly adheres to the TicketResponse schema."
            },
            {
                "role": "user", 
                "content": f"Analyze this ticket: {request.model_dump_json()}"
            }
        ]
    )
    return response

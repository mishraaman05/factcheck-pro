from google import genai
from google.genai import types
from pydantic import BaseModel, Field

# Structural schema used to enforce structured output generation
class ClaimValidationSchema(BaseModel):
    status: str = Field(description="Strict categorical assignment. Must be exactly one of these three strings: 'Verified', 'Inaccurate', or 'False'. Do not use any other words.")
    confidence_score: int = Field(description="Integer certainty evaluation metric from 0 to 100.")
    corrected_fact: str = Field(description="Precise corrective truth declaration statement. If status is Verified, mirror original claim accurately.")
    explanation: str = Field(description="Detailed contextual breakdown tracking factual reasoning proofs and public consensus markers.")

def process_live_verification(claim: str, api_key: str) -> dict:
    """
    Establishes verified link parameters using the Gemini API 
    and enforces Pydantic schemas to secure accurate evaluation objects.
    """
    try:
        client = genai.Client(api_key=api_key)
        
        # Is prompt ko humne aur zyada strict aur clear kar diya hai
        system_instruction = (
            "You are an expert fact-checking intelligence engine. Your absolute duty is to categorize claims with high precision.\n"
            "Follow these rules strictly:\n"
            "1. If a claim is scientifically, historically, or factually 100% correct, you MUST classify it as 'Verified'. Do not mark it as Inaccurate.\n"
            "2. If a claim contains outdated metrics, slight errors, or partially wrong numbers, classify it as 'Inaccurate'.\n"
            "3. If a claim is completely false, a myth, or scientifically impossible, classify it as 'False'.\n\n"
            "Be decisive. Do not default to 'Inaccurate' if the statement is clearly 'Verified' or 'False'."
        )

        response = client.models.generate_content(
            model='gemini-2.5-flash',  # Model updated to 2.5 for highly accurate reasoning
            contents=f"Perform strict audit validation on the following statement entry: \"{claim}\"",
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                response_mime_type="application/json",
                response_schema=ClaimValidationSchema,
                temperature=0.0,  # Zero temperature handles maximum predictability and logic
            ),
        )
        
        import json
        structured_data = json.loads(response.text)
        return {
            "success": True,
            "status": structured_data.get("status", "Inaccurate"),
            "confidence_score": structured_data.get("confidence_score", 50),
            "corrected_fact": structured_data.get("corrected_fact", "N/A"),
            "explanation": structured_data.get("explanation", "Factual profile evaluation error encountered.")
        }
        
    except Exception as e:
        return {
            "success": False,
            "status": "Inaccurate",
            "confidence_score": 0,
            "corrected_fact": f"Processing fault encountered: {str(e)}",
            "explanation": "Critical system connection execution failure or invalid API credential structure."
        }
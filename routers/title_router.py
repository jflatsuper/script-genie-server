import os
from fastapi import APIRouter, HTTPException
from google.generativeai.types import GenerateContentResponse
from models import ScriptRequestDTO, ScriptResponseDTO
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()


title_router = APIRouter(prefix="/title", tags=["title"])
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
print(GEMINI_API_KEY)


@title_router.post("/generate-intro")
async def generate_intro(request: ScriptRequestDTO):
    genai.configure(api_key=GEMINI_API_KEY)
    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction="You are a helpful assistant."
        )
        response: GenerateContentResponse = model.generate_content(
            f'Write a catchy YouTube intro for this script: "{request.script}"'
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, detail="Failed to generate intro") from e

    return ScriptResponseDTO(
        data={"intro": response.text},
        status="success",
        message="Intro generated successfully"
    )

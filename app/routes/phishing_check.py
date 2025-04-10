from fastapi import APIRouter, UploadFile, File
from app.services.phishing_detection import analyze_email_header

router = APIRouter()

@router.post("/")
async def check_phishing(file: UploadFile = File(...)):
    headers = await file.read()
    result = analyze_email_header(headers.decode())
    return {"phishing_analysis": result}

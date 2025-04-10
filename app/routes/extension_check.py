from fastapi import APIRouter, UploadFile, File
from app.services.extension_analyzer import analyze_extension

router = APIRouter()

@router.post("/")
async def check_extension(file: UploadFile = File(...)):
    contents = await file.read()
    result = analyze_extension(contents)
    return {"extension_analysis": result}

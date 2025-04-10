from fastapi import APIRouter, UploadFile, File
from app.services.static_analysis import analyze_code

router = APIRouter()

@router.post("/")
async def scan_static(file: UploadFile = File(...)):
    code = await file.read()
    result = analyze_code(code.decode())
    return {"results": result}

from fastapi import APIRouter, UploadFile, File
from app.services.vulnerability_scanner import scan_requirements

router = APIRouter()

@router.post("/")
async def check_vulnerabilities(file: UploadFile = File(...)):
    reqs = await file.read()
    result = scan_requirements(reqs.decode())
    return {"vulnerabilities": result}

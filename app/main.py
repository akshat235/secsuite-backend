from fastapi import FastAPI
from app.routes import static_scan, phishing_check, vuln_scan, extension_check

app = FastAPI(title="SecSuite API")

app.include_router(static_scan.router, prefix="/static")
app.include_router(phishing_check.router, prefix="/phishing")
app.include_router(vuln_scan.router, prefix="/vulnerability")
app.include_router(extension_check.router, prefix="/extension")

@app.get("/")
def root():
    return {"message": "Welcome to SecSuite API"}

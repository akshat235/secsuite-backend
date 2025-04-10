import zipfile
import json
import io

SUSPICIOUS_PERMISSIONS = [
    "webRequest", "tabs", "clipboardWrite", "downloads", "webNavigation"
]

def analyze_extension(data: bytes):
    try:
        z = zipfile.ZipFile(io.BytesIO(data))
        manifest_data = z.read("manifest.json").decode("utf-8")
        manifest = json.loads(manifest_data)

        permissions = manifest.get("permissions", [])
        risky_perms = [p for p in permissions if p in SUSPICIOUS_PERMISSIONS]

        score = len(risky_perms)
        result = {
            "permissions": permissions,
            "risky_permissions": risky_perms,
            "risk_level": "high" if score >= 3 else "medium" if score else "low"
        }
        return result
    except Exception as e:
        return {"error": str(e)}

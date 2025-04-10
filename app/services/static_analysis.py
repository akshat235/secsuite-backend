import tempfile
import subprocess
import json

def analyze_code(code: str):
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode='w') as tmp:
        tmp.write(code)
        tmp.flush()
        tmp_path = tmp.name

    # Run Bandit on the temporary file
    result = subprocess.run(
        ["bandit", "-f", "json", tmp_path],
        capture_output=True,
        text=True
    )

    try:
        output = json.loads(result.stdout)
        issues = [
            {
                "line_number": issue["line_number"],
                "issue": issue["issue_text"],
                "severity": issue["issue_severity"],
                "confidence": issue["issue_confidence"],
                "code": issue["code"]
            }
            for issue in output.get("results", [])
        ]
        return issues
    except Exception as e:
        return [{"error": str(e)}]

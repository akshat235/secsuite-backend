import re

def analyze_email_header(headers: str):
    score = 0
    flags = []

    if "Reply-To" in headers and "From" in headers:
        from_match = re.search(r"From:.*?<(.+?)>", headers)
        reply_match = re.search(r"Reply-To:.*?<(.+?)>", headers)
        if from_match and reply_match:
            from_email = from_match.group(1).split("@")[-1]
            reply_email = reply_match.group(1).split("@")[-1]
            if from_email != reply_email:
                score += 1
                flags.append("From and Reply-To domains mismatch")

    if "Return-Path:" in headers and "Received:" not in headers:
        score += 1
        flags.append("Missing received path")

    result = {
        "phishing": score > 0,
        "risk_score": score,
        "flags": flags
    }
    return result

import os
import subprocess
import pickle
import jwt

# Insecure: hardcoded secret key
SECRET_KEY = "my_very_secret_key"

# Insecure: eval() usage
def run_dynamic_code(data):
    return eval(data)

# Insecure: subprocess with shell=True
def run_command(cmd):
    subprocess.call(cmd, shell=True)

# Insecure: insecure hashing algorithm
def weak_hash(data):
    import hashlib
    return hashlib.md5(data.encode()).hexdigest()

# Insecure: use of pickle for untrusted data
def unsafe_deserialize(serialized):
    return pickle.loads(serialized)

# Insecure: disable SSL certificate verification
def download_insecure(url):
    import requests
    return requests.get(url, verify=False)

# Insecure: JWT with none algorithm (forging risk)
def create_unsecured_jwt(payload):
    return jwt.encode(payload, SECRET_KEY, algorithm="none")

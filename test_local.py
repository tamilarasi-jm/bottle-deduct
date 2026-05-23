import requests
import json
from typing import Any

url = "http://localhost:9000/2015-03-31/functions/function/invocations"

# Test root endpoint
event: dict[str, Any] = {
    "requestContext": {
        "http": {
            "method": "GET",
            "path": "/"
        }
    },
    "rawPath": "/"
}

print("Testing Lambda function...")
response = requests.post(url, json=event)
print(f"Status: {response.status_code}")
print(f"Response: {response.text}")
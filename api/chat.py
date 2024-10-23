import requests
from api.api_config import host, chat_api_name, api_key


def chat_completion(user_input: str, file_id: str) -> str:
    result = requests.post(
        host + chat_api_name,
        json={
            "user_input": user_input,
            "instructions_id": file_id,
            "api_key": api_key
        }
    )
    print(result.status_code)
    if result.status_code != 200:
        return "Error"
    result = result.json()
    if result["code"] < 0:
        return result["message"]
    data = result["data"]
    return data["content"]

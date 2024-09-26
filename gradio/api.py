import requests


host = ""
chat_method = "/api/chat_completion"
api_key = ""


def chat_completion(user_input: str, file_id: str) -> str:
    result = requests.post(
        host + chat_method,
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
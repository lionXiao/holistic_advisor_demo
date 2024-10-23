import requests
from api.api_config import host, api_key, kb_dele_api_name, kb_list_api_name, kb_create_api_name


def kb_create_api(kb_first_title: str, kb_second_title: str, kb_id: str = "", description: str = "", user_id: str="") -> str:
    result = requests.post(
        host + kb_create_api_name,
        json={
            "kb_first_title": kb_first_title,
            "kb_second_title": kb_second_title,
            "kb_id": kb_id,
            "description": description,
            "user_id": user_id,
            "api_key": api_key
        }
    )
    if result.status_code != 200:
        return "Error"
    result = result.json()
    return result["msg"]
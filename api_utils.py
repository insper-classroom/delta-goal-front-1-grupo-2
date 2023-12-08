import requests 

BASE_URL = "'http://127.0.0.1:5000/'"

def cadastra_jogo(data,files):
    try:
        response = requests.post(f"{BASE_URL}/jogo",data=data,files=files)
        response.raise_for_status()
        return True, response.json()
    except Exception as e:
        return False, {"message": str(e)}
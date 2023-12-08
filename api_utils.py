import requests 

BASE_URL = "http://127.0.0.1:5000/"

def cadastra_jogo_dados(data):
    try:
        response = requests.post(f"{BASE_URL}jogo/dados",data=data)
        response.raise_for_status()
        return True, response.json()
    except Exception as e:
        return False, {"message": str(e)}
    
def cadastra_jogo_logos(nomes,files):
    try:
        response = requests.post(f"{BASE_URL}jogo/logos",data=nomes,files=files)
        response.raise_for_status()
        return True, response.json()
    except Exception as e:
        return False, {"message": str(e)}
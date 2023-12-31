import requests 

BASE_URL = "https://api-deltagoal-3153c6f80993.herokuapp.com/"

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
    
def cria_json(id_jogo):
    try:
        response = requests.get(f"{BASE_URL}jogo/{id_jogo}")
        response.raise_for_status()
        return True, response.json()
    except Exception as e:
        return False, {"message": str(e)}
    

def cadastra_json(json):
    try:
        response = requests.post(f"{BASE_URL}jogo/json",json=json)
        response.raise_for_status()
        return True, response.json()
    except Exception as e:
        return False, {"message": str(e)}
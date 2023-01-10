import requests
import settings


def check_login(login: str, password: str):
    data = f'{{ "name": "{login}", "password": "{password}" }}'
    r = requests.post(f'http://{settings.SERVER_HOST}:{settings.SERVER_PORT}/user/login', data=data)
    answer = r.json()

    return answer


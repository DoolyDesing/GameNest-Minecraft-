import requests, time

def get_ip(token, server_id, interval=5, retries=20):
    url = f'https://api.cloudvps.reg.ru/v1/reglets/{server_id}'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    for try_num in range(retries):
        time.sleep(interval)
        res = requests.get(url, headers=headers)
        
        if res.status_code == 200:
            data = res.json()
            ip_address = data['reglet'].get('ip')
            
            if ip_address:  # Проверяем, есть ли IP-адрес
                print('IP назначен:', ip_address)
                return ip_address
            else:
                print(f'IP не назначен, повторная проверка... {try_num + 1}')
        else:
            print(f"Ошибка при получении информации о сервере. Статус: {res.status_code}, сообщение: {res.text}")
    
    return None  # Если IP не назначен после всех попыток

import requests, time

def check_server_status(token, server_id, interval=15, retries=20):
    url = f'https://api.cloudvps.reg.ru/v1/reglets/{server_id}'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    for try_num in range(retries):
        time.sleep(interval)
        res = requests.get(url, headers=headers)
        
        if res.status_code == 200:
            data = res.json()
            status = data['reglet'].get('status')
            
            if status == 'active':  # Проверяем, есть ли IP-адрес
                print('Сервер запущен')
                return True
            else:
                print(f'Сервер не активен, повторная проверка... {try_num + 1}')
        else:
            print(f"Ошибка при получении информации о сервере. Статус: {res.status_code}, сообщение: {res.text}")
    
    return False  # Если IP не назначен после всех попыток


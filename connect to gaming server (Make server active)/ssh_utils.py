import subprocess

def create_script(name, server_ip): 
    content = f"""#!/bin/bash
                ssh "root@{server_ip}" 'mkdir -p ~/Hello_World'
                """
    # Создаем и записываем в файл
    with open(f"{name}.sh", "w") as file:
        file.write(content)

    print(f"Файл {name} успешно создан.")

def start_script(name):
    # Запускаем скрипт
    try:
        result = subprocess.run(['bash', name], check=True, text=True, capture_output=True)
        print(f"Скрипт выполнен успешно. Вывод: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Произошла ошибка при выполнении скрипта. Статус: {e.returncode}, сообщение: {e.stderr}")
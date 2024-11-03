import paramiko

def prepare_ssh_server(hostname, username='root', commands=None):
    """
    Подключается к серверу по SSH и выполняет команды подготовки.

    :param hostname: IP-адрес сервера.
    :param username: Пользователь для подключения (по умолчанию root).
    :param commands: Список команд для выполнения на сервере (по умолчанию создаёт директорию Hello_World).
    """
    if commands is None:
        commands = ['mkdir ~/Hello_World']  # Команда по умолчанию, если список команд не передан

    # Создаём SSH-клиент и подключаемся к серверу
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Автоматически добавляем сервер в список известных

    try:
        ssh.connect(hostname=hostname, username=username)
        for command in commands:
            stdin, stdout, stderr = ssh.exec_command(command)
            print(f"Running command: {command}")
            print("Output:", stdout.read().decode())
            print("Error:", stderr.read().decode())
    except paramiko.SSHException as e:
        print(f"SSH connection failed: {e}")
    finally:
        ssh.close()

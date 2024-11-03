from create_server import create_server
from server_utils import get_ip, check_server_status
from ssh_utils import create_script, start_script, delete_script
token = 'a7bb7d93acf6fcea1a9e387059b505b8a71f5d73c6236861fdca59796eed4411f3d9d8c1156cacb40d18063918652f29'
my_ssh = '4b:9d:36:18:f7:cf:f8:7b:61:8a:8e:48:d3:74:52:17'

data = create_server(token, my_ssh)
server_id = data['reglet']['id']
server_name = data['reglet']['name']
server_ip = get_ip(token, server_id)
if check_server_status(token, server_id) == True:
	print("Можно подключаться по ssh")
	create_script(server_name)
	start_script(server_name)
	delete_script(server_name)

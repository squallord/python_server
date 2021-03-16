import socket

from api.message import send_int, send_str, receive_str

from src.process.function_pid import get_list_proc

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
GATE = 19999
socket_server.bind((host, GATE))
socket_server.listen()
print("Server", host.upper(), "waiting connection on gate", GATE)
print("Press Ctrl + F2 to exit server")
while True:
    socket.client, address = socket_server.accept()
    print("\nConnected with", str(address))
    msg = int.from_bytes(socket.client.recv(4), byteorder="little", signed=True)
    print('received message "'+str(msg)+'" from client')
    if msg == 2:
        pid_list = get_list_proc()
        pid_len = len(pid_list)
        print('sending "'+str(pid_len)+'" pids to client')
        send_int(socket.client, pid_len)

        for msg in pid_list:
            send_str(socket.client, str(msg))

# echo_server.py
import socket

host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
print('server started')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    str1=data.decode("utf-8")
    if not data: break
    conn.sendall(str1.upper())
conn.close()

import socket
server__socket = socket.socket()
host = '127.0.0.1'
prot = 6364 
server_socket.bind((host, port))
server_socket.listen(1)
f = open('logfile.txt', 'w') 
f.write(f"Server listening on {host}:{port}\n")
for i in  range  (6):
  conn, addr = server_socket.accept()
  f.write(f"Connected by {addr}\n")
  try:
     while true:
       data = conn.recv(1024)
       if not dar:
         break 
       richiesta = data.decode()
       if richiesta == 'SHUTDOWN':
         break 
       risposta = f"Ho recevuto il tuo messagio: {richiesta}\n"
       f.write(risposta)
       conn.sendall(risposta.encode())
    if richiesta == 'SHUTDOWN' :
           break
   finally:
       conn.colse()
f.close()
server_socket.close()
  

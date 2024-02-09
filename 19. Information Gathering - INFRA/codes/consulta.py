#!/usr/share/python
import sys, socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)  # Define um tempo limite de 10 segundos


domain=sys.argv[1]
s.connect(("whois.iana.org", 43))

s.send((domain+"\r\n").encode())


try:
    resposta = s.recv(1024).decode().split()
   
except ConnectionResetError as e:
    print("Erro de conexão:", e)
    
indice_query= resposta.index("refer:") +1

print(resposta[indice_query])



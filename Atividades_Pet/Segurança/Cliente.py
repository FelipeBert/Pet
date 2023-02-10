import random as rd
import socket

def minimo(n1, n2):
    while n2 != 0:
        r = n1 % n2
        n1 = n2
        n2 = r
    return n1

def chave_publica(t):
    while True:
        chave_p = rd.randrange(2, t)
        if minimo(t, chave_p) == 1:
            return abs(chave_p)

def chave_privada(t, e):
    chave_pv = 0
    while ((chave_pv * chave_p) % t) != 1:
        chave_pv += 1
    return chave_pv

def criptografar(mensagem, chave, n_r):
    msg_c = ""
    for letra in mensagem:
        k = (ord(letra) ** chave) % n_r
        msg_c += chr(k)
    return msg_c

def descriptografar(mensagem, n, chave):
    msg_d = ""
    for letra in mensagem:
        k = (ord(letra) ** chave) % n
        msg_d += chr(k)
    return msg_d

p = 11
q = 13
n = p * q

x = p - 1
y = q - 1
t = (x * y)

chave_p = chave_publica(t)
chave_pv = chave_privada(t, chave_p)

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 8888))

data = cliente.recv(1024)
chave_rs = data.decode('utf-8')
chave_r = int(chave_rs)

cliente.send(str(chave_p).encode('utf-8'))

data_n = cliente.recv(1024)
n_rs = data_n.decode('utf-8')
n_r = int(n_rs)

cliente.send(str(n).encode('utf-8'))

termino = False

while not termino:
    msg = input("Digite a Mensagem: ")
    msg_e = criptografar(msg, chave_r, n_r)
    msg_e = msg_e.encode('utf-8')
    cliente.send(msg_e)

    msg_r = cliente.recv(1024).decode('utf-8')
    print("Mensagem Criptografada: ", msg_r)
    msg_rl = descriptografar(msg_r, n, chave_pv)
    if msg_rl == 'sair':
        termino = True
    else:
        print("Mensagem Descriptografada: ", msg_rl)

cliente.close()
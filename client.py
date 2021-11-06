from socket import *
import threading as th
priv = input('your private ip>> '), int(input('your private port>> '))
server = ('89.108.79.2', 50666)

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(priv)

to_send = priv[0] + '#' + str(priv[1])
sock.sendto(to_send.encode('utf-8'), server)
print(f'"{to_send}"" -> {server}')

resp = sock.recvfrom(1024).decode('utf-8')
print(f'got data from server -> "{resp}"')

def call_other(addr, sock):
    while 1:
        sock.sendto(b'test', addr)
        print(f'"test" -> {addr}')
    
def listen(sock):
    while 1:
        resp = sock.recvfrom(1024).decode('utf-8')
        print(f'idk from where, but -> "{resp}"')
    
public = resp.split('$')[0].split(', ')
pb_addr = (public[0][1:], int(public[1][:-1]))
print('another node pb_addr', pb_addr) 

private = resp.split('$')[0].split(', ')
pr_addr = (private[0][1:], int(private[1][:-1]))
print('another node pr_addr', pr_addr)

pub = threading.Thread(target=call_other, args=[pb_addr, sock])
priv = threading.Thread(target=call_other, args=[pr_addr, sock])
lstn = threading.Thread(target=listen, args=[sock])
lstn.start()
pub.start()
priv.strart()

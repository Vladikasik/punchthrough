from socket import *
import threading as th
priv = input('your private ip>> '), int(input('your private port>> '))
server = ('89.108.79.2', 50666)

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(priv)

to_send = priv[0] + '#' + str(priv[1])
sock.sendto(to_send.encode('utf-8'), server)
print(f'"{to_send}"" -> {server}')

resp, addr = sock.recvfrom(1024)
resp = resp.decode('utf-8')
print(f'got data from server -> "{resp}"')

def call_other(addr, sock):
    for _ in range(5):
        print(f'"test" -> {addr}')
        sock.sendto(b'test2', addr)
        
def listen(sock):
    while 1:
        resp, addr = sock.recvfrom(1024).decode('utf-8')
        print(f'{resp} <- "{addr}"')
    
public = resp.split('$')[0].split('#')
pb_addr = (public[0], int(public[1]))
print('another node pb_addr', pb_addr) 

private = resp.split('$')[1].split('#')
pr_addr = (private[0], int(private[1]))
print('another node pr_addr', pr_addr)

pub = th.Thread(target=call_other, args=[pb_addr, sock])
priv = th.Thread(target=call_other, args=[pr_addr, sock])
lstn = th.Thread(target=listen, args=[sock])
lstn.start()
pub.start()
priv.start()

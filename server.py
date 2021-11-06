from socket import *
server = ('89.108.79.2', 50666)
sock = socket(AF_INET, SOCK_DGRAM)
def exchange(sock):
    data1, addr1 = sock.recvfrom(1024)
    data2, addr2 = sock.recvfrom(1024)
    print(f'"{data1}" <- {addr1}')
    print(f'"{data2}" <- {addr2}')

    data1 = data1 + '$' + addr1[0] + addr1[1]
    data2 = data2 + '$' + addr2[0] + addr2[1]
    
    sock.sendto(data1, addr2)
    sock.sendto(data2, addr1)
while 1:
    exchange(sock)
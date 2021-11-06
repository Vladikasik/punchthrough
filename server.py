from socket import *
server = ('89.108.79.2', 50666)
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(server)
def exchange(sock):
    data1, addr1 = sock.recvfrom(1024)
    data1 = data1.decode('utf-8')
    print(f'"{data1}" <- {addr1}')

    data2, addr2 = sock.recvfrom(1024)
    data2 = data2.decode('utf-8')
    print(f'"{data2}" <- {addr2}')

    data1 = data1 + '$' + str(addr1[0]) + str(addr1[1])
    data2 = data2 + '$' + str(addr2[0]) + str(addr2[1])
    
    sock.sendto(data1.encode('urf-8'), addr2)
    sock.sendto(data2.encode('urf-8'), addr1)
while 1:
    exchange(sock)
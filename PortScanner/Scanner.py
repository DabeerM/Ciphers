import socket

# create an INET (IPv4), STREAMing (TCP) socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def scan_port(port:int)->bool:
    try:
        # Try to connect
        con = s.connect((target, port))
        return True
    except:
        return False

target = input('What website do you wish to scan: ')

PORT_MIN, PORT_MAX = 0, 65535

# Scanning ports now
for port in range(PORT_MIN, PORT_MAX):
    if scan_port(port):
        print('Port', port, 'is open')

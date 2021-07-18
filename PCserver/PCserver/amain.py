import socket
import time
if __name__ == '__main__':
    # socket.setblocking(0)
    # hostname = socket.gethostname()
    # UDP_IP = socket.gethostbyname(hostname)

    # the ip address of the server
    # UDP_IP = '192.168.0.106'
    UDP_IP = '192.168.0.112'

    # tge socket port number
    UDP_PORT = 4569
    
    # initialize the socket and bind it
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    sock.setblocking(0)
    sock.bind((UDP_IP, UDP_PORT))

    # receive data from watch
    a = range(1000)
    counter = 0
    start_time = time.time()
    
    for i in a:
        data = sock.recv(1024)
    elapsed_time =time.time() - start_time  
    print(1000/elapsed_time)

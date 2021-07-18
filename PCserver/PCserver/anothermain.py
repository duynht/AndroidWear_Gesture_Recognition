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
    
    counter = 0
    while True:
        if counter == 0:
            start_time = time.time()
        current_time = time.time()
        elapsed_time = current_time - start_time
        counter += 1
        if elapsed_time > 1:
            break
        # print("Data: ")
        data, addr = sock.recvfrom(1024)
        # print(data)
    print(counter)

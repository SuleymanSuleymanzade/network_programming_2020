import socket 
import argparse 
import random 
from datetime import datetime 
import sys 

MAX_BYTES = 65536 

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print(f'server bind with {sock.getsockname()}')

    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        
        if random.random() < 0.5:
            print(f'server has droped the package from {address}')
            continue

        text = data.decode('ascii')
        print(f'The client {address}, says {text}')

        server_text = f'this is a server, your data was {len(data)} byted long'
        server_data = server_text.encode('ascii')
        sock.sendto(server_data, address)

def client(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = sys.argv[2]
    sock.connect((hostname, port))
    text = f"this is the text from the client. we sent it at {datetime.now()}"
    data = text.encode('ascii')

    delay = 0.1
    while True:
        sock.send(data)
        print(f'waiting for {delay} sec')
        sock.settimeout(delay)
        try:
            data = sock.recv(MAX_BYTES)
        except socket.timeout:
            delay *= 2
            if delay > 2:
                raise RuntimeError('The message is not recieved something is wrong')
        else:   
            break
    print(f"server message: {data.decode('ascii')}")


def main():
    choices = {'client':client, 'server':server}
    parser = argparse.ArgumentParser(description = 'Send and recieve from UDP')
    parser.add_argument('role', choices=choices, help = 'who you want to be')
    parser.add_argument('-p', metavar='PORT', type=int, default=1025)
    parser.add_argument('host')

    args = parser.parse_args()

    func = choices[args.role]
    func(args.host, args.p)



if __name__ == "__main__":
    main()




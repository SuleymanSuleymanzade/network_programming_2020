import socket 
import argparse 
from datetime import datetime 
MAX_BYTES = 65536 

def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    print(f'server bind with {sock.getsockname()}')

    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        print(f'The client {address}, says {text}')

        server_text = f'this is a server, your data was {len(data)} byted long'
        server_data = server_text.encode('ascii')
        
        sock.sendto(server_data, address)

def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = f"this is the text from the client. we sent it at {datetime.now()}"
    data = text.encode('ascii')

    sock.sendto(data, ('127.0.0.1', port))
    print(f'the OS bind the client to {sock.getsockname()} socket')
    
    data, address = sock.recvfrom(MAX_BYTES)
    text = data.decode('ascii')
    print(f'the server {address} sends us text: {text}')


def main():
    choices = {'client':client, 'server':server}
    parser = argparse.ArgumentParser()
    parser.add_argument('role', choices=choices)
    parser.add_argument('-p', metavar='PORT', type=int, default=1025)

    args = parser.parse_args()

    func = choices[args.role]
    func(args.p)



if __name__ == "__main__":
    main()




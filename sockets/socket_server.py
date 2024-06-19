"""Server Socket"""
import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()
    print(conn)
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            print(addr, ' >> ', data.decode())
            msg = input('SERVER >> ')
            conn.sendall(msg.encode())
            if not data:
                break
            print(data.decode())
            conn.sendall(data)



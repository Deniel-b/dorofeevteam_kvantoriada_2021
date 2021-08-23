import socket

print("manipulator running")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("0.0.0.0", 3000))

sock.listen(1)

conn, addr = sock.accept()

print("connected", addr)


while True:
    data = conn.recv(1024)

    if data:
        print(data)
    #/////////////////////////////////////////
        if data == b"positive_X":
            conn.send(b"towarding positive X")
            print("towarding positive X")
        elif data == b"positive_Y":
            conn.send(b"towarding positive Y")
            print("towarding positive Y")
        elif data == b"positive_Z":
            conn.send(b"towarding positive Z")
            print("towarding positive Z")
        #/////////////////////////////////////////
        elif data == b"negative_X":
            conn.send(b"towarding negative X")
            print("towarding negative X")
        elif data == b"negative_Y":
            conn.send(b"towarding negative Y")
            print("towarding negative Y")
        elif data == b"negative_Z":
            conn.send(b"towarding negative Z")
            print("towarding negative Z")
        #/////////////////////////////////////////
        elif data == b"positive_rotating":
            conn.send(b"positive_rotating")
            print("positive_rotating")
        elif data == b"negative_rotating":
            conn.send(b"negative_rotating")
            print("negative_rotating")




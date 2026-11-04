import socket
import threading

RED = "\033[91m"
RESET = "\033[0m"

banner = f"""
{RED}
 ____  _               _               _   _      _
/ ___|| |__   __ _  __| | _____      _| \\ | | ___| |_
\\___ \\| '_ \\ / _` |/ _` |/ _ \\ \\ /\\ / /  \\| |/ _ \\ __|
 ___) | | | | (_| | (_| | (_) \\ V  V /| |\\  |  __/ |_
|____/|_| |_|\\__,_|\\__,_|\\___/ \\_/\\_/ |_| \\_|\\___|\\__|

                                        by 0xredlog v1.1

  For educational use and authorized testing only.
  Unauthorized scanning is illegal.
{RESET}"""

print(banner)

ip = input("Enter target IP: ")
print(f"\n{RED}[*] Scanning {ip}...{RESET}\n")

def scan(port): 
    sock = socket.socket()
    sock.settimeout(0.5)
    try:
        result = sock.connect_ex((ip, port))
    except:
        print("[!] Error connecting to target")
        return
 
    if result == 0:
        print(f"[+] Port {RED}{port}{RESET} OPEN")
        try:
            banner = sock.recv(1024).decode().strip()
            print(f"    Banner: {banner}")
            with open(f'{ip}-results.txt', 'a') as f:
                f.write(f"Port {port} OPEN -{banner}\n")
        except:
            with open(f"{ip}results.txt", "a") as f:
                 f.write(f"Port {port} OPEN \n")
        pass
    sock.close()


for port in range(1, 1001): 
    t = threading.Thread(target=scan, args=(port,)) 
    t.start() 

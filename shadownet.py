import socket

RED = "\033[91m"
RESET = "\033[0m"

banner = f"""
{RED}
 ____  _               _               _   _      _
/ ___|| |__   __ _  __| | _____      _| \\ | | ___| |_
\\___ \\| '_ \\ / _` |/ _` |/ _ \\ \\ /\\ / /  \\| |/ _ \\ __|
 ___) | | | | (_| | (_| | (_) \\ V  V /| |\\  |  __/ |_
|____/|_| |_|\\__,_|\\__,_|\\___/ \\_/\\_/ |_| \\_|\\___|\\__|

                                        by 0xredlog v1.0

  For educational use and authorized testing only.
  Unauthorized scanning is illegal.
{RESET}"""

print(banner)

ip = input("Enter target IP: ")
print(f"\n{RED}[*] Scanning {ip}...{RESET}\n")

for port in range(1, 1001):
    sock = socket.socket()
    sock.settimeout(0.5)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print(f"[+] Port {RED}{port}{RESET} OPEN")
    sock.close()

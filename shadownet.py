import socket
import threading
import argparse
import requests
import subprocess

# ─── Colors ───────────────────────────────────────────────
RED = "\033[91m"
RESET = "\033[0m"

# ─── ASCII Banner ─────────────────────────────────────────
ascii_banner = f"""
{RED}
 ____  _               _               _   _      _
/ ___|| |__   __ _  __| | _____      _| \\ | | ___| |_
\\___ \\| '_ \\ / _` |/ _` |/ _ \\ \\ /\\ / /  \\| |/ _ \\ __|
 ___) | | | | (_| | (_| | (_) \\ V  V /| |\\  |  __/ |_
|____/|_| |_|\\__,_|\\__,_|\\___/ \\_/\\_/ |_| \\_|\\___|\\__|

                                        by 0xredlog v3.0

  For educational use and authorized testing only.
  Unauthorized scanning is illegal.
{RESET}"""

print(ascii_banner)

# ─── Argument Flags ───────────────────────────────────────
parser = argparse.ArgumentParser(description='ShadowNet by 0xredlog')
parser.add_argument("-t", help="Target IP")
parser.add_argument("-p", help="Port range e.g. 1-1000 or single port e.g. 80")
parser.add_argument("-o", help="Output file name")
args = parser.parse_args()

# ─── Target IP ────────────────────────────────────────────
if args.t:
    ip = args.t
else:
    ip = input("Enter target IP: ")

# ─── Ping Check ───────────────────────────────────────────
result = subprocess.run(["ping", "-c", "1", ip],
                        capture_output=True, text=True)
if result.returncode == 0:
    print(f"{RED}[+] Host {ip} is ALIVE — starting scan...{RESET}")
else:
    print(f"[-] Host {ip} is DOWN — stopping.")
    exit()

# ─── Port Range ───────────────────────────────────────────
if args.p:
    if "-" in args.p:
        ports = args.p.split("-")
        start = int(ports[0])
        end = int(ports[1])
    else:
        start = int(args.p)
        end = int(args.p)
else:
    start = 1
    end = 1000

# ─── Output File ──────────────────────────────────────────
if args.o:
    filename = args.o
else:
    filename = f"{ip}-results.txt"

print(f"\n{RED}[*] Scanning {ip} ports {start}-{end}...{RESET}\n")

# ─── Scan Function ────────────────────────────────────────
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
            with open(filename, 'a') as f:
                f.write(f"Port {port} OPEN - {banner}\n")
        except:
            with open(filename, 'a') as f:
                f.write(f"Port {port} OPEN\n")
        if port == 80 or port == 443:
            try:
                protocol = "https" if port == 443 else "http"
                r = requests.get(f"{protocol}://{ip}", timeout=2)
                print(f"    HTTP Status: {r.status_code}")
                print(f"    Server: {r.headers.get('Server', 'unknown')}")
            except:
                pass
    sock.close()

# ─── Threading Loop ───────────────────────────────────────
for port in range(start, end + 1):
    t = threading.Thread(target=scan, args=(port,))
    t.start()

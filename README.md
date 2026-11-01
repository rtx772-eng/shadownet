<p align="center">
  <img src="logo.png" alt="ShadowNet Logo" width="800"/>
</p>

<p align="center">
 <strong>بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ</strong><br>
  
  <em>In the name of Allah , the Most Gracious , the Most Merciful </em><br><br>
  <strong>الحمد لله على كل شيء — Alhamdulillah for everything 🤲</strong><br><br>
  <em> InshAllah — By His will .</em>
</p>

---

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux-black?style=for-the-badge&logo=linux)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![Author](https://img.shields.io/badge/Author-0xredlog-red?style=for-the-badge)

---

## What is ShadowNet?

```
 ____  _               _               _   _      _
/ ___|| |__   __ _  __| | _____      _| \ | | ___| |_
\___ \| '_ \ / _` |/ _` |/ _ \ \ /\ / /  \| |/ _ \ __|
 ___) | | | | (_| | (_| | (_) \ V  V /| |\  |  __/ |_
|____/|_| |_|\__,_|\__,_|\___/ \_/\_/ |_| \_|\___|\__|

                                        by 0xredlog v1.0
```

ShadowNet is a lightweight CLI port scanner built from scratch in Python.  
It scans a target IP across ports 1–1000 and reports every open port — fast, clean, no noise.

Built as a first offensive security tool by a self-taught red teamer.

---

## Features

- 🔍 Scans ports 1 to 1000
- ⚡ Fast timeout per port (0.5s)
- 🎯 Clean output — open ports only
- 💻 Pure Python — no dependencies
- 🖥️ Works on any Linux machine

---

## Usage

```bash
git clone https://github.com/rtx772-eng/shadownet
cd shadownet
python3 shadownet.py
```

```
Enter target IP: 45.33.32.156

[+] Port 22 OPEN
[+] Port 80 OPEN
```

---

## How It Works

```
1. Ask user for target IP
2. Loop through ports 1 to 1000
3. Try to connect to each port (socket)
4. Print open ports only
```

Under the hood — Python's `socket` library knocks on each port.  
If the connection returns `0` → port is open.  
Anything else → closed, move on.

---

## Code

```python
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
```

---

## Legal

> ShadowNet is built for educational purposes and authorized testing only.  
> Only scan targets you own or have explicit permission to test.  
> Unauthorized scanning is illegal.

---

## Author

**Mohamed Cherradi** — 0xredlog  
Self-Taught Red Teamer | Offensive Security | AI Red Teaming

- GitHub: [@rtx772-eng](https://github.com/rtx772-eng)
- LinkedIn: [mohamed-cherradi](https://www.linkedin.com/in/mohamed-cherradi-0b0140432)
- Instagram: [@0xredlogz](https://instagram.com/0xredlogz)

---

## Roadmap

- [ ] v1.1 — Add banner grabbing (detect service on port)
- [ ] v1.2 — Custom port range input
- [ ] v1.3 — Save results to file
- [ ] v2.0 — Multi-threaded (10x faster)
- [ ] v3.0 — Full recon suite

---

*First tool. Not the last. — 0xredlog*

<p align="center">
  <em>إِنْ شَاءَ اللَّهُ</em><br>
  <strong>Inshallah</strong>
</p>

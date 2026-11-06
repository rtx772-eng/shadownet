<p align="center">
  <strong> بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ </strong><br>
  <em> In the name of Allah , the Most Gracious , the Most Merciful </em><br><br>
  <strong> الحمد لله على كل شيء — Alhamdulillah for everything 🤲</strong><br><br>
  <em> Inshallah — By His will .</em>
</p>

---

<p align="center">
  <img src="logo.png" alt="ShadowNet Logo" width="800"/>
</p>

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux-black?style=for-the-badge&logo=linux)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![Author](https://img.shields.io/badge/Author-0xredlog-red?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-3.0-red?style=for-the-badge)
---

## What is ShadowNet?

```
 ____  _               _               _   _      _
/ ___|| |__   __ _  __| | _____      _| \ | | ___| |_
\___ \| '_ \ / _` |/ _` |/ _ \ \ /\ / /  \| |/ _ \ __|
 ___) | | | | (_| | (_| | (_) \ V  V /| |\  |  __/ |_
|____/|_| |_|\__,_|\__,_|\___/ \_/\_/ |_| \_|\___|\__|

                                        by 0xredlog v3.0
```

What is ShadowNet?

ShadowNet is a lightweight CLI port scanner and reconnaissance tool built from scratch in Python. It scans a target IP across ports 1–1000, grabs service banners, performs HTTP recon, checks host availability, and saves results automatically — fast, clean, no noise.

Built as a first offensive security tool by a self-taught red teamer.

---

## Features

- 🔍 Scans ports 1 to 1000
- ⚡ Multi-threaded — 1000 workers at once
- 🎯 Banner grabbing — identifies service + version
- 💾 Auto-saves results to [target_ip]-results.txt
- 🛡️ Error handling — never crashes on bad input
- 🔴 Red terminal output
- 🚩 Argument flags — `-t` `-p` `-o`
- 🌐 HTTP recon — status code + server header
- 📡 Host alive check — ping before scan
- 💻 Pure Python — no dependencies
- 🖥️ Works on any Linux machine

---

## Usage

```bash

git clone https://github.com/rtx772-eng/shadownet
cd shadownet
pip install requests --break-system-packages
python3 shadownet.py

```

### With flags
```bash
# full scan
python3 shadownet.py -t 45.33.32.156

# custom port range
python3 shadownet.py -t 45.33.32.156 -p 1-100

# single port
python3 shadownet.py -t 45.33.32.156 -p 80

# custom output file
python3 shadownet.py -t 45.33.32.156 -o myscan.txt

# all flags
python3 shadownet.py -t 45.33.32.156 -p 1-1000 -o results.txt
```

### Without flags
```bash
python3 shadownet.py
# asks for IP interactively

[+] Host 45.33.32.156 is ALIVE — starting scan...

[*] Scanning 45.33.32.156 ports 1-1000...

[+] Port 22 OPEN
    Banner: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
[+] Port 80 OPEN
    HTTP Status: 200
    Server: Apache/2.4.7 (Ubuntu)
```

---

## How It Works

```
1. Ping check — is host alive? If not → stop.
2. Ask user for target IP (flag or input)
3. Launch threads — one per port
4. Each thread knocks on its port (socket)
5. If open → grab banner + HTTP headers + save to file
6. Results saved to [ip]-results.txt automatically

```

Under the hood — socket → knocks on each port
threading → runs all workers simultaneously
requests → grabs HTTP headers on port 80/443
subprocess → pings target before scanning
If the connection returns `0` → port is open → banner grabbed.
Anything else → closed, move on silently.

---

## Code

The full source code is available in the repository.
See `shadownet.py` for the complete implementation.

---

## Legal

> ShadowNet is built for educational purposes and authorized testing only.
> Only scan targets you own or have explicit permission to test.
> Unauthorized scanning is illegal.

---

## Author

Mohamed Cherradi — 0xredlog Self-Taught Red Teamer | Offensive Security | AI Red Teaming

GitHub: @rtx772-eng
LinkedIn: mohamed-cherradi
Instagram: @0xredlogz

- GitHub: [@rtx772-eng](https://github.com/rtx772-eng)
- LinkedIn: [mohamed-cherradi](https://www.linkedin.com/in/mohamed-cherradi-0b0140432)
- Instagram: [@0xredlogz](https://instagram.com/0xredlogz)

---

## Roadmap

- [x] v1.0 — Basic port scanner
- [x] v1.1 — Threading + banner grabbing + file saving
- [x] v2.0 — Argument flags (-t, -p, -o)
- [x] v3.0 — HTTP recon + ping check
- [ ] v4.0 — Full recon suite

---

*First tool. Not the last. — 0xredlog*

<p align="center">
  <em> إِنْ شَاءَ اللَّهُ </em><br>
  <strong< Inshallah </strong>
</p>

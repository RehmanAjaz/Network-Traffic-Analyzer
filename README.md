<div align="center">

# 🕵️ NetSniff — Network Packet Sniffer

**A lightweight, real-time network packet capture and protocol analysis tool built with Python & Scapy.**

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scapy](https://img.shields.io/badge/Scapy-Latest-green?style=for-the-badge)](https://scapy.net/)
[![Platform](https://img.shields.io/badge/Platform-Linux-orange?style=for-the-badge&logo=linux&logoColor=white)](https://www.linux.org/)
[![License](https://img.shields.io/badge/License-Educational-red?style=for-the-badge)](#license)

<br/>

> ⚠️ **For educational and authorized use only.**  
> Unauthorized packet sniffing is illegal. Always obtain proper permission before monitoring any network.

</div>

---

## 📌 What is NetSniff?

**NetSniff** is a terminal-based network packet sniffer that captures and analyzes live network traffic in real time. It inspects IP packet headers to identify protocols — **TCP**, **UDP**, and **ICMP** — and displays source/destination IPs and ports directly in your terminal.

No bloated GUI. No complex setup. Just raw network visibility.

```
Sniffer started... Press CTRL+C to stop.

[TCP]  192.168.1.10  →  142.250.80.46  |  Port 52341  →  443
[UDP]  192.168.1.10  →  8.8.8.8        |  Port 54201  →  53
[ICMP] 192.168.1.10  →  192.168.1.1
[TCP]  142.250.80.46 →  192.168.1.10   |  Port 443    →  52341
```

---

## ✨ Features

- 📡 **Real-time packet capture** from live network interfaces
- 🔍 **Protocol detection** — TCP, UDP, ICMP, and generic IP
- 🌐 **IP header analysis** — source & destination addresses
- 🔌 **Port extraction** for TCP and UDP packets
- 🪶 **Zero storage overhead** — packets are analyzed on-the-fly, never stored
- 🧩 **Modular and extensible** — easy to build upon

---

## 🛠️ Tech Stack

| Component | Detail |
|-----------|--------|
| Language | Python 3 |
| Core Library | [Scapy](https://scapy.net/) |
| Recommended OS | Linux (Kali / Ubuntu) |
| Privileges | Root / Administrator |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed
- `pip` package manager
- Root / sudo privileges

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/netsniff.git
cd netsniff

# 2. Install dependencies
pip install scapy
```

### Run

```bash
sudo python3 Sniffer.py
```

Press `CTRL + C` to stop the sniffer.

---

## ⚙️ How It Works

```
Network Interface
       │
       ▼
  sniff() — captures packets in real-time
       │
       ▼
  IP Layer check — skip non-IP packets
       │
       ├──► TCP?  → Print src IP, dst IP, src port, dst port
       ├──► UDP?  → Print src IP, dst IP, src port, dst port
       ├──► ICMP? → Print src IP, dst IP
       └──► IP?   → Print src IP, dst IP
```

The sniffer operates at the **network interface level**, reading raw packet headers only. It does **not** capture, decrypt, or store payload data.

---

## 📂 Project Structure

```
netsniff/
│
├── Sniffer.py      # Core packet capture & analysis logic
└── README.md       # Project documentation
```

---

## 🔬 Supported Protocols

| Protocol | Full Name | Port Info | Common Use |
|----------|-----------|-----------|------------|
| `TCP` | Transmission Control Protocol | ✅ Shown | Web, Email, SSH |
| `UDP` | User Datagram Protocol | ✅ Shown | DNS, Streaming, Gaming |
| `ICMP` | Internet Control Message Protocol | ❌ N/A | Ping, Diagnostics |
| `IP` | Generic IP (other) | ❌ N/A | Fallback |

---

## 🔐 Ethical & Legal Notice

This tool is intended **strictly for educational use** in authorized environments.

- ✅ Use on networks you own or have **explicit written permission** to monitor
- ✅ Ideal for CTFs, lab environments, and cybersecurity coursework
- ❌ Do **not** use on public, corporate, or any unauthorized network
- ❌ Intercepting third-party traffic may violate laws such as the **CFAA**, **GDPR**, and local regulations

---

## 🗺️ Roadmap

- [ ] CLI flags for interface selection (`-i eth0`)
- [ ] Filter by protocol or IP (`--filter tcp`)
- [ ] Save captures to `.log` or `.csv`
- [ ] Export as `.pcap` (Wireshark-compatible)
- [ ] Live packet count and bandwidth statistics
- [ ] Color-coded terminal output by protocol

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve NetSniff:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed for **educational purposes only.**  
Use responsibly and ethically.

---

<div align="center">

Made with 🛡️ for cybersecurity learners everywhere.  
⭐ Star this repo if you found it helpful!

</div>

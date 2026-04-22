# IoT Deception Honeypot Network for Healthcare

##  Project Overview
This project implements a **deception-based cybersecurity system** designed to simulate a vulnerable healthcare IoT device and capture attacker behavior in real-time.

With the rapid growth of IoT devices in healthcare, systems are increasingly exposed to cyber threats such as brute-force attacks, unauthorized access, and malware deployment.  
This project demonstrates how a **honeypot (Cowrie)** can be used to detect, log, and analyze such attacks.

---

##  Objectives
- Simulate a real-world healthcare IoT device
- Capture attacker activity (login attempts, commands, sessions)
- Extract Indicators of Compromise (IoCs)
- Visualize attack patterns and trends
- Understand attacker behavior in a controlled environment

---

##  Architecture

- **Ubuntu Server** → Honeypot (Cowrie)
- **Kali Linux** → Attacker machine
- **Host-only Network** → Isolated lab environment
- **Python Scripts** → Log analysis & visualization

---

##  Technologies & Tools Used

- Cowrie SSH Honeypot  
- Python 3  
- Kali Linux  
- Ubuntu Server  
- Hydra (Brute-force attack simulation)  
- Flask (Dashboard)  
- Matplotlib (Charts)  
- Folium (Geographic map)  
- VirtualBox  

---

##  Project Workflow

### 🟢 Week 1 — Environment Setup & Simulation
- Created two virtual machines (Ubuntu & Kali)
- Configured host-only network (192.168.56.x)
- Installed and configured Cowrie honeypot
- Simulated healthcare device (`vitals-monitor-04`)

---

### 🟡 Week 2 — Attack Simulation & Data Capture
- Performed SSH-based manual attack
- Simulated brute-force attack using Hydra
- Executed attacker commands:
  - `ls`, `pwd`, `whoami`, `cat /etc/passwd`
- Captured logs in:
  - `cowrie.log`
  - `cowrie.json`

---

### 🔵 Week 3 — Log Analysis & Threat Intelligence
- Developed Python script (`analyzer.py`)
- Parsed JSON logs
- Extracted:
  - Attacker IP addresses
  - Commands executed
  - Login attempts
  - Attack timeline
- Generated summary statistics

---

### 🔴 Week 4 — Visualization & Dashboard
- Built dashboard using Flask
- Generated:
  - Bar charts (attack statistics)
  - Pie charts (login success/failure)
- Created geographic attack map using Folium
- Visualized attacker origin (demo using public IP)

---

##  Key Features

✔ Real-time attacker interaction capture  
✔ Brute-force attack simulation  
✔ Command logging and session tracking  
✔ IoC extraction and timeline generation  
✔ Interactive dashboard visualization  
✔ Geographic attack mapping  

---

##  Screenshots

### 🔹 Hydra Brute Force Attack
![Hydra Attack](screenshots/hydra_attack.png)

### 🔹 Cowrie Logs
![Logs](screenshots/cowrie_logs.png)

### 🔹 Dashboard
![Dashboard](screenshots/dashboard.png)

### 🔹 Attack Map
![Map](screenshots/attack_map.png)

---

##  How to Run the Project

### 1. Start Honeypot
```bash
cd cowrie
source cowrie-env/bin/activate
cowrie start

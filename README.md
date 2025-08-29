# 🧪 Socket Programming in Python🧪

A hands-on collection of small socket-programming exercises in Python:
1) a **basic** single client/server echo,
2) a **multi-client** server (iterative),
3) a **multi-client** server using **threads**,
4) a **sandbox** for experiments.

> Folders in this repo: `basic/`, `multiclients/`, `multiclientsusingthreading/`, `sandbox/`.

---

## Table of Contents
- [Prerequisites](#prerequisites)
- [Get the Code](#get-the-code)
- [Common How-To](#common-how-to)
- [1) basic — Single Client/Server Echo](#1-basic--single-clientserver-echo)
- [2) multiclients — Multiple Clients (Iterative)](#2-multiclients--multiple-clients-iterative)
- [3) multiclientsusingthreading — Multiple Clients (Threaded)](#3-multiclientsusingthreading--multiple-clients-threaded)
- [4) sandbox — Experiments & Extras](#4-sandbox--experiments--extras)
- [Test on Local Network (LAN)](#test-on-local-network-lan)
- [Troubleshooting](#troubleshooting)
- [Project Structure](#project-structure)

---

## Prerequisites
- **Python 3.10+** (3.8+ will likely work; these examples use only the standard library.)
- OS: Windows / macOS / Linux
- Terminal/Command Prompt
- (Optional) Multiple terminals to run server + multiple clients

> No third-party packages required (standard `socket`, `threading`, etc.).

---

## Get the Code
```bash
# clone
git clone https://github.com/git-tarik/socket_programming.git
cd socket_programming

# (recommended) create a virtual environment
python -m venv .venv
# Windows
. .venv/Scripts/activate
# macOS/Linux
source .venv/bin/activate
```

---

## Common How-To
Most folders follow this pattern:

- A **server** script (e.g., `server.py`) that binds to `HOST` and `PORT`  
- A **client** script (e.g., `client.py`) that connects to the server  

> If the scripts accept CLI flags, use `--host` and `--port`.  
> If they don’t, open the file and edit constants near the top (e.g., `HOST = '127.0.0.1'`, `PORT = 5000`).

### Typical ports & commands
```bash
# Terminal A — start server
python server.py 

# Terminal B — start client
python client.py 

# (Optional) More clients in C/D/E...
python client.py 
```

---

## 1) `basic` — Single Client/Server Echo
**Goal:** Smallest possible request–response model.

**Concept:**
- Server: `socket() → bind() → listen() → accept() → recv()/send() → close()`
- Client: `socket() → connect() → send()/recv() → close()`

### Run
```bash
cd basic
# Server
python server.py 
# Client (new terminal)
python client.py 
```

### Try it
- Type a message in the client; the server echos it back.
- Quit convention: type `quit` or press `Ctrl+C` (depends on your script).

### What to look for
- How the server handles a single connection from `accept()` to `close()`.
- Clean shutdown when client exits.

---

## 2) `multiclients` — Multiple Clients (Iterative)
**Goal:** Allow many clients **one at a time** (no threads yet).

**Concept:**
- The server loops over `accept()` and serves one client to completion before handling the next.
- Useful for understanding blocking I/O and control flow.

### Run
```bash
cd multiclients
python server.py 
# Open 2–4 more terminals and start clients:
python client.py 
```

### What to look for
- When one client is being served, others must wait.
- Proper closing of client sockets so the next `accept()` can proceed.

**Tip:** If you need basic “broadcast”, the iterative version typically won’t broadcast; each client is handled in turn.

---

## 3) `multiclientsusingthreading` — Multiple Clients (Threaded)
**Goal:** Handle many clients **concurrently**.

**Concept:**
- Main thread: `bind()` + `listen()` + `accept()`.
- For each accepted client, spawn a **thread** that loops on `recv()` and responds.
- Optionally keep a shared list of connections to **broadcast** messages.

### Run
```bash
cd multiclientsusingthreading
python server.py 
# Start several clients in separate terminals:
python client.py 
```

### What to look for
- Per-client worker threads.
- Thread-safe broadcast (if implemented): on message from Client A, send to all others.
- Graceful cleanup: closing a client should end its thread without crashing the server.

**Safety notes:**
- Be mindful of shared data structures; use locks if you mutate a global client list.

---

## 4) `sandbox` — Experiments & Extras
**Goal:** A playground to try variations:
- Change message framing (line-based vs length-prefixed).
- Add simple “/nick” or “/quit” commands.
- Experiment with timeouts (`settimeout`) or non-blocking sockets.
- Swap `127.0.0.1` with your LAN IP to chat across machines on the same Wi-Fi.

### Run
```bash
cd sandbox
python server.py --host 127.0.0.1 --port 5003
python client.py --host 127.0.0.1 --port 5003
```

---

## Test on Local Network (LAN)
1. **Find your server machine’s IP**
   - Windows: `ipconfig` → look for `IPv4 Address` (e.g., `192.168.1.23`)
   - macOS/Linux: `ifconfig` or `ip addr`
2. Start the server with that IP:
   ```bash
   python server.py --host 192.168.1.23 --port 5000
   ```
3. On other devices on the same Wi-Fi:
   ```bash
   python client.py --host 192.168.1.23 --port 5000
   ```
4. If connection fails, see **Troubleshooting**.

---

## Troubleshooting
- **`Address already in use`**  
  Another server is bound to that port. Choose a new port or wait until the old socket releases (TIME_WAIT).
- **`Connection refused`**  
  Server not running, wrong IP/port, or firewall blocked.
- **Windows Defender / Firewall prompts**  
  Allow Python on **Private networks** (Block Public if you’re unsure).
- **App hangs waiting for data**  
  The other side didn’t send a newline/terminator your code expects, or you’re reading more bytes than sent.
- **Crash on client disconnect**  
  Handle `recv()` returning 0 bytes and catch exceptions around `sendall()`.

---

## Project Structure
```
socket_programming/
├─ basic/
│  ├─ server.py
│  └─ client.py
├─ multiclients/
│  ├─ server.py
│  └─ client.py
├─ multiclientsusingthreading/
│  ├─ server.py
│  └─ client.py
└─ sandbox/
   ├─ server.py
   └─ client.py
```
> If your filenames differ, keep the same idea: each folder has a server and a client script.

---


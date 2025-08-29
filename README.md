# 🧪 Socket Programming in Python — Four Mini-Projects

A hands-on collection of small socket-programming exercises in Python:
1) a **basic** single client/server echo,
2) a **multi-client** server (iterative),
3) a **multi-client** server using **threads**,
4) a **sandbox** for your experiments.

> Folders in this repo: `basic/`, `multiclients/`, `multiclientsusingthreading/`, `sandbox/`. Language: Python. :contentReference[oaicite:1]{index=1}

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
- [License](#license)

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

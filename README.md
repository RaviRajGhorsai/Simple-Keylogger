# Simple Keylogger

A lightweight and simple keylogger built in Python, using `pynput` to capture keystrokes and `smtplib` to send logs via email.

---

## 📋 Features

- Captures all keyboard input
- Writes keystrokes to a local `log.txt` file
- Sends captured logs to your email address periodically
- Lightweight and easy to use

---

## ⚙️ Setup Instructions

1. **Clone this repository:**

   ```bash
   git clone https://github.com/RaviRajGhorsai/Simple-Keylogger.git
   cd Simple-Keylogger
   ```

2. **Install the required library:**

   ```bash
   pip install pynput
   ```

3. **Configure your email settings:**
   
   - Open the Python script.
   - Replace the following placeholders:
     - `sender_email` with your Gmail address
     - `receiver_email` with the receiver's email address
     - `password` with your Gmail App Password (if you have 2FA enabled)

4. **Run the script:**

   ```bash
   python keylogger.py
   ```

---

## ⚠️ Legal Disclaimer

This tool is designed for **educational purposes only**.  
Unauthorized use of keyloggers to monitor devices without permission is illegal and unethical.  
Use it only on devices you own or have explicit permission to monitor.

---

## 🛠 Built With

- Python 3
- `pynput`
- `smtplib`
- `ssl`
- `threading`

---


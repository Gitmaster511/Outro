import os
import time
import playsound
from playsound import playsound
from threading import Thread


def sound():
    playsound('Outro.mp3')


def countdown():
    print("Locking in 10...")
    time.sleep(2)
    print("9...")
    time.sleep(2)
    print("8...")
    time.sleep(2)
    print("7...")
    time.sleep(2)
    print("6...")
    time.sleep(2)
    print("5...")
    time.sleep(2)
    print("4...")
    # dramatic effect
    time.sleep(3)
    print("3..")
    time.sleep(3)
    print("2..")
    time.sleep(3)
    print("1..")
    time.sleep(0.5)
    print("Goodbye")
    time.sleep(1.5)
    ctypes.windll.user32.LockWorkStation()


if os.getuid() != 0:
    print("run as root")
    exit(0)

elif __name__ == '__main__':
    Thread(target=countdown).start()
    Thread(target=sound).start()

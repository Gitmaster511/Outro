import os
import time
import playsound
from playsound import playsound
from threading import Thread


def sound():
    playsound('Outro.mp3')


def countdown():
    i = 10

    while i > 0:
        j = str(i)
        print("Shutting Down in " + j + "...")
        time.sleep(2.2)
        i = i - 1
    print("Goodbye :)")
    os.system("shutdown -h now")


if os.getuid() != 0:
    print("run as root")
    exit(0)

elif __name__ == '__main__':
    Thread(target=countdown).start()
    Thread(target=sound).start()

import os
import time
import playsound
from playsound import playsound
from threading import Thread


def sound():
    playsound('Outro.mp3')


def countdown():
    for i in range(10):
        print(f"Shutting Down in {10 - i}... ")
        time.sleep(2.2)
    print("Goodbye :)")
    os.system("shutdown /f")


if __name__ == '__main__':
    Thread(target=countdown).start()
    Thread(target=sound).start()

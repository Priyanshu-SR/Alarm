from time import time
from datetime import datetime
from pygame import mixer


def sounds(file, str):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(loops=-1)
    while True:
        a = input()
        if a == str:
            mixer.music.stop()
            break


def log_message(msg):
    with open("My Logs.txt", "a") as lm:
        lm.write(f"{msg}, {datetime.now()}\n")


if __name__ == '__main__':
    initial_water_time = time()
    initial_eyes_time = time()
    initial_exercise_time = time()
    water_sec = 5000
    eyes_sec = 15000
    exercise_sec = 22000
    while True:
        if time() - initial_water_time > water_sec:
            print(f"___DRINK WATER___\nTo stop this alarm enter 'Drank'")
            sounds("drink.mp3", "Drank")
            initial_water_time = time()
            log_message("I drank water at")
        if time() - initial_eyes_time > eyes_sec:
            print(f"___EXERCISE EYES___\nTo stop this alarm enter 'IExDone'")
            sounds("wake_up.mp3", "IExDone")
            initial_eyes_time = time()
            log_message("I did eyes exercise at")
        if time() - initial_exercise_time > exercise_sec:
            print(f"___EXERCISE BODY___\nTo stop this alarm enter 'ExDone'")
            sounds("do_it.mp3", "ExDone")
            initial_exercise_time = time()
            log_message("I did body exercise at")

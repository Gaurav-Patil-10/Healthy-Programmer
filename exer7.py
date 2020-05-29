import pygame
from pygame import mixer
import time
from time import time
import datetime

def logg(string,func_name):
    file_name =func_name+".txt"
    with open(file_name,"a+") as f:
        f.write(f"{string}  {func_name} at "+str(datetime.datetime.now())+"\n")


def water():
    mixer.init()
    mixer.music.load("water.mp3")
    mixer.music.play()
    while True:
        w=input()
        if w=="Drank" or w=="drank":
            pygame.mixer.music.stop()
            logg(w,"water")
            break
def eyes():
    mixer.init()
    mixer.music.load("eyes.mp3")
    mixer.music.play()
    while True:
        w=input()
        if w=="Done" or w=="done":
            pygame.mixer.music.stop()
            logg(w,"the eye relaxation")
            break
def physical():
    mixer.init()
    mixer.music.load("physical_exercise.mp3")
    mixer.music.play()
    while True:
        w=input()
        if w=="Done" or w=="done":
            pygame.mixer.music.stop()
            logg(w,"the physical exercise")
            break

if __name__ == "__main__":
    time_water = time()
    time_eyes = time()
    time_exercise = time()
    water_duration = 30*60
    eyes_duration = 35*60
    physical_duration = 45*60

    while True:
        if time() - time_water > water_duration:
            print("Have you drank the water ?")
            water()
            time_water = time()

        if time() - time_eyes > eyes_duration:
            print("Have you relaxed your eyes ?")
            eyes()
            time_eyes = time()

        if time() - time_exercise > physical_duration:
            print("Have you performed the physical exercise ?")
            physical()
            time_exercise = time()








            
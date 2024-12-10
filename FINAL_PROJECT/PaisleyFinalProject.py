
# find libraries and import
import pygame
import sys
import numpy as np
import ffmpeg
from pydub import AudioSegment;
from pydub.playback import play;
import pyaudio
import csv
import tkinter;
#import audioop_lts
pygame.init()

# get key press events
def input():
    
    note = ''
    while note == '':
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_g]:
            note = "C4"
        elif keys[pygame.K_h]:
            note = "D4"
        elif keys[pygame.K_j]:
            note = "E4"
        elif keys[pygame.K_k]:
            note = "F4"
        elif keys[pygame.K_l]:
            note = "G4"
        elif keys[pygame.K_SEMICOLON]:
            note = "A4"
        elif keys[pygame.K_m]:
            note = "B4"
        elif keys[pygame.K_COMMA]:
            note = "C5"
        elif keys[pygame.K_PERIOD]:
            note = "D5"
        elif keys[pygame.K_SLASH]:
            note = "E5"
        elif keys[pygame.K_f]:
            note = "B3"
        elif keys[pygame.K_d]:
            note = "A3"
        elif keys[pygame.K_s]:
            note = "G3"
        elif keys[pygame.K_a]:
            note = "F3"
        elif keys[pygame.K_c]:
            note = "E3"
        elif keys[pygame.K_x]:
            note = "D3"
        elif keys[pygame.K_z]:
            note = "C3"
        elif event.type == pygame.QUIT or keys[pygame.K_q]:
            running = False
            pygame.quit()
    return note



def generate_sine_wave(frequency, duration, sample_rate=44100, amplitude=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = amplitude * np.sin(2 * np.pi * float(frequency) * t)
    wave = np.int16(wave * 32767)
    return AudioSegment(
        wave.tobytes(),
        frame_rate=sample_rate,
        sample_width=wave.dtype.itemsize,
        channels=1
    )

def blit_image(screen, image, position, area=None):
    screen.blit(image, position, area)


 



# read file and create dictionary

f=open("C:/Users/paisl/OneDrive/Desktop/FINAL_PROJECT/files/notes.txt","r")

notesCSV=csv.DictReader(f)
myNotes={}

for row in notesCSV: 
    key = row['name']
    myNotes[key]={'freq':row['freq'],'posX':row['posX'],'posY':row['posY'],'picOff':row['picOff'],'picOn':row['picOn']}
print(myNotes) #test




    # images
leftOff = pygame.image.load("C:/Users/paisl/OneDrive/Desktop/FINAL_PROJECT/graphics/leftOff.jpeg") 
midOff = pygame.image.load("C:/Users/paisl/OneDrive/Desktop/FINAL_PROJECT/graphics/midOff.jpeg") 
rightOff = pygame.image.load("C:/Users/paisl/OneDrive/Desktop/FINAL_PROJECT/graphics/rightOff.jpeg") 
leftOn = pygame.image.load("C:/Users/paisl/OneDrive/Desktop/FINAL_PROJECT/graphics/leftOn.jpeg") 
midOn = pygame.image.load("C:/Users/paisl/OneDrive/Desktop/FINAL_PROJECT/graphics/midOn.jpeg") 
rightOn = pygame.image.load("C:/Users/paisl/OneDrive/Desktop/FINAL_PROJECT/graphics/rightOn.jpeg") 



# display
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Music Melody by Paisley")

print(type(myNotes))
# draw display
screen.fill((0,0,0))
for name in myNotes:
    myPOSX=int(myNotes[name]['posX'])
    myPOSY=int(myNotes[name]['posY'])
    print(myPOSX)
    imName="C:/Users/paisl/OneDrive/Desktop/FINAL_PROJECT/graphics/" +myNotes[name]['picOff']+".jpeg"
    myImage=pygame.image.load(imName) 
    blit_image(screen,myImage,(myPOSX,myPOSY))

# label the keys
# 
font = pygame.font.SysFont(None, 24)  
text_surface1 = font.render("z    x    c    a    s    d    f    g    h    j       k    l    ;     m    ,      .    /", True, (255, 255, 255)) 
text_surface2 = font.render("\'q\' to quit.", True, (255, 255, 255))
screen.blit(text_surface1, (310, 380))  
screen.blit(text_surface2,(310,270))
pygame.display.flip()



# main loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            getkey=input()
            if getkey in ("C3","D3","E3","F3","G3","A3","B3","C4","D4","E4","F4","G4","A4","B4","C5","D5","E5"):
                myPOSX=int(myNotes[getkey]['posX'])
                myPOSY=int(myNotes[getkey]['posY'])
                imName="C:/Users/paisl/OneDrive/Desktop/FINAL_PROJECT/graphics/" +myNotes[getkey]['picOn']+".jpeg"
                myImage=pygame.image.load(imName) 
                blit_image(screen,myImage,(myPOSX,myPOSY))
                pygame.display.flip()
                play(generate_sine_wave(myNotes[getkey]["freq"], .25))
                imName="C:/Users/paisl/OneDrive/Desktop/FINAL_PROJECT/graphics/" +myNotes[getkey]['picOff']+".jpeg"
                myImage=pygame.image.load(imName) 
                blit_image(screen,myImage,(myPOSX,myPOSY))
            else:
                continue

        pygame.display.flip()
             
        
#flip display
#pygame.display.flip()

# quit
pygame.quit()
sys.exit()
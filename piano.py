# Librairies imports
from tkinter import *
import pygame
import tkinter as tk
import time

# Initializing window
pygame.init()
window = tk.Tk()
window.title('Virtual Piano')
window.geometry('1080x900+0+0') # Dimensions of the window
window.configure(background='White')

# Different sections of the Windows grid
# Global grid (the one that encapsulates all the sub grids)
piano = Frame(window, bg='black', bd='15', relief='ridge')
piano.grid()

piano.pack(fill="both", expand=True, padx=20, pady=20)

# Grid 1: Top interface
interface = Frame(piano, bg='black', bd='15', relief='ridge')
interface.grid()

# Grid 2: Music Sheet
musicsheet = Frame(piano, bg='black', bd='15', relief='ridge')
musicsheet.grid()

# Grid 3: Piano Keys
pianokeys = Frame(piano, bg='white', bd='15', relief='ridge')
pianokeys.grid()

# Strings
title = StringVar()
title.set('Now playing: Name of the song')
timer = StringVar()
offset = StringVar()

# Update timer
def update_timer(timer):
    now = time.strftime("%H:%M:%S")
    timer.set(now)
    window.after(1, update_timer)

# Set timers
update_timer(timer)
offset.set(time.strftime("%H:%M:%S"))


# Changes based on which note is being pressed in the button actions
displayNote = StringVar()

# Buttons playing sound method
# P.S:keybind_(letter) corresponds to the keybind to the note in piano language
# Note: In python, you need to declare your methods first before implementing them inside your buttons

# Octave 1
def keybind_ShiftZ(event=None):
    displayNote.set('C')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\01.wav')
    sound.play()

def keybind_ShiftS(event=None):
    displayNote.set('C#')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\02.wav')
    sound.play()

def keybind_ShiftX(event=None):
    displayNote.set('D')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\03.wav')
    sound.play()

def keybind_ShiftD(event=None):
    displayNote.set('Eb')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\04.wav')
    sound.play()

def keybind_ShiftC(event=None):
    displayNote.set('E')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\05.wav')
    sound.play()
    
def keybind_ShiftV(event=None):
    displayNote.set('F')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\06.wav')
    sound.play()

def keybind_ShiftG(event=None):
    displayNote.set('F#')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\07.wav')
    sound.play()

def keybind_ShiftB(event=None):
    displayNote.set('G')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\08.wav')
    sound.play()
    
def keybind_ShiftH(event=None):
    displayNote.set('G#')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\09.wav')
    sound.play()

def keybind_ShiftN(event=None):
    displayNote.set('A')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\10.wav')
    sound.play()

def keybind_ShiftJ(event=None):
    displayNote.set('Bb')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\11.wav')
    sound.play()

def keybind_ShiftM(event=None):
    displayNote.set('B')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\12.wav')
    sound.play()

# Octave 2
def keybind_ShiftY(event=None):
    displayNote.set('C')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\13.wav')
    sound.play()

def keybind_Shift7(event=None):
    displayNote.set('C#')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\14.wav')
    sound.play()

def keybind_ShiftU(event=None):
    displayNote.set('D')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\15.wav')
    sound.play()

def keybind_Shift8(event=None):
    displayNote.set('Eb')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\16.wav')
    sound.play()

def keybind_ShiftI(event=None):
    displayNote.set('E')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\17.wav')
    sound.play()
    
def keybind_ShiftO(event=None):
    displayNote.set('F')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\18.wav')
    sound.play()

def keybind_Shift0(event=None):
    displayNote.set('F#')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\19.wav')
    sound.play()

def keybind_ShiftP(event=None):
    displayNote.set('G')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\20.wav')
    sound.play()
    
def keybind_Underscore(event=None):
    displayNote.set('G#')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\21.wav')
    sound.play()

def keybind_LeftBrace(event=None):
    displayNote.set('A')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\22.wav')
    sound.play()

def keybind_Plus(event=None):
    displayNote.set('Bb')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\23.wav')
    sound.play()

def keybind_RightBrace(event=None):
    displayNote.set('B')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\24.wav')
    sound.play()

# Octave 3
def keybind_Z(event=None):
    displayNote.set('C')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\25.wav')
    sound.play()

def keybind_S(event=None):
    displayNote.set('C#')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\26.wav')
    sound.play()

def keybind_X(event=None):
    displayNote.set('D')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\27.wav')
    sound.play()

def keybind_D(event=None):
    displayNote.set('Eb')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\28.wav')
    sound.play()

def keybind_C(event=None):
    displayNote.set('E')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\29.wav')
    sound.play()
    
def keybind_V(event=None):
    displayNote.set('F')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\30.wav')
    sound.play()

def keybind_G(event=None):
    displayNote.set('F#')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\31.wav')
    sound.play()

def keybind_B(event=None):
    displayNote.set('G')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\32.wav')
    sound.play()
    
def keybind_H(event=None):
    displayNote.set('G#')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\33.wav')
    sound.play()

def keybind_N(event=None):
    displayNote.set('A')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\34.wav')
    sound.play()

def keybind_J(event=None):
    displayNote.set('Bb')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\35.wav')
    sound.play()

def keybind_M(event=None):
    displayNote.set('B')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\36.wav')
    sound.play()

# Octave 4
def keybind_Y(event=None):
    displayNote.set('C')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\37.wav')
    sound.play()

def keybind_7(event=None):
    displayNote.set('C#')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\38.wav')
    sound.play()

def keybind_U(event=None):
    displayNote.set('D')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\39.wav')
    sound.play()

def keybind_8(event=None):
    displayNote.set('Eb')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\40.wav')
    sound.play()

def keybind_I(event=None):
    displayNote.set('E')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\41.wav')
    sound.play()
    
def keybind_O(event=None):
    displayNote.set('F')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\42.wav')
    sound.play()

def keybind_0(event=None):
    displayNote.set('F#')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\43.wav')
    sound.play()

def keybind_P(event=None):
    displayNote.set('G')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\44.wav')
    sound.play()
    
def keybind_Minus(event=None):
    displayNote.set('G#')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\45.wav')
    sound.play()

def keybind_LeftBracket(event=None):
    displayNote.set('A')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\46.wav')
    sound.play()

def keybind_Equal(event=None):
    displayNote.set('Bb')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\47.wav')
    sound.play()

def keybind_RightBracket(event=None):
    displayNote.set('B')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\48.wav')
    sound.play()

# Octave 5
def keybind_CtrlZ(event=None):
    displayNote.set('C')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\49.wav')
    sound.play()

def keybind_CtrlS(event=None):
    displayNote.set('C#')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\50.wav')
    sound.play()

def keybind_CtrlX(event=None):
    displayNote.set('D')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\51.wav')
    sound.play()

def keybind_CtrlD(event=None):
    displayNote.set('Eb')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\52.wav')
    sound.play()

def keybind_CtrlC(event=None):
    displayNote.set('E')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\53.wav')
    sound.play()
    
def keybind_CtrlV(event=None):
    displayNote.set('F')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\54.wav')
    sound.play()

def keybind_CtrlG(event=None):
    displayNote.set('F#')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\55.wav')
    sound.play()

def keybind_CtrlB(event=None):
    displayNote.set('G')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\56.wav')
    sound.play()
    
def keybind_CtrlH(event=None):
    displayNote.set('G#')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\57.wav')
    sound.play()

def keybind_CtrlN(event=None):
    displayNote.set('A')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\58.wav')
    sound.play()

def keybind_CtrlJ(event=None):
    displayNote.set('Bb')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\59.wav')
    sound.play()

def keybind_CtrlM(event=None):
    displayNote.set('B')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\60.wav')
    sound.play()

# Octave 6
def keybind_CtrlY(event=None):
    displayNote.set('C')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\61.wav')
    sound.play()

def keybind_Ctrl7(event=None):
    displayNote.set('C#')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\62.wav')
    sound.play()

def keybind_CtrlU(event=None):
    displayNote.set('D')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\63.wav')
    sound.play()

def keybind_Ctrl8(event=None):
    displayNote.set('Eb')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\64.wav')
    sound.play()

def keybind_CtrlI(event=None):
    displayNote.set('E')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\Extra1.wav')
    sound.play()
    
def keybind_CtrlO(event=None):
    displayNote.set('F')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\Extra2.wav')
    sound.play()

def keybind_Ctrl0(event=None):
    displayNote.set('F#')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\Extra3.wav')
    sound.play()

def keybind_CtrlP(event=None):
    displayNote.set('G')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\Extra.wav')
    sound.play()
    
def keybind_CtrlMinus(event=None):
    displayNote.set('G#')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\Missing_file.wav')
    sound.play()

def keybind_CtrlLeftBracket(event=None):
    displayNote.set('A')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\Missing_file.wav')
    sound.play()

def keybind_CtrlEqual(event=None):
    displayNote.set('Bb')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\Missing_file.wav')
    sound.play()

def keybind_CtrlRightBracket(event=None):
    displayNote.set('B')
    sound = pygame.mixer.Sound(r'C:\Users\light\Desktop\Python Piano\Piano_Notes\Missing_file.wav')
    sound.play()

# Label with title for grid 1 (interface) 
Label(interface, textvariable=title, font=('arial',25,'bold'),padx=4 ,pady=4, bd=4, bg='black',
fg='white', justify=CENTER).grid(row=0, column=0, columnspan=11) # 12 keys in an octave

# Textbox for grid 1 (interface)
txtTimer = Label(interface, textvariable=timer, font=('arial',16,'bold'), bg='black', fg='white', width=25, justify=CENTER)
txtTimer.grid(row=1, column=0, pady=1)

txtTitle = Entry(interface, textvariable=displayNote, font=('arial',16,'bold'), bg='black', fg='white', width=25, justify=CENTER)
txtTitle.grid(row=1, column=1, pady=1)

txtOffset = Entry(interface, textvariable=offset, font=('arial',16,'bold'), bg='black', fg='white', width=25, justify=CENTER)
txtOffset.grid(row=1, column=2, pady=1)

# Select Music Sheet Button for grid 2 (music sheet (WIP))
btnSelect = Button(musicsheet, width=25, height=2, bd=4, text='Select music sheet', font=('arial',12,'bold'), bg='white', fg='black')
btnSelect.grid(row=0, column=0, padx=5, pady=5)

# Buttons for grid 3 (pianokeys) P.S:Command(letter) = keybind to the note in text

# Octave 1
btnShiftZ = Button(pianokeys, width=4, height=18, bd=4, text='C', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_ShiftZ)
btnShiftZ.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
btnShiftS = Button(pianokeys, width=2, height=6, bd=4, text='C#', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_ShiftS)
btnShiftS.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
btnShiftX = Button(pianokeys, width=4, height=18, bd=4, text='D', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_ShiftX)
btnShiftX.grid(row=1, column=2, columnspan=2, padx=5, pady=5)
btnShiftD = Button(pianokeys, width=2, height=6, bd=4, text='Eb', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_ShiftD)
btnShiftD.grid(row=0, column=3, columnspan=2, padx=5, pady=5)
btnShiftC = Button(pianokeys, width=4, height=18, bd=4, text='E', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_ShiftC)
btnShiftC.grid(row=1, column=4, padx=5, pady=5)

btnShiftV = Button(pianokeys, width=4, height=18, bd=4, text='F', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_ShiftV)
btnShiftV.grid(row=1, column=5, columnspan=2, padx=5, pady=5)
btnShiftG = Button(pianokeys, width=2, height=6, bd=4, text='F#', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_ShiftG)
btnShiftG.grid(row=0, column=6, columnspan=2, padx=5, pady=5)
btnShiftB = Button(pianokeys, width=4, height=18, bd=4, text='G', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_ShiftB)
btnShiftB.grid(row=1, column=7, columnspan=2, padx=5, pady=5)
btnShiftH = Button(pianokeys, width=2, height=6, bd=4, text='G#', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_ShiftH)
btnShiftH.grid(row=0, column=8, columnspan=2, padx=5, pady=5)
btnShiftN = Button(pianokeys, width=4, height=18, bd=4, text='A', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_ShiftN)
btnShiftN.grid(row=1, column=9, columnspan=2, padx=5, pady=5)
btnShiftJ = Button(pianokeys, width=2, height=6, bd=4, text='Bb', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_ShiftJ)
btnShiftJ.grid(row=0, column=10, columnspan=2, padx=5, pady=5)
btnShiftM = Button(pianokeys, width=4, height=18, bd=4, text='B', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_ShiftM)
btnShiftM.grid(row=1, column=11, padx=5, pady=5)

# Octave 2
btnShiftY = Button(pianokeys, width=4, height=18, bd=4, text='C', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_ShiftY)
btnShiftY.grid(row=1, column=12, columnspan=2, padx=5, pady=5)
btnShift7 = Button(pianokeys, width=2, height=6, bd=4, text='C#', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_Shift7)
btnShift7.grid(row=0, column=13, columnspan=2, padx=5, pady=5)
btnShiftU = Button(pianokeys, width=4, height=18, bd=4, text='D', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_ShiftU)
btnShiftU.grid(row=1, column=14, columnspan=2, padx=5, pady=5)
btnShift8 = Button(pianokeys, width=2, height=6, bd=4, text='Eb', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_Shift8)
btnShift8.grid(row=0, column=15, columnspan=2, padx=5, pady=5)
btnShiftI = Button(pianokeys, width=4, height=18, bd=4, text='E', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_ShiftI)
btnShiftI.grid(row=1, column=16, padx=5, pady=5)

btnShiftO = Button(pianokeys, width=4, height=18, bd=4, text='F', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_ShiftO)
btnShiftO.grid(row=1, column=17, columnspan=2, padx=5, pady=5)
btnShift0 = Button(pianokeys, width=2, height=6, bd=4, text='F#', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_Shift0)
btnShift0.grid(row=0, column=18, columnspan=2, padx=5, pady=5)
btnShiftP = Button(pianokeys, width=4, height=18, bd=4, text='G', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_ShiftP)
btnShiftP.grid(row=1, column=19, columnspan=2, padx=5, pady=5)
btnUnderscore = Button(pianokeys, width=2, height=6, bd=4, text='G#', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_Underscore)
btnUnderscore.grid(row=0, column=20, columnspan=2, padx=5, pady=5)
btnLeftBrace = Button(pianokeys, width=4, height=18, bd=4, text='A', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_LeftBrace)
btnLeftBrace.grid(row=1, column=21, columnspan=2, padx=5, pady=5)
btnPlus = Button(pianokeys, width=2, height=6, bd=4, text='Bb', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_Plus)
btnPlus.grid(row=0, column=22, columnspan=2, padx=5, pady=5)
btnRightBrace = Button(pianokeys, width=4, height=18, bd=4, text='B', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_RightBrace)
btnRightBrace.grid(row=1, column=23, padx=5, pady=5)

# Octave 3
btnZ = Button(pianokeys, width=4, height=18, bd=4, text='C', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_Z)
btnZ.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
btnS = Button(pianokeys, width=2, height=6, bd=4, text='C#', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_S)
btnS.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
btnX = Button(pianokeys, width=4, height=18, bd=4, text='D', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_X)
btnX.grid(row=1, column=2, columnspan=2, padx=5, pady=5)
btnD = Button(pianokeys, width=2, height=6, bd=4, text='Eb', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_D)
btnD.grid(row=0, column=3, columnspan=2, padx=5, pady=5)
btnC = Button(pianokeys, width=4, height=18, bd=4, text='E', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_C)
btnC.grid(row=1, column=4, padx=5, pady=5)

btnV = Button(pianokeys, width=4, height=18, bd=4, text='F', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_V)
btnV.grid(row=1, column=5, columnspan=2, padx=5, pady=5)
btnG = Button(pianokeys, width=2, height=6, bd=4, text='F#', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_G)
btnG.grid(row=0, column=6, columnspan=2, padx=5, pady=5)
btnB = Button(pianokeys, width=4, height=18, bd=4, text='G', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_B)
btnB.grid(row=1, column=7, columnspan=2, padx=5, pady=5)
btnH = Button(pianokeys, width=2, height=6, bd=4, text='G#', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_H)
btnH.grid(row=0, column=8, columnspan=2, padx=5, pady=5)
btnN = Button(pianokeys, width=4, height=18, bd=4, text='A', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_N)
btnN.grid(row=1, column=9, columnspan=2, padx=5, pady=5)
btnJ = Button(pianokeys, width=2, height=6, bd=4, text='Bb', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_J)
btnJ.grid(row=0, column=10, columnspan=2, padx=5, pady=5)
btnM = Button(pianokeys, width=4, height=18, bd=4, text='B', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_M)
btnM.grid(row=1, column=11, padx=5, pady=5)

# Octave 4
btnY = Button(pianokeys, width=4, height=18, bd=4, text='C', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_Y)
btnY.grid(row=1, column=12, columnspan=2, padx=5, pady=5)
btn7 = Button(pianokeys, width=2, height=6, bd=4, text='C#', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_7)
btn7.grid(row=0, column=13, columnspan=2, padx=5, pady=5)
btnU = Button(pianokeys, width=4, height=18, bd=4, text='D', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_U)
btnU.grid(row=1, column=14, columnspan=2, padx=5, pady=5)
btn8 = Button(pianokeys, width=2, height=6, bd=4, text='Eb', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_8)
btn8.grid(row=0, column=15, columnspan=2, padx=5, pady=5)
btnI = Button(pianokeys, width=4, height=18, bd=4, text='E', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_I)
btnI.grid(row=1, column=16, padx=5, pady=5)

btnO = Button(pianokeys, width=4, height=18, bd=4, text='F', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_O)
btnO.grid(row=1, column=17, columnspan=2, padx=5, pady=5)
btn0 = Button(pianokeys, width=2, height=6, bd=4, text='F#', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_0)
btn0.grid(row=0, column=18, columnspan=2, padx=5, pady=5)
btnP = Button(pianokeys, width=4, height=18, bd=4, text='G', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_P)
btnP.grid(row=1, column=19, columnspan=2, padx=5, pady=5)
btnMinus = Button(pianokeys, width=2, height=6, bd=4, text='G#', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_Minus)
btnMinus.grid(row=0, column=20, columnspan=2, padx=5, pady=5)
btnLeftBracket = Button(pianokeys, width=4, height=18, bd=4, text='A', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_LeftBracket)
btnLeftBracket.grid(row=1, column=21, columnspan=2, padx=5, pady=5)
btnEqual = Button(pianokeys, width=2, height=6, bd=4, text='Bb', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_Equal)
btnEqual.grid(row=0, column=22, columnspan=2, padx=5, pady=5)
btnRightBracket = Button(pianokeys, width=4, height=18, bd=4, text='B', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_RightBracket)
btnRightBracket.grid(row=1, column=23, padx=5, pady=5)

# Octave 5
btnCtrlZ = Button(pianokeys, width=4, height=18, bd=4, text='C', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_CtrlZ)
btnCtrlZ.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
btnCtrlS = Button(pianokeys, width=2, height=6, bd=4, text='C#', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_CtrlS)
btnCtrlS.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
btnCtrlX = Button(pianokeys, width=4, height=18, bd=4, text='D', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_CtrlX)
btnCtrlX.grid(row=1, column=2, columnspan=2, padx=5, pady=5)
btnCtrlD = Button(pianokeys, width=2, height=6, bd=4, text='Eb', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_CtrlD)
btnCtrlD.grid(row=0, column=3, columnspan=2, padx=5, pady=5)
btnCtrlC = Button(pianokeys, width=4, height=18, bd=4, text='E', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_CtrlC)
btnCtrlC.grid(row=1, column=4, padx=5, pady=5)

btnCtrlV = Button(pianokeys, width=4, height=18, bd=4, text='F', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_CtrlV)
btnCtrlV.grid(row=1, column=5, columnspan=2, padx=5, pady=5)
btnCtrlG = Button(pianokeys, width=2, height=6, bd=4, text='F#', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_CtrlG)
btnCtrlG.grid(row=0, column=6, columnspan=2, padx=5, pady=5)
btnCtrlB = Button(pianokeys, width=4, height=18, bd=4, text='G', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_CtrlB)
btnCtrlB.grid(row=1, column=7, columnspan=2, padx=5, pady=5)
btnCtrlH = Button(pianokeys, width=2, height=6, bd=4, text='G#', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_CtrlH)
btnCtrlH.grid(row=0, column=8, columnspan=2, padx=5, pady=5)
btnCtrlN = Button(pianokeys, width=4, height=18, bd=4, text='A', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_CtrlN)
btnCtrlN.grid(row=1, column=9, columnspan=2, padx=5, pady=5)
btnCtrlJ = Button(pianokeys, width=2, height=6, bd=4, text='Bb', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_CtrlJ)
btnCtrlJ.grid(row=0, column=10, columnspan=2, padx=5, pady=5)
btnCtrlM = Button(pianokeys, width=4, height=18, bd=4, text='B', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_CtrlM)
btnCtrlM.grid(row=1, column=11, padx=5, pady=5)

# Octave 6
btnCtrlY = Button(pianokeys, width=4, height=18, bd=4, text='C', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_CtrlY)
btnCtrlY.grid(row=1, column=12, columnspan=2, padx=5, pady=5)
btnCtrl7 = Button(pianokeys, width=2, height=6, bd=4, text='C#', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_Ctrl7)
btnCtrl7.grid(row=0, column=13, columnspan=2, padx=5, pady=5)
btnCtrlU = Button(pianokeys, width=4, height=18, bd=4, text='D', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_CtrlU)
btnCtrlU.grid(row=1, column=14, columnspan=2, padx=5, pady=5)
btnCtrl8 = Button(pianokeys, width=2, height=6, bd=4, text='Eb', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_Ctrl8)
btnCtrl8.grid(row=0, column=15, columnspan=2, padx=5, pady=5)
btnCtrlI = Button(pianokeys, width=4, height=18, bd=4, text='E', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_CtrlI)
btnCtrlI.grid(row=1, column=16, padx=5, pady=5)

btnCtrlO = Button(pianokeys, width=4, height=18, bd=4, text='F', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_CtrlO)
btnCtrlO.grid(row=1, column=17, columnspan=2, padx=5, pady=5)
btnCtrl0 = Button(pianokeys, width=2, height=6, bd=4, text='F#', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_Ctrl0)
btnCtrl0.grid(row=0, column=18, columnspan=2, padx=5, pady=5)
btnCtrlP = Button(pianokeys, width=4, height=18, bd=4, text='G', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_CtrlP)
btnCtrlP.grid(row=1, column=19, columnspan=2, padx=5, pady=5)
btnCtrlMinus = Button(pianokeys, width=2, height=6, bd=4, text='G#', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_CtrlMinus)
btnCtrlMinus.grid(row=0, column=20, columnspan=2, padx=5, pady=5)
btnCtrlLeftBracket = Button(pianokeys, width=4, height=18, bd=4, text='A', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_CtrlLeftBracket)
btnCtrlLeftBracket.grid(row=1, column=21, columnspan=2, padx=5, pady=5)
btnCtrlEqual = Button(pianokeys, width=2, height=6, bd=4, text='Bb', font=('arial',12,'bold'), bg='black', fg='white', command=keybind_CtrlEqual)
btnCtrlEqual.grid(row=0, column=22, columnspan=2, padx=5, pady=5)
btnCtrlRightBracket = Button(pianokeys, width=4, height=18, bd=4, text='B', font=('arial',12,'bold'), bg='white', fg='black', command=keybind_CtrlRightBracket)
btnCtrlRightBracket.grid(row=1, column=23, padx=5, pady=5)

# Binding keybindings to command

# Octave 1
window.bind('Z', keybind_ShiftZ)
window.bind('S', keybind_ShiftS)
window.bind('X', keybind_ShiftX)
window.bind('D', keybind_ShiftD)
window.bind('C', keybind_ShiftC)
window.bind('V', keybind_ShiftV)
window.bind('G', keybind_ShiftG)
window.bind('B', keybind_ShiftB)
window.bind('H', keybind_ShiftH)
window.bind('N', keybind_ShiftN)
window.bind('J', keybind_ShiftJ)
window.bind('M', keybind_ShiftM)

# Octave 2
window.bind('Y', keybind_ShiftY)
window.bind('&', keybind_Shift7)
window.bind('U', keybind_ShiftU)
window.bind('*', keybind_Shift8)
window.bind('I', keybind_ShiftI)
window.bind('O', keybind_ShiftO)
window.bind(')', keybind_Shift0)
window.bind('P', keybind_ShiftP)
window.bind('_', keybind_Underscore)
window.bind('{', keybind_LeftBrace)
window.bind('+', keybind_Plus)
window.bind('}', keybind_RightBrace)

# Octave 3
window.bind('z', keybind_Z)
window.bind('s', keybind_S)
window.bind('x', keybind_X)
window.bind('d', keybind_D)
window.bind('c', keybind_C)
window.bind('v', keybind_V)
window.bind('g', keybind_G)
window.bind('b', keybind_B)
window.bind('h', keybind_H)
window.bind('n', keybind_N)
window.bind('j', keybind_J)
window.bind('m', keybind_M)

# Octave 4
window.bind('y', keybind_Y)
window.bind('7', keybind_7)
window.bind('u', keybind_U)
window.bind('8', keybind_8)
window.bind('i', keybind_I)
window.bind('o', keybind_O)
window.bind('0', keybind_0)
window.bind('p', keybind_P)
window.bind('-', keybind_Minus)
window.bind('[', keybind_LeftBracket)
window.bind('=', keybind_Equal)
window.bind(']', keybind_RightBracket)

# Octave 5
window.bind('<Control-z>', keybind_CtrlZ)
window.bind('<Control-s>', keybind_CtrlS)
window.bind('<Control-x>', keybind_CtrlX)
window.bind('<Control-d>', keybind_CtrlD)
window.bind('<Control-c>', keybind_CtrlC)
window.bind('<Control-v>', keybind_CtrlV)
window.bind('<Control-g>', keybind_CtrlG)
window.bind('<Control-b>', keybind_CtrlB)
window.bind('<Control-h>', keybind_CtrlH)
window.bind('<Control-n>', keybind_CtrlN)
window.bind('<Control-j>', keybind_CtrlJ)
window.bind('<Control-m>', keybind_CtrlM)

# Octave 6
window.bind('<Control-y>', keybind_CtrlY)
window.bind('<Control-7>', keybind_Ctrl7)
window.bind('<Control-u>', keybind_CtrlU)
window.bind('<Control-8>', keybind_Ctrl8)
window.bind('<Control-i>', keybind_CtrlI)
window.bind('<Control-o>', keybind_CtrlO)
window.bind('<Control-0>', keybind_Ctrl0)
window.bind('<Control-p>', keybind_CtrlP)
window.bind('<Control-minus>', keybind_CtrlMinus)
window.bind('<Control-[>', keybind_CtrlLeftBracket)
window.bind('<Control-=>', keybind_CtrlEqual)
window.bind('<Control-]>', keybind_CtrlRightBracket)

# End of program
window.mainloop() 
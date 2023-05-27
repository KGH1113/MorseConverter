import alphabets_numbers
from playsound import playsound
import time

def Eng2Morse():
    Eng = input().lower()
    length = len(Eng)
    Englist = []

    for i in range(length):
        Englist.append(Eng[i])
    
    for word in Englist:
        if word == "":
            continue
        elif word == "a":
            alphabets_numbers.alphabets.a()
        elif word == "b":
            alphabets_numbers.alphabets.b()
        elif word == "c":
            alphabets_numbers.alphabets.c()
        elif word == "d":
            alphabets_numbers.alphabets.d()
        elif word == "e":
            alphabets_numbers.alphabets.e()
        elif word == "f":
            alphabets_numbers.alphabets.f()
        elif word == "g":
            alphabets_numbers.alphabets.g()
        elif word == "h":
            alphabets_numbers.alphabets.h()
        elif word == "i":
            alphabets_numbers.alphabets.i()
        elif word == "j":
            alphabets_numbers.alphabets.j()
        elif word == "k":
            alphabets_numbers.alphabets.k()
        elif word == "l":
            alphabets_numbers.alphabets.l()
        elif word == "m":
            alphabets_numbers.alphabets.m()
        elif word == "n":
            alphabets_numbers.alphabets.n()
        elif word == "o":
            alphabets_numbers.alphabets.o()
        elif word == "p":
            alphabets_numbers.alphabets.p()
        elif word == "q":
            alphabets_numbers.alphabets.q()
        elif word == "r":
            alphabets_numbers.alphabets.r()
        elif word == "s":
            alphabets_numbers.alphabets.s()
        elif word == "t":
            alphabets_numbers.alphabets.t()
        elif word == "u":
            alphabets_numbers.alphabets.u()
        elif word == "v":
            alphabets_numbers.alphabets.v()
        elif word == "w":
            alphabets_numbers.alphabets.w()
        elif word == "x":
            alphabets_numbers.alphabets.x()
        elif word == "y":
            alphabets_numbers.alphabets.y()
        elif word == "z":
            alphabets_numbers.alphabets.z()
    

    return alphabets_numbers.result
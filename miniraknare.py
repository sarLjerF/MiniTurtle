import math as M
import matplotlib.pyplot as graf
import re
import numpy as np

def addera (t1,t2):
    return (t1+t2)

def subtrahera (t1,t2):
    return (t1-t2)

def multiplisera (t1,t2):
    return (t1*t2)

def dividera (t1,t2):
    return (t1/t2)

def to_the_power_of_(t1,t2):
    return (t1**t2)
    

def equTolk(ecuation):
    ecuationlist = (re.split(" ",ecuation))
    try:
        tal1 = (int(ecuationlist[0]))
        opperator = ecuationlist[1]
        tal2 = (int(ecuationlist[2]))
        return tal1, tal2, opperator
    except: 
        print("Du skrev fel")
        return 0, "+", 0

def solve(equ,i):
    #IIIIIIIIIIIINNNNNNNNNNNNNNNNNNNNNTTTTTTTTTTTTTTTTTTEEEEEEEEEEEEEEEEEEE klar
    
    pass


def Desmos2_0():
    y = []    
    equ = input("Ekvation med syntax, x + c")
    if equ == 1:
        for i in range(10):
            y.append(to_the_power_of_(equ,i))
    
    graf.plot(y)
    graf.show()
    pass
# IIIIIIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNTEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE klar



run = True
while run:
    choice = input("Grafritare(0) eller Räknare(1)")

    if choice == "0":
        Desmos2_0()     


    if choice == "1":
        equation = input("""
            Bästa Miniräknaren / Desoms 2.0
        Skriv funktion  i formen Tal Opperator Tal ---> """)
        t1, t2, op = equTolk(equation)
        cs = True
        if op == "+":
            a = addera(t1,t2)
        elif op == "-":
            a = subtrahera(t1,t2)
        elif op == "*":
            a = multiplisera(t1,t2)
        elif op == "/":
            a = dividera(t1,t2)
        else:
            cs = False
            a = "ajabaja"
        if cs:
            print("Svaret blir")
        print(a)

    else:
        #Felhantering
        pass
    
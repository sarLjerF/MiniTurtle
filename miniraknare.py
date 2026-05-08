import math as M
import matplotlib.pyplot as graf
import re
import numpy as np
import cmath as cM

def felhantering():
    print("Felhantering")

def addera (t1,t2):
    return (int(t1)+int(t2))

def subtrahera (t1,t2):
    return (int(t1)-int(t2))

def multiplisera (t1,t2):
    return (int(t1)*int(t2))

def dividera (t1,t2):
    return (int(t1)/int(t2))

def to_the_power_of_(t1,t2):
    return (int(t1)**int(t2))
    

def equTolk(ecuation):
    ecuationlist = (re.split(" ",ecuation))
    try:
        tal1 = (int(ecuationlist[0]))
        opperator = ecuationlist[1]
        tal2 = (int(ecuationlist[2]))
        return tal1, tal2, opperator
    except: 
        felhantering()
        return 0, "+", 0

def graflister(equ):
    equation = []

    for i in range(12):
        x2 = to_the_power_of_(i,2)
        x = multiplisera(i,equ[3])

        if equ[2] == "+" and equ[5] == "+":
            equation.append(int(equ[0]) * x2 + x + int(equ[3]))
        elif equ[2] == "+" and equ[5] == "-":
            equation.append(int(equ[0]) * x2 + x - int(equ[3]))  
        elif equ[2] == "-" and equ[5] == "+":
            equation.append(int(equ[0]) * x2 - x + int(equ[3]))  
        elif equ[2] == "-" and equ[5] == "-":
            equation.append(int(equ[0]) * x2 - x - int(equ[3]))  
        else:
            felhantering()  
    return equation

def solve(equ,i):
    
    
    
    #IIIIIIIIIIIINNNNNNNNNNNNNNNNNNNNNTTTTTTTTTTTTTTTTTTEEEEEEEEEEEEEEEEEEE klar
    
    pass


def Desmos2_0():
     
    equ = input("Ekvation med syntax, 'a x^2 + b x + c' ==> ")
    try:
        ecuationlist = (re.split(" ",equ)) 
    except:
        felhantering()  
    
    ylis = graflister(ecuationlist)
    print (ylis)

    graf.plot(ylis)
    graf.show()
    #                                                                             FörFina grafen härnågonstands

def miniraknaren():
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
   
run = True
while run:
    choice = input("Grafritare(0) eller Räknare(1)")

    if choice == "0":
        Desmos2_0()     


    if choice == "1":
        miniraknaren()

    if choice == "2":
        # Söka nollställen
        pass

    else:
        #Felhantering
        pass
    
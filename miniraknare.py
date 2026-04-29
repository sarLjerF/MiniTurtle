import math as M
import matplotlib as graf
import re




def addera (t1,t2):
    return (t1+t2)

def subtrahera (t1,t2):
    return (t1-t2)

def multiplisera (t1,t2):
    return (t1*t2)

def dividera (t1,t2):
    return (t1/t2)
    


def equTolk(ecuation):
    ecuationlist = (re.split(" ",ecuation))
    #for i in range (len(ecuationlist)):

    tal1 = (int(ecuationlist[0]))
    opperator = ecuationlist[1]
    tal2 = (int(ecuationlist[2]))

    return tal1, tal2, opperator


# Tal opperator Tal
run = True
while run:

    choice = input("Grafritare(0) eller Räknare(1)")

    # if choice == "0":
    #     pass


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
    
    
    
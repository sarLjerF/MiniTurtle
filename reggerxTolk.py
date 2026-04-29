import re
def equTolk(ecuation):
    ecuationlist = (re.split(" ",ecuation))
    #for i in range (len(ecuationlist)):

    tal1 = (int(ecuationlist[0]))
    opperator = ecuationlist[1]
    tal2 = (int(ecuationlist[2]))

    return tal1, tal2, opperator
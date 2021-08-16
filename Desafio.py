#Variables
num_2 = ["a", "b", "c"]
num_3 = ["d", "e", "f"]
num_4 = ["g", "h", "i"]
num_5 = ["j", "k", "l"]
num_6 = ["m", "n", "o", "ñ"]
num_7 = ["p", "q", "r","s"]
num_8 = ["t", "u", "v"]
num_9 = ["w", "x", "y", "z"]
num_0 = [" ", "+"]


cad = input("Ingresa una cadena de caracteres: ")


def Con_Cal(e, y, var):         #Fucion
        if e==var[0]:
            proba  = y          
        elif e==var[1]:
            proba = y * 2        
        elif e==var[2]:
            proba = y * 3
        else:
            proba = y * 4
        return proba

for i in cad:                  #Bucle
    cal= ""
    x = ""
    if i in num_2:             #Numero 2
        x="2"
        cal = Con_Cal(i, x, num_2)

    if i in (num_3):          #Numero 3
       x="3"
       cal = Con_Cal(i, x, num_3)

    if i in (num_4):          #Numero 4
        x="4"
        cal = Con_Cal(i, x, num_4)

    if i in (num_5):          #Numero 5
        x="5"
        cal = Con_Cal(i, x, num_5)

    if i in (num_6):          #Numero 6
        x="6"
        cal = Con_Cal(i, x, num_6)   

    if i in (num_7):          #Numero 7
        x="7"
        cal = Con_Cal(i, x, num_7)

    if i in (num_8):          #Numero 8
        x="8"
        cal = Con_Cal(i, x, num_8)

    if i in (num_9):          #Numero 9
        x="9"
        cal = Con_Cal(i, x, num_9)   

    if i in (num_0):          #Numero 0
            x="0"
            cal = Con_Cal(i, x, num_0)   
            
    print (cal, end= " ") 
 

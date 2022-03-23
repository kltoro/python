#!/usr/bin/env python3


# Feladat: írjunk egy olyan eljárást, mely kap egy 8 elemű listát, s 
# ez alapján megrajzolja a sakktáblát. Például ha a bemenet [7,3,0,2,5,1,6,4] 
# Ennek jelentése: az 1. oszlopban a királynő alulról a 8. sorban van, a 2. oszlopban alulról
# a 4. sorban, stb. 


def printLines():
    print("+","-"*16,"+")

def printtabla(li):
    if len(li) != 8:
        print("Hiba: nem 8 elemű a lista!")
        return
    else:
        printLines()
        
        sor = 7
        while sor >= 0:
            print("|", end = " ")
            oszlop = 0
            while oszlop < 8:
                if li[oszlop] == sor:
                    print("Q", end = " ")
                else:
                    print(".", end = " ")
                oszlop += 1
            print("|")
            sor -= 1
            
        printLines()

def main():
    
    li = [7,3,0,2,5,1,6,4]
    print("Lista:", end= " ")
    print(li)
    printtabla(li)
    
    print("Lista:", end= " ")
    li = [0,4,7,5,2,6,1,3]
    print(li)
    printtabla(li)

main()

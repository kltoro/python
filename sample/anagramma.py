#!/usr/bin/env python3

# feladat: döntsük el két paraméterként megadott 
# stringről , hogy anagramma-e

def normalize(s):
    return s.lower().replace(" ","")
    
#halmazzal
def isAnagramma(s1,s2):
    return set(normalize(s1))==set(normalize(s2))

#for ciklussal
#def isAnagramma(s1,s2):
#    for c in normalize(s1):
#        if c not in normalize(s2):
#            return False
#    return True

def main():
    s1 = "Clint Eastwood"
    s2 = "Old West Action"
    
    print(s1 + " anagrammája-e " + s2 + " ?", end = " ")
    if isAnagramma(s1,s2):
        print("Igen")
    else:
        print("Nem")
    

if __name__ == '__main__':
    main()

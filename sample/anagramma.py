#!/usr/bin/env python3

# feladat: döntsük el két paraméterként megadott 
# stringről , hogy anagramma-e

def normalize(s):
    return s.lower().replace(" ","")
    
def isAnagramma(s1,s2):
    li = list(normalize(s1))
    for c in normalize(s2):
        if c in li:
            li.remove(c)
    
    if len(li) == 0:
        return True
    return False        


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

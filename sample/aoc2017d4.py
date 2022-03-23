#!/usr/bin/env python3

# AdventOfCode 2017 Day4 
# A new system policy has been put in place that requires all accounts to 
# use a passphrase instead of simply a password. A passphrase consists of 
# a series of words (lowercase letters) separated by spaces.To ensure 
# security, a valid passphrase must contain no duplicate words

def readInFile(s1):
    myinput = open(s1,"r")
    li = myinput.readlines()
    
    return li

def isPassphraseValid(passphrase):
    
    pieces = passphrase.replace("\n","").split()
    
    if len(set(pieces)) == len(pieces):
        return True
    return False

def main():
    inputfile = readInFile("hazinput.txt")
    
    howmanyvalid = 0    
    
    for passphrase in inputfile:
        if isPassphraseValid(passphrase):
            howmanyvalid += 1
            
    print(str(howmanyvalid) + " db jelmondat helyes")

if __name__ == '__main__':
    main()
from os import chdir
chdir('/mnt/c/Users/axel1/Desktop/kod/GitHub/Advent-of-Code-2020/Day4')
file = open("input.txt","r").readlines()
keyListe = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
tempKey = keyListe.copy()
nbPass = 0
for i in range(len(file)):
    if(file[i] == "\n"):
        print("test if", tempKey)
        if(len(tempKey) == 0 or (len(tempKey) == 1 and tempKey[0] == "cid")):
            nbPass += 1
            print("test nbPass : ",nbPass)
        tempKey = keyListe.copy()
    for y in range(len(keyListe)):
        if keyListe[y] in file[i]:
            tempKey.remove(keyListe[y])
print(nbPass)
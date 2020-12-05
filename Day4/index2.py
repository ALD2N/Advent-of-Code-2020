from os import chdir
import re
chdir('/mnt/c/Users/axel1/Desktop/kod/GitHub/Advent-of-Code-2020/Day4')
file = open("input.txt","r").readlines()
keyListe = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
listeData = []
nbDocument = 0
testHexa = re.compile('[#][a-f0-9]{6}')
testPid = re.compile('[0-9]{9}')
def test(arg,data):
    if(arg == 'byr' and int(data)<=2002 and int(data)>=1920):
        return True
    elif(arg == 'iyr' and int(data)>=2010 and int(data)<=2020):
        return True
    elif(arg == 'eyr' and int(data)>=2020 and int(data)<=2030):
        return True
    elif(arg == 'hgt' and ((data[len(data)-2:len(data)] == "cm" and int(data[0:len(data)-2])>=150 and int(data[0:len(data)-2])<=193) or (data[len(data)-2:len(data)] == "in" and int(data[0:len(data)-2])>=59 and int(data[0:len(data)-2])<=76))):
        return True
    elif(arg == 'hcl' and testHexa.match(data) != None):
        return True
    elif(arg == 'ecl' and data in ["amb","blu","brn","gry","grn","hzl","oth"]):
        return True
    elif(arg == 'pid' and testPid.match(data) and len(data) == 9):
        return True
    else:
        return False


for i in range(len(file)):
    if(file[i] == "\n"):
        nbDocument += 1
    else:
        try:
            for y in range(len(file[i][0:len(file[i])-2].split(" "))):
                listeData[nbDocument].append(file[i][0:len(file[i])-1].split(" ")[y])  
        except IndexError:
            listeData.append(file[i][0:len(file[i])-1].split(" "))
print(listeData[0])
print(listeData[21])
nbPass = 0
for i in range(len(listeData)):
    tempKey = keyListe.copy()
    for y in range(len(keyListe)):
        for z in range(len(listeData[i])):
            if keyListe[y] in listeData[i][z]:
                data = listeData[i][z][4:len(listeData[i][z])]
                if(i == 0):
                    print(data)
                if(test(keyListe[y],data)):
                    tempKey.remove(keyListe[y])
    print(i," : ",tempKey)
    if(len(tempKey) == 0 or (len(tempKey) == 1 and tempKey[0] == "cid")):
        nbPass += 1
    else:
        print(i," value : ",listeData[i])
    
print(nbPass)
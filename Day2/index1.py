from os import chdir
chdir('/mnt/c/Users/axel1/Desktop/kod/advent of code/Day2')
file = open("source1.txt","r")

liste = file.readlines()
nbCorrectMdp = 0
for i in range(len(liste)):
    tempLine = liste[i]
    tempNbrCara = tempLine[0:tempLine.index(" ")]
    tempNbrCara1 = tempNbrCara[0:tempNbrCara.index("-")]
    tempNbrCara2 = tempNbrCara[tempNbrCara.index("-")+1:len(tempNbrCara)]
    tempCara = tempLine[tempLine.index(" ")+1]
    tempMdp = tempLine[tempLine.index(":")+2:len(tempLine)]
    if(tempMdp.count(tempCara) >= int(tempNbrCara1) and tempMdp.count(tempCara) <= int(tempNbrCara2)):
        nbCorrectMdp += 1
print(nbCorrectMdp)
    

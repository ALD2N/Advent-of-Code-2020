from os import chdir
chdir('/mnt/c/Users/axel1/Desktop/kod/advent of code/Day1/')
file = open("source2.txt","r")
liste = file.readlines()
for i in range(len(liste)):
    liste[i] = int(liste[i])
for i in range(len(liste)):
    for y in range(i+1,len(liste)-1):
        for z in range(y+1,len(liste)-1):
            if liste[i]+liste[y]+liste[z] == 2020:
                print(liste[i]*liste[y]*liste[z])
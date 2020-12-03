from os import chdir
chdir('/mnt/c/Users/axel1/Desktop/kod/advent of code/Day3')
file = open("source.txt","r")
listePattern = file.readlines()
nbArbre = 0
for i in range(len(listePattern)):
    if(listePattern[i][(i*3)%(len(listePattern[i])-1)] == "#"):
        nbArbre += 1
print(nbArbre)
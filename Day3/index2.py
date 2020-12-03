from os import chdir
chdir('/mnt/c/Users/axel1/Desktop/kod/advent of code/Day3')
file = open("source.txt","r")
listePattern = file.readlines()
tabTobogans = [[1,1],[3,1],[5,1],[7,1],[1,2]]
tabArbre = [0,0,0,0,0]
for i in range(len(listePattern)):
    for y in range(len(tabTobogans)):
        if(i*tabTobogans[y][1] < len(listePattern) and listePattern[i*tabTobogans[y][1]][(i*tabTobogans[y][0])%(len(listePattern[i])-1)] == "#"):
            tabArbre[y] += 1
        elif(i*tabTobogans[y][1] > len(listePattern) and listePattern[len(listePattern)-1][(i*tabTobogans[y][0])%(len(listePattern[i])-1)] == "#"):
            tabArbre[y] += 1
            tabTobogans.pop(y)
        elif(i*tabTobogans[y][1] > len(listePattern) and listePattern[len(listePattern)-1][(i*tabTobogans[y][0])%(len(listePattern[i])-1)] != "#"):
            tabTobogans.pop(y)
nbArbre = 1
for i in range(len(tabArbre)):
    nbArbre = nbArbre*tabArbre[i]
print(nbArbre)
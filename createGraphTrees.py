import random as r
import treeLib as trees

size = 13
differentTrees = 1301 #A000055

found = []
distGraph = [x[:] for x in [[1<<31]*differentTrees]*differentTrees]
for i in range(differentTrees):
    distGraph[i][i] = 0

G = trees.createTreeLine(size)
GPrime = trees.createTreeStar(size)
#print(GPrime)

lastTree = ""
lastTreePrime = ""
rework = 0
#Look for all different trees and add their distances
while(rework < differentTrees*5):
    if(len(found) == differentTrees):
        rework += 1
    #Tree N°1
    centers = trees.getCenter(G)
    foundTree = ""
    if(len(centers) == 2): #check if tree isn't already found
        code1, code2 = trees.code(G, centers[0], [False]*size), trees.code(G, centers[1], [False]*size)
        if(not (code1 in found or code2 in found)):
            found.append(code1)        
        if(code1 in found):
            foundTree = code1
        elif(code2 in found):
            foundTree = code2
    elif(len(centers)==1):
        code = trees.code(G, centers[0], [False]*size)
        if(not code in found):
            found.append(code)
        foundTree = code
    if(foundTree != lastTree and lastTree != ""): #add their proximity into the distGraph
        index1, index2 = found.index(foundTree),found.index(lastTree)
        distGraph[index1][index2] = distGraph[index2][index1] = 1
    lastTree = foundTree
    #change random vertice
    stack = []
    for i in range(len(G)):
        if(sum(G[i]) == 1):
            stack.append(i)
    indexLeaf = stack[r.randint(0,len(stack)-1)]
    indexOld = G[indexLeaf].index(True)
    indexNew = indexLeaf
    while(indexNew == indexLeaf or indexNew == indexOld):
        indexNew = r.randint(0,size-1)
    G[indexLeaf][indexOld] = G[indexOld][indexLeaf] = False
    G[indexLeaf][indexNew] = G[indexNew][indexLeaf] = True

    #Tree N°2
    centers = trees.getCenter(GPrime)
    foundTree = ""
    if(len(centers) == 2): #check if tree isn't already found
        code1, code2 = trees.code(GPrime, centers[0], [False]*size), trees.code(GPrime, centers[1], [False]*size)
        if(not (code1 in found or code2 in found)):
            found.append(code1)        
        if(code1 in found):
            foundTree = code1
        elif(code2 in found):
            foundTree = code2
    elif(len(centers)==1):
        code = trees.code(GPrime, centers[0], [False]*size)
        if(not code in found):
            found.append(code)
        foundTree = code
    if(foundTree != lastTreePrime and lastTreePrime != ""): #add their proximity into the distGraph
        index1, index2 = found.index(foundTree),found.index(lastTreePrime)
        distGraph[index1][index2] = distGraph[index2][index1] = 1
    lastTreePrime = foundTree
    #change random vertice
    stack = []
    for i in range(len(GPrime)):
        if(sum(GPrime[i]) == 1):
            stack.append(i)
    indexLeaf = stack[r.randint(0,len(stack)-1)]
    indexOld = GPrime[indexLeaf].index(True)
    indexNew = indexLeaf
    while(indexNew == indexLeaf or indexNew == indexOld):
        indexNew = r.randint(0,size-1)
    GPrime[indexLeaf][indexOld] = GPrime[indexOld][indexLeaf] = False
    GPrime[indexLeaf][indexNew] = GPrime[indexNew][indexLeaf] = True

#floyd warshall
for k in range(differentTrees):
    for i in range(differentTrees):
        for j in range(differentTrees):
            distGraph[i][j] = min(distGraph[i][j], distGraph[i][k]+distGraph[k][j])
#print result
print(size, differentTrees)
for s in found:
    print(s)
for i in distGraph:
    for j in i:
        print(j,end=",")
    print()
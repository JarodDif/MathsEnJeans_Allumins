import treeLib as trees

nVertices = int(input("Enter number of vertices: "))
nEdges = nVertices - 1

if(nVertices > 12):
    print("Désolé travail en cours")

G1 = trees.createTree(nVertices)
G2 = trees.createTree(nVertices)

print("Arbre n°1")
for i in range(nEdges):
    src = int(input("Entrer source de l'arete {0} : ".format(i)))
    dest = int(input("Entrer destination de l'arete {0} : ".format(i)))
    G1[src][dest] = G1[dest][src] = True

print("Arbre N°2")
for i in range(nEdges):
    src = int(input("Entrer source de l'arete {0} : ".format(i)))
    dest = int(input("Entrer destination de l'arete {0} : ".format(i)))
    G2[src][dest] = G2[dest][src] = True

data = open("{0:02d}.txt".format(nVertices), "r")
temp = data.readline()
temp = temp.split(" ")
diffTrees = int(temp[1])
treeCodes = []
for i in range(diffTrees):
    treeCodes.append(data.readline().replace("\n",""))

#print(treeCodes)

index1, index2 = -1,-1
centers = trees.getCenter(G1)
if(len(centers) == 2):
    code1, code2 = trees.code(G1, centers[0], [False]*nVertices), trees.code(G1, centers[1], [False]*nVertices)       
    index1 = code1 if code1 in treeCodes else code2
    index1 = treeCodes.index(index1)
elif(len(centers)==1):
    code = trees.code(G1, centers[0], [False]*nVertices)
    index1 = treeCodes.index(code)
    

centers = trees.getCenter(G2)
if(len(centers) == 2):
    code1, code2 = trees.code(G2, centers[0], [False]*nVertices), trees.code(G2, centers[1], [False]*nVertices)       
    index2 = code1 if code1 in treeCodes else code2
    index2 = treeCodes.index(index2)
elif(len(centers)==1):
    code = trees.code(G2, centers[0], [False]*nVertices)
    index2 = treeCodes.index(code)

index1, index2 = min(index1, index2), max(index1, index2)

for i in range(index1): #skipping lines
    data.readline()

dists = data.readline()
dists = dists.split(",")
#print("Distances entre les deux arbres est", dists[index2])

newGraph = [x[:] + [False]*nVertices for x in G1] + [[False]*nVertices + x[:] for x in G2]

trees.draw(newGraph, description="Distances entre les deux arbres est {}".format(dists[index2]), labels={i:i%nVertices for i in range(nVertices*2)})
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from time import sleep

def createTree(size):
    return [x[:] for x in [[False]*size]*size]

def createTreeLine(size):
    G = createTree(size)
    for i in range(size-1):
        G[i][i+1] = G[i+1][i] = True
    return G

def createTreeStar(size):
    G = createTree(size)
    for i in range(size-1):
        G[i][size-1] = G[size-1][i] = True
    return G

def sum(list):
    count = 0
    for i in list:
        count += 1 if i else 0
    return count

def getCenter(g):
    C = [x[:] for x in g]
    labels = [i for i in range(len(g))]

    while(len(C) > 2):
        stack = []
        for i in range(len(C)):
            if(sum(C[i]) == 1):
                stack.append(i)
        stack.reverse()
        for i in stack:
            labels.pop(i)
            C.pop(i)
            for s in C:
                s.pop(i)
        #sleep(0.5)
    return labels

def code(g, cur, visited):
   visited[cur] = True
   codeStr = "0"
   temp = []
   for i in range(len(g)):
      if(g[cur][i] and not visited[i]):
         temp.append(code(g, i, visited))
   temp.sort()
   for s in temp:
       codeStr += s
   codeStr += "1"
   return codeStr

def reconstruct(codeInput):
    n_vertices = len(codeInput)//2
    n_edges = n_vertices-1
    g = [x[:] for x in [[False]*n_vertices]*n_vertices]
    stack = []
    lastV = 0
    stack.append(0)
    i = 1
    while len(stack) != 0:
        if(codeInput[i] == '0'):
            # add to stack
            lastV += 1
            stack.append(lastV)
            g[stack[-2]][stack[-1]] = g[stack[-1]][stack[-2]] = True
        elif(codeInput[i] == '1'):
            #pop stack
            stack.pop()
        i+=1

    return n_vertices, n_edges, g

def draw(g, description="Arbre", labels={}):
    if(len(labels)==0):
        labels = {x:str(x) for x in range(len(g))}
    adjacency_matrix = np.array([[1 if j else 0 for j in i]for i in g])
    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)
    plt.figure(description)
    nx.draw(gr, node_size=500, labels=labels, with_labels=True)
    plt.show()
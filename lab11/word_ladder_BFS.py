from build_graph import buildGraph

from graph_algorithms import bfs

g = buildGraph("words.dat")

print("word ladder graph:")
for v in g:
    print(v)

print("\n============ bfs prints =======================\n")

bfs(g, g.getVertex("fool"))

print("\n================================================\n")


wordLadderList = []
v = g.getVertex("sage")
# ADD CODE HERE for part A (d) of the Lab
currentVert=v
wordLadderList.append(currentVert.getId())

while currentVert.getPred()!=None:
    currentVert=currentVert.getPred()
    wordLadderList.append(currentVert.getId())
    
wordLadderList.reverse() 
for i in wordLadderList:
    print(i,end=' ')
print('\n')


from dfs_graph import DFSGraph

g = DFSGraph()

graphFile = open("pancakes.txt")
print("Pancake graph:")
for edgeLine in graphFile:
    print(edgeLine, end="")
    edgeList = edgeLine.strip().split(':')
    g.addEdge(edgeList[0], edgeList[1], int(edgeList[2]))
    
g.dfs()
print("\nAfter DFS:")
for v in g:
    print ( v.getId(),": discovery", v.getDiscovery(), "  finish", v.getFinish())
# ADD CODE here for the EXTRA CREDIT Part of the Lab
topSort=[]
for v in g:
    fin=v.getFinish()
    ThisTuple=(fin,v.getId())
    topSort.append(ThisTuple)
topSort.sort()
topSort.reverse()
for thing in topSort:
    print(thing,end=' ')

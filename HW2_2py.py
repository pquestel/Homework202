# Solving homework exercise 2_2

import numpy as np

Edges = [(7, 9, -4.851),
(7, 2, 2.9585),
(7, 5, -4.3057),
(7, 3, 1.9569),
(7, 4, 4.4298),
(7, 0, -0.57024),
(9, 0, 4.9738),
(9, 3, 6.7302),
(9, 4, 9.3592),
(9, 2, 8.1628),
(9, 6, 1.361),
(0, 4, 4.8603),
(0, 5, -3.9274),
(0, 8, 3.426),
(0, 6, -3.5175),
(0, 1, 0.83131),
(4, 8, -1.3038),
(4, 1, -3.9057),
(4, 5, -9.2724),
(4, 2, -1.9237),
(8, 6, -6.5603),
(8, 2, -0.56773),
(8, 1, -2.9797),
(8, 5, -8.4274),
(8, 3, -2.1633),
(6, 2, 6.5333),
(2, 5, -7.8453),
(2, 1, -2.3873),
(3, 1, -1.1802),
(5, 1, 4.9125)]


#nodes = [0,1,2,3,4,5,6,7,8,9]
paths = []

offsets = np.zeros([10,1])


for i in Edges:
    if i[0] == 0:
        offsets[i[1]] = i[2]
        
    elif i[1] == 0:
        offsets[i[0]] = -i[2]

# print(offsets)

#Determine matrix of all neighbours

neighbours = np.zeros([10,10])
weights = np.zeros([10,10])

for j in range(10):
    for i in range(30):
        if Edges[i][0] == j:
            neighbours[j,Edges[i][1]] = 1
            weights[j,Edges[i][1]] = Edges[i][2]
        elif Edges[i][1] == j:
            neighbours[j,Edges[i][0]] = 1
            weights[j,Edges[i][0]] = Edges[i][2]

 
#print(neighbours)
#print(weights)

# we can use the weights to define the shortest path from any node to node 0 and simply add the
# different offsets of the shortest path (simple strategy).

node0Paths = []
node1Paths = []
node2Paths = []
node3Paths = []
node4Paths = []
node5Paths = []
node6Paths = []
node7Paths = []
node8Paths = []
node9Paths = []

for i in range(len(neighbours)):
    if neighbours[0][i] == 1:
        node0Paths.append(i)
for i in range(len(neighbours)):
    if neighbours[1][i] == 1:
        node1Paths.append(i)
for i in range(len(neighbours)):
    if neighbours[2][i] == 1:
        node2Paths.append(i)
for i in range(len(neighbours)):
    if neighbours[3][i] == 1:
        node3Paths.append(i)
for i in range(len(neighbours)):
    if neighbours[4][i] == 1:
        node4Paths.append(i)
for i in range(len(neighbours)):
    if neighbours[5][i] == 1:
        node5Paths.append(i)
for i in range(len(neighbours)):
    if neighbours[6][i] == 1:
        node6Paths.append(i)
for i in range(len(neighbours)):
    if neighbours[7][i] == 1:
        node7Paths.append(i)
for i in range(len(neighbours)):
    if neighbours[8][i] == 1:
        node8Paths.append(i)
for i in range(len(neighbours)):
    if neighbours[9][i] == 1:
        node9Paths.append(i)


            
allNodesNeighbours = [node1Paths,node2Paths,node3Paths,node4Paths,node5Paths,node6Paths,node7Paths,node8Paths,node9Paths]

#print(allNodesNeighbours)
#print(neighbours)

#Function returns all the neighbours for any given node. 
def giveNeighbours(node):
    return(allNodesNeighbours[node-1]) #list starts at node1Paths and not node0paths. 

def dfs(nodes, init_node):  # just explores the nodes, depth first search algorithm 
    node_list = []
    queue = [init_node]

    while queue:
        node = queue.pop(0)
        node_list.append(node)
        neighbors = giveNeighbours(node)
        neighbors = [neighbor for neighbor in neighbors if neighbor not in queue + node_list]
        if neighbors != []:
            queue =  neighbors + queue
    
    return node_list

print(dfs(node1Paths),1)

## Next steps: 
# Compute all node lists for all possible paths of the network by using depth first search algorithm 
# could also try breadth first search algorithm. 
# Then, once we have computed all the possible paths, we can map the node lists to the respective offsets
# of the transitions.
# With this we can find all the optimal offsets for the network. 

# Unfortunately due to a lack of time, I probably won't be able to finish the code, I will be on the plane during 
# submission deadline. Hopefully, the next steps correctly express what I had in mind ! 

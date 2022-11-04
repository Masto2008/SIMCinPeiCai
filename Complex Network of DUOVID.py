import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.read_edgelist('contact.edgelist')

#asign infecteds
#_______________________________________________________________________________________________________________________

Result = []
T=0
N = len(G.nodes)
infected = ["8","9"]
numbers = np.array(G.nodes)
numbers = [x for x in numbers if x not in infected]

#print(random.choice())
saveG = G
saveI = infected
maxI =0
maxInfect=[]
def CalcInfect(infected):
    while True:
        no_of_ALPHA_infecteds = len(infected)
        for node in G:
            if len([x for x in infected if x in G.adj[node]]) > 1 \
                    and node not in infected:
                infected.append(node)
        if len(infected) == no_of_ALPHA_infecteds:
            break
    print("Total infected = "+str(len(infected)))
    return infected



for i in range(N-2):
    G = saveG.copy()
    infected = saveI.copy()
    infected.append(numbers[i])
    print("Before spead")
    print(infected)
    CalcInfect(infected)
    if maxI < len(infected):
        maxI = len(infected)
        maxInfect = infected.copy()

print("The first infected are\n" + str(maxInfect[0]) + "," + str(maxInfect[1]) + "," + str(maxInfect[2]))
print("max I = "+str(maxI))
print("The Total list of infected is")
print(maxInfect)
#
# infected.sort()
# # print(str(infected) + "are infected")
# T = T + 1
# print(infected)
# if len(infected) == len(G.nodes):
#     print("Everyone have been infected")
# else:
#     print("Not everyone have been infected")
#
#
#
# #infected = ["8","9"]
color_map = []
for node in G:
    if node in maxInfect:
        color_map.append("#ff0000")
    else:
        color_map.append("#5cffef")
options = {"edgecolors": "#69BE28", "linewidths": 3, "width": 3,}
nx.draw_networkx(G,
                 with_labels = True,
                 node_color=color_map,
                 **options)
plt.show()
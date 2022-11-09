import random
#random.seed()

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

#To-do list:
#Make a version that display the infection step by step

#Blue stand for normal person, Green for infected

#Variable
l=4
L = l+1
N = int((L+1)*L/2)


# amount of nodes on the edge of the Triangle



#Create Graph
#_______________________________________________________________________________________________________________________
G = nx.Graph()

def CreateTriangleGraph(G,L):

    width = L
    h = 0
    T = 1
    for j in range (L):
        for i in range(width):
            G.add_node(T, pos = (i+(h/2) , h))
            T = T + 1
        width =  width - 1
        h = h + 1


    width = L
    h = 0
    T = 1
    for j in range(L):
        for i in range(width-1):
            G.add_edge(T, T+1)
            T = T + 1
        width = width - 1
        h = h + 1
        T = T + 1

    width = L
    h = 0
    T = 1
    for j in range(L):
        for i in range(width-1):
            G.add_edge(T, T+width)
            T = T + 1
        width = width - 1
        h = h + 1
        T = T + 1

    width = L
    h = 0
    T = 1
    for j in range(L):
        for i in range(width-1):
            G.add_edge(T+1, T+width)
            T = T + 1
        width = width - 1
        h = h + 1
        T = T + 1
    return G
G = CreateTriangleGraph(G,L)





# assign variable
# _______________________________________________________________________________________________________________________
vaccinated = []
first_infected = {11,13}
infected = list(first_infected)
# _______________________________________________________________________________________________________________________
potential_infected = np.array(G.nodes)
potential_infected = [x for x in potential_infected if x not in infected]
def CalcPandemic(vaccinated, G, infected):

    potential_infected = np.array(G.nodes)
    potential_infected = [x for x in potential_infected if x not in infected]
    potential_infected = [x for x in potential_infected if x not in vaccinated]
    N = len(G.nodes)
    saveG = G
    saveI = infected
    maxI = 0
    maxInfect = []


    def CalcInfect(infected):
        while True:
            no_of_ALPHA_infecteds = len(infected)
            for node in G:
                if len([x for x in infected if x in G.adj[node]]) > 1 \
                        and node not in infected and node not in vaccinated:
                    infected.append(node)
            if len(infected) == no_of_ALPHA_infecteds:
                break
        return infected


    # simulate the outcome of this vaccination candinate

    for i in range(len(potential_infected)):
        G = saveG.copy()
        CalcInfect(infected)
        if maxI < len(infected):
            maxI = len(infected)
            maxInfect = infected.copy()

    # print("The first infected are\n" + str(first_infected))
    # print("The vaccinated is = " + str(vaccinated))
    # print("The amount of people infected is = " + str(maxI))
    # print("The Total list of infected is")
    # print(maxInfect)

    color_map = []
    for node in G:
        if node in maxInfect:
            color_map.append("#ff0000")
        if node in vaccinated:
            color_map.append("green")
        if node not in vaccinated and node not in maxInfect:
            color_map.append("#5cffef")

    plt.figure(1)
    options = {"edgecolors": "#69BE28", "linewidths": 3, "width": 3, }
    nx.draw_networkx(G,
                     with_labels=True,
                     pos = nx.get_node_attributes(G,'pos'),
                     node_color=color_map,
                     **options)

    #plt.show()
    return maxInfect

maxInfectsave = N
for node in potential_infected:
    vaccinated = [node]
    infected = list(first_infected)
    maxInfect = CalcPandemic(vaccinated,G,infected)

    if len(maxInfect) < maxInfectsave:
        maxInfectsave = len(maxInfect)
        BestV = node

vaccinated = [BestV]
infected = list(first_infected)
maxInfect = CalcPandemic(vaccinated,G,infected)
plt.show()
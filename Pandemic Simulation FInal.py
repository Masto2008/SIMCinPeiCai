import matplotlib.pyplot as plt
import numpy as np
import networkx as nx


# Create Graph
def CreateTriangleGraph(L):
    width = L
    h = 0
    T = 1
    for j in range(L):
        for i in range(width):
            G.add_node(str(T), pos=(i + (h / 2), h))
            T = T + 1
        width = width - 1
        h = h + 1

    width = L
    h = 0
    T = 1
    for j in range(L):
        for i in range(width - 1):
            G.add_edge(str(T), str(T + 1))
            T = T + 1
        width = width - 1
        h = h + 1
        T = T + 1

    width = L
    h = 0
    T = 1
    for j in range(L):
        for i in range(width - 1):
            G.add_edge(str(T), str(T + width))
            T = T + 1
        width = width - 1
        h = h + 1
        T = T + 1

    width = L
    h = 0
    T = 1
    for j in range(L):
        for i in range(width - 1):
            G.add_edge(str(T + 1), str(T + width))
            T = T + 1
        width = width - 1
        h = h + 1
        T = T + 1
    return G

def CreateSquareGraph(L):
    width = L
    h = 0
    T = 1
    for j in range(L):
        for i in range(width):
            G.add_node(str(T), pos=(i, h))
            T = T + 1
        h = h + 1

    width = L
    h = 0
    T = 1
    for j in range(L):
        for i in range(width - 1):
            G.add_edge(str(T), str(T + 1))
            T = T + 1
        h = h + 1
        T = T + 1

    width = L
    T = 1
    for j in range((L) - 1):
        for i in range(width):
            G.add_edge(str(T), str(T + width))
            T = T + 1
    #
    # width = L
    # h = 0
    # T = 1
    # for j in range(L):
    #     for i in range(width - 1):
    #         G.add_edge(T + 1, T + width)
    #         T = T + 1
    #     width = width - 1
    #     h = h + 1
    #     T = T + 1
    return G
# L stand for the amount of nodes on the edge of the shape, NOT the amount of (edges between nodes) on the edge


G = nx.Graph()
G = CreateTriangleGraph(5)
#G = nx.read_edgelist('contact.edgelist')
N = len(G.nodes)


# Simulation
def PrintResult(first_infected, first_vaccinated, infected):
    print("First Infected list\n " + str(first_infected))
    print("Vaccinated list\n " + str(first_vaccinated))
    print("The amount of people infected is = " + str(len(infected)))
    print("The Total list of infected is")
    print(infected)


def CalcPotential_Infected(infected, vaccinated):
    potential_infected = np.array(G.nodes)
    potential_infected = [x for x in potential_infected if x not in infected]
    potential_infected = [x for x in potential_infected if x not in vaccinated]
    return potential_infected

def GenerateFirst_Infecteds(potential_infected, i):
    first_infected.append(potential_infected[i])
    return first_infected

def GenerateFirst_Vaccinateds(first_vaccinated, i):
    first_vaccinated.append(i)
    return first_vaccinated



def Individual_Simulation(G, first_vaccinated, first_infected):
    # Simulating
    vaccinated = list(first_vaccinated)
    infected = list(first_infected)

    def CalcInfect(infected, vaccinated):
        while True:
            infected_count = len(infected)
            for node in G:
                if len([x for x in infected if
                        x in G.adj[node]]) > 1 and node not in infected and node not in vaccinated:
                    infected.append(node)

            if len(infected) == infected_count:
                break
        return infected

    infected = CalcInfect(infected, vaccinated)


    #PrintResult(first_infected,vaccinated,infected)
    return infected

def Multiple_Simulation(G, first_vaccinated, first_infected):
    infected = first_infected.copy()
    vaccinated = first_vaccinated.copy()
    potential_infected = CalcPotential_Infected(infected, vaccinated)
    saveinfected = []
    savefirst_infected = first_infected.copy()
    Disaster = []

    #If you want to generate more first infected, make another for loop inside I2 and label it I3 with
    #
    # first_infected = savefirst_infected3.copy()
    # first_infected.append(potential_infected[I3])
    # savefirst_infected4 = first_infected.copy()
    #
    #Then move this to I3
    # infected = Individual_Simulation(G, first_vaccinated, first_infected)
    #
    #Then repeat the process so on and so forth (sorry for the inconvinience, I do not know a better way to do this)

    #1st infected
    for I1 in range(len(potential_infected)):
        first_infected = savefirst_infected.copy()
        first_infected.append(potential_infected[I1])
        savefirst_infected2 = first_infected.copy()
        #
        #2nd infected
        for I2 in range((I1+1),(len(potential_infected))):
            first_infected = savefirst_infected2.copy()
            first_infected.append(potential_infected[I2])
            savefirst_infected3 = first_infected.copy()

            infected = Individual_Simulation(G, first_vaccinated, first_infected)

            if len(infected) == len(G.nodes):
                Disaster.append(first_infected)

            if len(infected) > len(saveinfected):
                bestfirst_infected = first_infected.copy()
                saveinfected = infected.copy()


    infected = saveinfected.copy()
    print("The chance of a Disaster(everyone're infected) is")
    print(str((len(Disaster)/(N*(N-1)/2))*100)+"%")
    R = [bestfirst_infected,infected]
    return R


R = []
# Starting variable
#must be a number in the form of a string
first_vaccinated = []
first_infected = []

#Individual_SImulation will predict the outcome using the starting variables
#Multiple_Simulation will generate 2 (changeable inside the function more first_infected person then predict all the outcome using all the possible generations
#Select either of them by uncomment it and turn the other into a comment

#Individual mode

infected = Individual_Simulation(G, first_vaccinated, first_infected)


#Multiple mode

#R = Multiple_Simulation(G, first_vaccinated, first_infected)


if R:
    first_infected = R[0]
    infected = R[1]

#PrintResult
PrintResult(first_infected, first_vaccinated, infected)

# render Graph
def RenderInfectionGraph(G, infected, vaccinated):
    color_map = []
    for node in G:
        if node in infected:
            color_map.append("#ff0000")
        if node in vaccinated:
            color_map.append("green")
        if node not in vaccinated and node not in infected:
            color_map.append("#5cffef")

    plt.figure(1)
    options = {"edgecolors": "#69BE28", "linewidths": 3, "width": 3, }
    if nx.get_node_attributes(G,'pos'):
        nx.draw_networkx(G,
                     with_labels=True,
                     pos=nx.get_node_attributes(G,'pos'),
                     node_color=color_map,
                     **options)
    else:
        nx.draw_networkx(G,
                         with_labels=True,
                         pos=nx.kamada_kawai_layout(G),
                         node_color=color_map,
                         **options)
    plt.show()
RenderInfectionGraph(G, infected, first_vaccinated)

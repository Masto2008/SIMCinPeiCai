import matplotlib.pyplot as plt
import numpy as np
import networkx as nx




# assign variable
# _______________________________________________________________________________________________________________________
vaccinated = ['91']
first_infected = {"8", "9", "1", "151"}
G = nx.read_edgelist('contact.edgelist')
infected = list(first_infected)
# _______________________________________________________________________________________________________________________
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

    print("The first infected are\n" + str(first_infected))
    print("The vaccinated is = " + str(vaccinated))
    print("The amount of people infected is = " + str(maxI))
    print("The Total list of infected is")
    print(maxInfect)

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
                     pos=nx.kamada_kawai_layout(G),
                     node_color=color_map,
                     **options)

    plt.show()
c = CalcPandemic(vaccinated,G,infected)
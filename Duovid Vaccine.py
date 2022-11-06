import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

G = nx.read_edgelist('contact.edgelist')

# todo: create an author diary that document the 7 days
# credit to countless individuals on Stackoverflow
# asign infecteds
# _______________________________________________________________________________________________________________________

Result = []
T = 0
N = len(G.nodes)
vaccinated = []
infected = ["8", "9"]


def CalcPandemic(vaccinated, G, infected):
    potential_infected = np.array(G.nodes)
    potential_infected = [x for x in potential_infected if x not in infected]
    potential_infected = [x for x in potential_infected if x not in vaccinated]
    # print(random.choice())

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
        # print("Total infected = "+str(len(infected)))
        return infected

    # simulate the outcome of every vaccination candinate

    # simulate every outcome if the vaccinated individual was ^
    for i in range(len(potential_infected)):
        G = saveG.copy()
        infected = saveI.copy()
        infected.append(potential_infected[i])
        # print("Before spead")
        # print(infected)
        CalcInfect(infected)
        if maxI < len(infected):
            maxI = len(infected)
            maxInfect = infected.copy()

    # print("The first infected are\n" + str(maxInfect[0]) + ", " + str(maxInfect[1]) + " and " + str(maxInfect[2]))
    # print("max I = " + str(maxI))
    # print("The Total list of infected is")
    # print(maxInfect)
    # print('\n'*2)
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
    # maxc = 0
    # for node in G:
    #     if len(G.adj[node]) > maxc:
    #         maxc = len(G.adj[node])
    #         print(node)
    # print(maxc)

    color_map = []
    for node in G:
        if node in maxInfect:
            color_map.append("#ff0000")
        if node in vaccinated:
            color_map.append("green")
        if node not in vaccinated and node not in maxInfect:
            color_map.append("#5cffef")

    # plt.figure(1)

    # options = {"edgecolors": "#69BE28", "linewidths": 3, "width": 3, }
    # nx.draw_networkx(G,
    #                  with_labels=True,
    #                  pos=nx.kamada_kawai_layout(G),
    #                  node_color=color_map,
    #                  **options)

    # A color map that display how much someone interact with people
    # _______________________________________________________________________________________________________________________

    # plt.figure(2)

    G2 = nx.read_edgelist('contact.edgelist')

    G2colors = []

    for node in G2:
        G2colors.append(len(G2.adj[node]))
    # print(G2colors)

    # # create number for each group to allow use of colormap
    # from itertools import count
    # # get unique groups
    # groups = set(nx.get_node_attributes(g,'group').values())
    # mapping = dict(zip(sorted(groups),count()))
    # nodes = g.nodes()
    # colors = [mapping[g.node[n]['group']] for n in nodes]
    #
    # # drawing nodes and edges separately so we can capture collection for colobar
    # pos = nx.spring_layout(g)
    # ec = nx.draw_networkx_edges(g, pos, alpha=0.2)
    # nc = nx.draw_networkx_nodes(g, pos, nodelist=nodes, node_color=colors,
    #                             with_labels=False, node_size=100, cmap=plt.cm.jet)
    # plt.colorbar(nc)
    # plt.axis('off')
    # plt.show()

    # nx.draw(G2,
    #         with_labels=True,
    #         pos=nx.kamada_kawai_layout(G),
    #         node_color=G2colors,
    #         **options)
    return maxInfect





# print('The vaccinated')
# print(vaccinated[0])
# print('The amount of people this person interact with')
# print(len(G[vaccinated[0]]))

# print('Distance between vaccinated to person 8')
# print(len(path[vaccinated[0]]['8']))
# print('Distance between vaccinated person to person 9')
# print(len(path[vaccinated[0]]['9']))
# print("The amount of infections if this person was vaccinated")
# print(len(maxInfect))

path = dict(nx.all_pairs_shortest_path(G))
ot=[[]]

xa = []
ya = []


Gsave=G
for node in G:
    vaccinated = []
    vaccinated.append(node)
    infected = ["8", "9"]
    G=Gsave.copy()
    maxInfect = CalcPandemic(vaccinated, G, infected)
    Stage2Connection = 0
    for cNode in G.adj[node]:
        Stage2Connection = Stage2Connection + G.degree[cNode]


    weight8 = 1 / len(path[vaccinated[0]]['8'])
    ya.append(weight8)
    xa.append(len(path[vaccinated[0]]['8']))

    ot.append([vaccinated[0],weight8,len(path[vaccinated[0]]['1']),len(G[vaccinated[0]]),Stage2Connection,len(maxInfect)])




H = plt.plot(xa,ya)

#print(ot)
a = np.asarray(ot)
np.savetxt("Test1.csv",a,delimiter=",",fmt='%s')


























































plt.show()
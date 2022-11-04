import random
#random.seed()

import matplotlib.pyplot as plt
import networkx as nx


#To-do list:
#Make a version that display the infection step by step

#Blue stand for normal person, Green for infected


#Variable
l=10
L = l+1
N = int((L+1)*L/2)


# amount of nodes on the edge of the Triangle
no_of_ALPHA_infecteds = 2


#Create Graph
#_______________________________________________________________________________________________________________________
G = nx.Graph()



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
#new
tot = 0
cnt = 0
for a in range(1,N):
    for b in range(a + 1, N+1):
        dist = nx.shortest_path(G, a, b)
        if (len(dist)<4): cnt=cnt+1
        #else: print(str(a)+","+str(b)+str(dist))
        tot = tot + 1
print(str(cnt)+"/"+str(tot)+"="+str(cnt/tot*100))
#asign infecteds
#_______________________________________________________________________________________________________________________

#numbers = list(range(1, N))
infected = []
#for i in range (no_of_ALPHA_infecteds):
    #numbers = [x for x in numbers if x not in infected]
    #infected.append(random.choice(numbers))
Result = []
T=0
for a in range (N-1):
    #for b in [x for x in range(N) if x != a]:
    for b in range(a + 1, N):
        infected.clear()
        infected.append(a+1)
        infected.append(b+1)
        ALP = [infected]

        print(str(infected) + "are Alpha infected")

        #algorightm to find who will be infected by the ALPHA
        #_______________________________________________________________________________________________________________________
        while True:
            no_of_ALPHA_infecteds = len(infected)
            for node in G:
                if len([x for x in infected if x in G.adj[node]]) > 1\
                and node not in infected:
                    infected.append(node)
            if len(infected) == no_of_ALPHA_infecteds:
                break

        infected.sort()
        #print(str(infected) + "are infected")
        T=T+1
        if len(infected) == len(G.nodes):
            print("Everyone have been infected")
            Result.append(ALP)
        else:
            print("Not everyone have been infected")




        color_map = []
        for node in G:
            if node in infected:
                color_map.append("#2d8709")
            else:
                color_map.append("#66cafa")
        options = {"edgecolors": "#69BE28", "linewidths": 3, "width": 3,}
        nx.draw_networkx(G,
                         with_labels = True,
                         pos = nx.get_node_attributes(G,'pos'),
                         node_color=color_map,
                         **options)
        #plt.show()
[Result.append(infected) for x in Result if x not in Result]
print(len(Result))
print(T)
print(str((len(Result))/T*100)+"%")
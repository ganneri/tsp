#!/usr/bin/env python
# coding: utf-8

# In[124]:


get_ipython().run_cell_magic('time', '', 'import numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport math\nfrom sys import maxsize \nfrom itertools import permutations\nimport timeit\n\n\n# Function body\ndef shortestPathCost(graph, n, tsize): \n \n    # store all vertices apart from the source vertex \n    vertex = [] \n    for i in range(tsize): \n        if i != n: \n            vertex.append(i) \n    \n    \n    # All about cost \n    lowest_cost = maxsize \n    next_permutation=permutations(vertex) #each permutation is a possible route considering source city at start and end by default\n    \n    for i in next_permutation: #Calculating cost of each possible permutation or route\n        current_cost = 0   \n        k = n #starting from source city, with index k = 0\n        for j in i: \n            current_cost += graph[k][j] #summation of routes between cities for a given full tour\n            k = j \n            \n        current_cost += graph[k][n] #Adding cost of going back to source city at the end\n        if current_cost < lowest_cost:\n            ideal_route = []\n            ideal_route = list(i)\n            ideal_route.insert(n,n) #inserting source city at the start of the ideal route\n            ideal_route.insert(tsize,n) #inserting source city at the end of the ideal route\n        lowest_cost = min(lowest_cost, current_cost) \n         \n    return lowest_cost, ideal_route\n \n\ndef getCostOfRoute(route, n):\n    cost = 0\n    k=n\n    for j in route:\n        cost += graph[k][j]\n        k=j\n        \n    cost += graph[k][n]\n    requested_route = list(route)\n    requested_route.insert(n,n) #inserting source city at the start of the ideal route\n    requested_route.insert(tsize,n) #inserting source city at the start of the ideal route\n    \n    return cost, requested_route\n\n\n\n#to calculate cost of a particular route\n\nif __name__ == "__main__": \n    tsize = int(input("Please enter the number of cities "))\n    n = 0\n\n    \n    graph = np.array(tsize) #graph in matrix\n\n#For 4 given cities\n#graph = np.array([[0, 20, 42, 35], [20, 0, 30, 34], [42, 30, 0, 12], [35, 34, 12, 0]]) \n\n#graph for testing tour cost with random sizes\n\'\'\'graph = np.random.randint(50, size = (tsize, tsize))\nfor i in range(0, tsize):\n    for j in range(0, tsize):\n        if i == j: \n            graph[i][j] = 0 #To ensure diagonal elements are 0\n\'\'\'\n\ndata = pd.read_csv(r"C:\\Users\\girid\\Downloads\\ulysses16.csv")\nx = data["x"]\ny = data["y"]\n\ntsize = len(x)\n\n\ndef distance(x1,x2,y1,y2): \n    dist = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)) #Pythagoras\' theorem\n    return(dist)\n\ng=[]\ndraft = []\nfor i in range(0, tsize):\n   \n    for j in range(0, tsize):\n        #list(graph_draft)\n        draft.append(distance(x[i],x[j],y[i],y[j]))\n        #print(draft)\n    g = np.array(draft)\n    graph = np.array_split(g, tsize)\n    \np = int(input("What would you like to know. Press 1 for Shortest path cost or Press 2 for Cost of a particular route: "))\nif p == 1:\n    print(shortestPathCost(graph, n, tsize))\n    \nelif p == 2:\n    route = []   \n    for b in range(0, tsize-1):\n        draft = int(input("Please enter the desired route as city numbers one after the other. Note: Source city is numbered 0 and does not need to be entered at start or end of the route: "))\n        route.append(draft)\n    \n    print(getCostOfRoute(route, n))\n\nelse:\n    print("Please enter only 1 or 2 as inputs")\n')


# In[ ]:





# In[ ]:





# In[123]:


cities = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16]
time = [0.832, 0.834, 0.864, 1.16, 1.26, 1.71, 7.1, 32.4, 358, 4871, 41400]
plt.title("Step 6 Question")
plt.xlabel("Cities")
plt.ylabel("Time (in sec)")
plt.plot(cities, time)


# In[ ]:





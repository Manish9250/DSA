def dijkstra(WList,s):
    infinity = 1 + len(WList.keys())*max([d for u in WList.keys()for (v,d) in WList[u]])
    (visited,distance) = ({},{})
    for v in WList.keys():
        (visited[v],distance[v]) = (False,infinity)       
    distance[s] = 0    
    for u in WList.keys():
        nextd = min([distance[v] for v in WList.keys() if not visited[v]])
        nextvlist = [v for v in WList.keys() if (not visited[v]) and distance[v] == nextd]
        if nextvlist == []:
            break
        nextv = min(nextvlist)        
        visited[nextv] = True        
        for (v,d) in WList[nextv]:
            if not visited[v]:
                if distance[v] > distance[nextv] + d:
                    distance[v] = distance[nextv] + d   
    return(distance)

import heapq


def unmodified_dijkstra(graph, start, target):
    print("-"*20, "Start:  Unmodified Dajkistra", "-"*20)
    n = len(graph)  # 
    print("Number of nodes: ", n)
    distances = [float('inf')] * n  # Initialize distances as infinity
    distances[start] = 0  # Distance to the start node is 0
    print("Distances: ", distances)
    pq = [(0, start)]  # Priority queue initialized with (distance, node)
    
    while pq:
        print("Priorty qeue", pq)
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(pq)
        print(f"Node with smallest distance [{current_node}:{current_distance}]")

        if current_node == target:
            print("Target vertex found with distance: ", current_distance)
            print("-"*20, "End:  unmodified Dejkistra", "-"*20)
            return current_distance
        
        # Skip if the distance is outdated
        if current_distance > distances[current_node]:
            print(f"Outdated Distance: Previous dis: [{distances[current_node]}], current Dis: [{current_distance}]")
            continue

        # Process neighbors
        for neighbor, weight in graph[current_node]:
            print(f"[{current_node}'s] Neighbour node [{neighbor}] with dis [{weight}]")
            distance = current_distance + weight
            print("calculated distance: ", distance, "Previous distance: ", distances[neighbor])
            # If a shorter path is found, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                print("New dis is small added to qeue: ", (distance, neighbor))
    print("-"*20, "End:  unmodified Dejkistra", "-"*20)
    return distances[target]

#{0: [(2, 11), (5, 12)],
# 1: [(5, 17), (4, 14)], 
# 2: [(0, 11), (3, 10)], 
# 3: [(5, 52), (4, 13), (2, 10)], 
# 4: [(1, 14), (3, 13)], 
# 5: [(0, 12), (3, 52), (1, 17)]}

def dijkstra1(graph, start, target):
    """Dijkstra's algorithm to find the shortest path from start to target."""
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    pq = [(0, start)]  # Priority queue (distance, node)

    while pq:
        current_dist, node = heapq.heappop(pq)

        if node == target:
            return current_dist

        if current_dist > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances[target]


#{0: [(2, 11), (5, 12)],
# 1: [(5, 17), (4, 14)], 
# 2: [(0, 11), (3, 10)], 
# 3: [(5, 52), (4, 13), (2, 10)], 
# 4: [(1, 14), (3, 13)], 
# 5: [(0, 12), (3, 52), (1, 17)]}

def shortestCircularRoute(WList, S):
    print("-"*20, "Start:  ShortestCircularPAth", "-"*20)
    """Find the shortest circular route starting and ending at S."""
    min_distance = float('inf')
    print("Minimum Distance: ", min_distance)
    copylist = WList[S].copy()
    # Iterate through each neighbor of S
    for neighbor, weight in copylist:
        print(f"Neighbour of [{S}] is [{neighbor}] with weight: {weight}")
        # Temporarily remove the edge (S, neighbor)
        WList[S].remove((neighbor, weight))
        WList[neighbor].remove((S, weight))
        print("removed neighbours", WList[S], WList[neighbor])

        # Compute shortest path from neighbor back to S
        print("-"*5, "Starting Dejkistra with ", "Start vertex: ", neighbor, "Target vertex: ", S)
        back_to_s_distance = unmodified_dijkstra(WList, neighbor, S)
        print(f"distance from {neighbor} back to {S} is [{back_to_s_distance}]")

        # Calculate total circular route distance
        total_distance = weight + back_to_s_distance
        print(f"Total back distance: {total_distance}")
        min_distance = min(min_distance, total_distance)
        print(f"minimum distance: {min_distance}")

        # Restore the edge (S, neighbor)
        WList[S].append((neighbor, weight))
        WList[neighbor].append((S, weight))
        #WList[S] = [(neighbor, weight)] + WList[S]
        #WList[neighbor] = [(S, weight)] + WList[neighbor]
        print("added back neighbours", WList[S], WList[neighbor])
    print("-"*20, "End:  ShortestCircularPAth", "-"*20)
    return min_distance

n = 6
edges = [(2,0,11),(5,0,12),(5,3,52),(5,1,17),(4,1,14),(3,4,13),(2,3,10)]
S = 0
WL = {}
for i in range(n):
    WL[i] = []
for ed in edges: #create dictionary for undirected graph
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))

#print(WL)
print(shortestCircularRoute(WL,S))

#print(unmodified_dijkstra(WL, 2))
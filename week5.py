import heapq
def Airport(Wlist):
    visited = set()

    visited.add(0)
    q = [(0, 0)]
    min_dis = 0

    while q:
        print(q)
        q.sort()
        dis, node = heapq.heappop(q)
        print("Dis: ", dis, "Node: ", node)
        min_dis += dis
        print("total dis: ", min_dis)

        min_v_dis = 1000000
        for neighbour, distance in Wlist[node]:
            if neighbour not in visited:
                if distance < min_v_dis:
                    min_v_dis = distance
                    visited.add(neighbour)
                    q.append((distance, neighbour))
    return min_dis, visited
        


size = 7
edges = [(0,1,10),(0,2,50),(0,3,300),(5,6,45),(2,1,30),(6,4,37),(1,6,65),(2,5,76),(1,3,40),(3,4,60),(2,4,20)]
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))

print(WL)
print(Airport(WL))

{0: [(1, 10), (2, 50), (3, 300)], 
 1: [(0, 10), (2, 30), (6, 65), (3, 40)], 
 2: [(0, 50), (1, 30), (5, 76), (4, 20)], 
 3: [(0, 300), (1, 40), (4, 60)], 
 4: [(6, 37), (3, 60), (2, 20)], 
 5: [(6, 45), (2, 76)], 
 6: [(5, 45), (4, 37), (1, 65)]}



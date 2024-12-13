def minmax(a, b):
    maxlist = None
    minlist = None
    if max(a) > max(b):
        maxlist = a
        minlist = b
    else:
        maxlist = b
        minlist = a
    print("Max list: ", maxlist)
    print("Min list: ", minlist)
    
    
    program = True
    while True:
        minval = max(minlist)
        min_index = None
        max_index = -1
        
        for i in range(len(minlist)):
            if minlist[i] == minval:
                min_index = i 
        print("Index of minlist val ", minval, "is", min_index)
        for i in range(len(maxlist)):
            if maxlist[i] < minval:
                max_index = i 
        print("Index of maxlist val ", maxlist[max_index], "is", max_index)
        if max_index != -1:
            print("minvalue:",minval, "max Value:", maxlist[max_index])
            (maxlist[max_index], minlist[min_index]) = (minlist[min_index], maxlist[max_index])
            print("Min list: ", minlist)
            print("Max list: ", maxlist)
        else:
            return max(maxlist)*max(minlist)



def removeDuplicate(head):
    
    while head.next:
        print("Step:1--> ","Head: ", head.data, "Next: ", head.next.data)
        print("Step:2--> ",head.data == head.next.data)
        if head.data == head.next.data:
            head.next = head.next.next
            
            print("Step3:--> ","Next head: ",head.next.data)
        else:
            head = head.next
            print("Step3:-->",head.data)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)
head1.next.next.next = Node(7)
head1.next.next.next.next = Node(9)

head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)



def mergeSortedList(head1, head2):

    if not head1:
        return head2
    if not head2:
        return head1

    node = Node(0)
    new_head = node
    while head1 and head2:
        
        if head1.data < head2.data:
            new_head.next = head1
            head1 = head1.next
        else:   
            new_head.next = head2
            head2 = head2.next
        new_head = new_head.next
    
    if head1:
        new_head.next = head1
    if head2:
        new_head.next = head2

    return node.next
#print(mergeSortedList(head1, head2).data)

data = [2, 3, 4, 21, 43, 52, 51, 18, 11, 9, 6, 5, 1] 


def indexfinder(l, x):
    for i in range(len(l)):
        if l[i] == x:
            return i


def peak_unimodal(l):
    (left, right) = (0, len(l)-1)

    while left < right:
        mid = (left+right)//2

        if l[mid] < l[mid+1]:
            left = mid+1
        else:
            right = mid 
    return left


import copy
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

# DFS initialization
def DFS_init(AList):
    (visited, parent) = ({}, {})
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1
    return (visited, parent)

#WL:
    #{0: [(2, 11), (5, 12)], 1: [(5, 17), (4, 14)], 
    # 2: [(0, 11), (3, 10)], 3: [(5, 52), (4, 13), (2, 10)], 
    # 4: [(1, 14), (3, 13)], 5: [(0, 12), (3, 52), (1, 17)]}
def DFS(AList, visited, parent, vertex):
    visited[vertex] = True
    print(visited, parent)

    for (k,_) in AList[vertex]:
        if (not visited[k]):
            parent[k] = vertex
            (visited, parent) = DFS(AList, visited, parent, k)
    return (visited, parent)


n = 6
edges = [(2,0,11),(5,0,12),(5,3,52),(5,1,17),(4,1,14),(3,4,13),(2,3,10)]
S = 0
WL = {}
for i in range(n):
    WL[i] = []
for ed in edges: #create dictionary for undirected graph
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
#print(shortestCircularRoute(WL,S))


(visited, parent) = DFS_init(WL)
(visited, parent) = DFS(WL, visited, parent, 0)
print(visited, parent)




# [(2,0,11),(5,0,12),(5,3,52),(5,1,17),(4,1,14),(3,4,13),(2,3,10)]
def shortestCircularRoute(WL, S):
    dis = dijkstra(WL, S) #{0: 0, 1: 29, 2: 11, 3: 21, 4: 34, 5: 12}
    #WL:
    #{0: [(2, 11), (5, 12)], 1: [(5, 17), (4, 14)], 
    # 2: [(0, 11), (3, 10)], 3: [(5, 52), (4, 13), (2, 10)], 
    # 4: [(1, 14), (3, 13)], 5: [(0, 12), (3, 52), (1, 17)]}
    base_key = S
    path = {}
    for (v, d) in WL[base_key]:
        path[0].append(v)
        for (v1, d1) in WL[v]:
            if v1 == base_key:
                pass
            else:
                pass

                






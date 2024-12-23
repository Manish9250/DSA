def coolWorkers(AList, preference):
    indegree, topolist = {},[]

    for i in AList.keys():
        indegree[i] = 0
    
    for key in AList.keys():
        for vertex in AList[key]:
            indegree[vertex] += 1
    queue = [key for key in AList.keys() if indegree[key] == 0 ]

    while (queue):
        print(queue)
        if len(queue) > 1:
            min_index = 100
            for i in queue:
                for j in preference:
                    if preference[j] == i:
                        if j < min_index:
                            min_index = j
                            print("Min index",min_index)
            vertex = preference[min_index]
            print("Vertex: ", vertex, "index: ",min_index )
            queue.remove(vertex)
        else:
            vertex = queue.pop(0)
        topolist.append(vertex)
        for neighbour in AList[vertex]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)
    
    print(topolist)


print("test1")
AList = {0: [1, 2, 3], 1: [7], 2: [3, 5], 3: [4, 1, 8], 7: [], 5: [6, 1], 4: [5, 7], 8: [5], 6: [7]}
preference = [1, 3, 2, 6, 8, 5, 4, 0, 7]
(coolWorkers(AList, preference))

print("test2")
AList = {0: [1, 2, 3], 1: [7], 2: [3, 5], 3: [5, 1], 7: [], 5: [6, 1], 4: [5, 7], 6: [7], 8: [5]}
preference = [0, 8, 7, 5, 6, 1, 3, 2, 4]
(coolWorkers(AList, preference))


def histogram(L):
    rep_list = []
    for i in L:
        keys = [n for (n, _) in rep_list]
        if i in keys:
            for j in range(len(rep_list)):
                if rep_list[j][0] == i:
                    rep_list[j][1] += 1
        else:
            rep_list.append([i, 1])
    sorted_list = []
    m = len(sorted_list)
    for i in rep_list:
        m = len(sorted_list)
        if len(sorted_list) == 0:
            sorted_list.append((i[0], i[1]))
        else:
            for j in range(m):
                if sorted_list[j][1] < i[1]:
                    sorted_list.append((i[0], i[1]))
                else:
                    sorted_list =sorted_list[:j+1] + [(i[0], i[1])] + sorted_list[j:]



def dic_histogram(L):
    rep_list = {}
    for i in L:
        if i in rep_list.keys():
            rep_list[i] += 1
        else:
            rep_list[i] = 1
    print(rep_list)

    sorted_list = []
    for key in rep_list.keys():
        if len(sorted_list) < 1:
            sorted_list.append((key, rep_list[key]))
        else:
            if sorted_list[-1][1] <= rep_list[key]:
                sorted_list.append((key, rep_list[key]))
            elif sorted_list[0][1] >= rep_list[key]:
                sorted_list = [(key, rep_list[key])] + sorted_list[:]
    print(sorted_list)
    print(sorted(sorted_list))
    
L = [7,12,11,13,7,11,13,14,12]
dic_histogram(L)



        

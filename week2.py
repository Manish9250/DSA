def binary_search(L, k):
    (left, right) = (0, len(L)-1)
    
    while left <= right:
        mid = left+right // 2
        
        if L[mid] == k:
            return True
        
        if k < L[mid]:
            right = mid-1
        else:
            left = mid+1

L = [1,2,4,5,8,79,45,85,65,4,5,8]

def findCommonElements1(L1, L2):
    sorted(L1)
    sorted(L2)
    
    i = 0
    j = 0
    common_list = []
    
    while i < len(L1) and j < len(L2):
        if L1[i] == L2[j]:
            common_list.append(L1[i])
            i += 1
            j += 1 
        elif L1[i] < L2[j]:
            i += 1 
        else:
            j += 1 
    return common_list


def findCommonElements(L1, L2):
    # Step 1: Sort both lists
    L1.sort()  # O(n log n)
    L2.sort()  # O(n log n)

    # Step 2: Initialize two pointers and the result list
    i, j = 0, 0
    result = []

    # Step 3: Use two-pointer technique to find common elements
    while i < len(L1) and j < len(L2):
        if L1[i] == L2[j]:
            result.append(L1[i])
            i += 1
            j += 1
        elif L1[i] < L2[j]:
            i += 1
        else:
            j += 1

    return result

'''# Example Usage
L1 = [5, 8, 2]
L2 = [6, 8, 1]
print(findCommonElements(L1, L2))  # Output: [8]

print(findCommonElements1(L1, L2)) 
L1 = [3, 7, 2, 9, 5]
L2 = [6, 3, 7, 5, 4]
print(findCommonElements(L1, L2))  # Output: [3, 7, 5]

print(findCommonElements1(L1, L2)) 
L1 = [23, 24, 18, 22, 20, 10, 17, 12, 16, 19, 21, 15, 14, 11, 13]
L2 = [23, 22, 33, 24, 31, 21, 20, 26, 30, 29, 25, 27, 28, 34, 32]
print(findCommonElements(L1, L2))  # Output: [20, 21, 22, 23, 24]

print(findCommonElements1(L1, L2)) 
'''
count = 0
def merge(L):
    global count 

    if len(L) == 0:
        return 
    elif len(L) == 1:
        #count += 1
        return L
    elif len(L) == 2:
        #count += 1
        if L[0] > L[1]:
            return [L[1], L[0]]
        else:
            return L
    else:
        mid = len(L) // 2
        #new =[]
        if mid > 0:
            print(L)
            print("left: ", L[:mid], "right: ", L[mid:])
            count += 2
            left = merge(L[:mid])
            right = merge(L[mid:])

            i = j = k = 0
            
            print("left: ", left, "Right: ", right)
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    L[k] = left[i]
                    #new.append(left[i])
                    i += 1
                    print(L)
                else:
                    L[k] = right[j]
                    #new.append(right[j])

                    j += 1
                    print(L)
                k += 1

            while i < len(left):
                L[k] = left[i]
                #new.append(left[i])
                i += 1
                k += 1
                print(L)
            
            while j < len(right):
                L[k] = right[j]
                #new.append(right[j])
                j += 1
                k += 1
                print(L)
        #count += 1
        return L

        
        
    
    
'''L1 = [10, 33, 45, 67, 92, 100, 5, 99, 105]
L2 = [194, 69, 103, 150, 151, 44, 103, 98]

res =  (merge(L2))
print("res: ", res)
print(count)'''

def findPair(L, x):
    L.sort()
    print(L)
    
    for i in L:
        print("i", i)
        if i > x:
            print("step1: ", i , x//2)
            return False
        else:
            for j in L:
                print("j", j)
                if j > x:
                    print("step2: ",j , x)
                    break
                else:
                    print("i+j", i+j)
                    if (i+j) == x:
                        print("step3: ", i, j)
                        return True


L = [int(item) for item in input().split()]
pairsum = int(input())
print(findPair(L, pairsum))
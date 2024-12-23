def find_peak(L):
    low, high = 0, len(L) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if the current element is a peak
        if (mid == 0 or L[mid] > L[mid - 1]) and (mid == len(L) - 1 or L[mid] > L[mid + 1]):
            return L[mid]

        # Move to the right half if the right neighbor is greater
        if mid < len(L) - 1 and L[mid] < L[mid + 1]:
            low = mid + 1
        else:
            # Move to the left half otherwise
            high = mid - 1

# Example Usage
L1 = [1, 3, 7, 8, 9, 4, 2]
print(find_peak(L1))  # Output: 9

L2 = [10, 20, 15, 2, 23, 90, 67]
print(find_peak(L2))  # Output: 20 or 90 (either one, as both are peaks)

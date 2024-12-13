import numpy as np
import time
def LCW(u, v):
    (m, n) = (len(u), len(v))
    lcw = np.zeros((m+2, n+2))

    for i in range(1, n+1):
        lcw[0, i] = v[i-1]
    for i in range(1, n+1):
        lcw[i, 0] = v[i-1]

    maxlcw = 0
    print(lcw)
    for c in range(n, 0, -1):
        for r in range(m, 0, -1):
            if int(u[r-1]) < int(v[c-1]):
                print(u[r-1] , v[c-1])
                lcw[r, c] = 1 + lcw[r+1, c+1]
                #time.sleep(0.5)
                print(lcw)
            else:
                lcw[r, c] = max(lcw[r+1, c], lcw[r, c+1])

# For finding subsecewnce ending which value greater than the previous ones
def countSubseq(S):
    # dp[i] will store the number of subsequences ending with digit i
    dp = [0] * 10

    for ch in S:
        digit = int(ch)
        # Count subsequences ending with the current digit
        dp[digit] = 1 + sum(dp[:digit+1])

        print(digit, dp)

    return sum(dp)

# Example usage
#s = "2134"
#print(countSubseq(s))  # Expected output: 95



def max_domino_score(N, top_row, bottom_row):
    # DP array to store the maximum scores
    dp = [0] * (N + 1)
    print(dp)

    # Base cases
    dp[1] = abs(top_row[0] - bottom_row[0])
    print(dp)

    # Fill the DP table
    for i in range(2, N + 1):
        # Vertical tile at column i
        vertical_score = dp[i - 1] + abs(top_row[i - 1] - bottom_row[i - 1])
        # Two horizontal tiles at columns i-1 and i
        horizontal_score = dp[i - 2] + abs(top_row[i - 2] - top_row[i - 1]) + abs(bottom_row[i - 2] - bottom_row[i - 1])
        # Take the maximum of both
        dp[i] = max(vertical_score, horizontal_score)
        print(dp)

    return dp[N]


# Input handling
N = 4  # Number of columns
top_row = [8,6,2,3]
bottom_row = [9,7,1,2]

# Compute and output the maximum score
print(max_domino_score(N, top_row, bottom_row))

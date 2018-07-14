def get_change_making_matrix(set_of_coins, r):
    m = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]
    for i in range(r + 1):
        m[0][i] = i
    return m

def change_making(coins, n):
    m = get_change_making_matrix(coins, n)
    for c in range(1, len(coins) + 1):
        for r in range(1, n + 1):
            if coins[c - 1] == r:
                m[c][r] = 1
            elif coins[c - 1] > r:
                m[c][r] = m[c - 1][r]
            else:
                m[c][r] = min(m[c - 1][r], 1 + m[c][r - coins[c - 1]])
    return m[-1][-1]
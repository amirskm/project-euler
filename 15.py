def count_routes_dp(n: int) -> int:
    # Create a (n+1) x (n+1) grid filled with 0s
    ways = [[0] * (n + 1) for _ in range(n + 1)]

    # There's exactly 1 way to reach any cell on the top row (all Rights)
    # and 1 way to reach any cell on the left column (all Downs)
    for i in range(n + 1):
        ways[0][i] = 1
        ways[i][0] = 1

    # Fill in the rest using the rule: from top + from left
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            ways[r][c] = ways[r - 1][c] + ways[r][c - 1]

    return ways[n][n]

print(count_routes_dp(2))
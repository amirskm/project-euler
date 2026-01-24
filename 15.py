n = 20

# grid = [[1 for _ in range(n + 1)] for _ in range(n + 1)]
grid = [[1 for _ in range(n + 1)] for _ in range(n + 1)]

print(grid)


for r in range(1, n + 1):
    for c in range(1, n + 1):
        grid[r][c] = grid[r - 1][c] + grid[r][c - 1]

print(grid[n][n])
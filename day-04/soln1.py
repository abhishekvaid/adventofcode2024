from itertools import product


def solve_part1(text_buf):

    m, n = len(text_buf), len(text_buf[0])
    pattern = list("XMAS")
    res = 0

    def backtrack(i, j, idx, dx, dy):
        nonlocal res
        if 0 <= i < m and 0 <= j < n and text_buf[i][j] == pattern[idx]:
            if idx + 1 == len(pattern):
                res += 1
                return
            else:
                text_buf[i][j] = "#"
                idx += 1
                backtrack(i + dx, j + dy, idx, dx, dy)
                idx -= 1
                text_buf[i][j] = pattern[idx]

    for row in range(m):
        for col in range(n):
            if text_buf[row][col] == pattern[0]:
                if text_buf[row][col] == "X":
                    for dx, dy in [
                        [1, 0],
                        [-1, 0],
                        [0, 1],
                        [0, -1],
                        [-1, 1],
                        [-1, -1],
                        [1, -1],
                        [1, 1],
                    ]:
                        backtrack(row, col, 0, dx, dy)

    return res


def solve_part2(text_buf):

    m, n = len(text_buf), len(text_buf[0])
    pattern = list("MAS")
    res = 0

    def backtrack(i, j, idx, dx, dy):
        res = False 
        if 0 <= i < m and 0 <= j < n and text_buf[i][j] == pattern[idx]:
            if idx + 1 == len(pattern):
                res = True
            else:
                text_buf[i][j] = "#"
                idx += 1
                res = backtrack(i + dx, j + dy, idx, dx, dy)
                idx -= 1
                text_buf[i][j] = pattern[idx]
        return res 

    for row in range(m):
        for col in range(n):
            if text_buf[row][col] == pattern[0]:
                if text_buf[row][col] == "M":
                    if backtrack(row, col, 0, 1, 1) and backtrack(row+2, col, 0, -1, 1):
                        res += 1
                    if backtrack(row, col, 0, 1, -1) and backtrack(row+2, col, 0, -1, -1):
                        res += 1
                    if backtrack(row, col, 0, -1, -1) and backtrack(row, col-2, 0, -1, 1):
                        res += 1
                    if backtrack(row, col, 0, -1, 1) and backtrack(row, col+2, 0, -1, -1):
                        res += 1

    return res


text_lines = open("test_input.txt").read().splitlines()
text_buf = [list(text_line) for text_line in text_lines]

print(solve_part1(text_buf))
print(solve_part2(text_buf))

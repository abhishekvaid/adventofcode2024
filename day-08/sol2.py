from itertools import combinations, count

def read_input(fname: str) -> list[list[str]]:
    return [ list(line) for line in open(fname).read().splitlines() ]

def solve_b( buf: list[list[str]]) -> int:
    m, n = len(buf), len(buf[0])
    pos_dict: dict[str, list[tuple[int, int]]] = {}
    for i in range(m):
        for j in range(n): 
            if buf[i][j] != ".":
                pos_dict.setdefault(buf[i][j], []).append((i, j))
    seen: set[tuple[int, int]] = set()
    for _, positions in pos_dict.items():
        for (x1, y1), (x2, y2) in combinations(positions, 2):
            dx, dy = x1 - x2, y1 - y2
            for scale in count(0):
                shouldBreak = True 
                scaled_dx = scale * dx # scaled version of dx
                scaled_dy = scale * dy # scaled version of dy 
                candidate1 = (x1 + scaled_dx, y1 + scaled_dy)
                candidate2 = (x2 - scaled_dx, y2 - scaled_dy)
                for cx, cy in [candidate1, candidate2]:
                    if 0 <= cx < m and 0 <= cy < n:
                        seen.add((cx, cy))
                        buf[cx][cy] = "#"
                        shouldBreak = False
                if shouldBreak:
                    break 
                
            
    return len(seen)

buf = read_input("small_test_input.txt")
print(solve_b(buf))
buf = read_input("test_input.txt")
print(solve_b(buf))
buf = read_input("input.txt")
print(solve_b(buf))


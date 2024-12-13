

def read_input(fname) -> list[list[str]]:
    with open(fname) as fin:
        text_buf = list(map(list, fin.read().splitlines()))
    return text_buf

def solve_part_1(text_buf):
    m, n = len(text_buf), len(text_buf[0])    
    def find_initial_loc():
        for i in range(m):
            for j in range(n):
                if text_buf[i][j] == "^":
                    return(i, j)
        return (-1, -1)
    
    x, y = find_initial_loc()
    dx, dy = -1, 0
    
    res = 0        
    while 0 <= x < m and 0 <= y < n:
        nx, ny = x + dx, y + dy 
        if not (0 <= nx < m and 0 <= ny < n):
            break # you are out of the board 
        elif text_buf[nx][ny] == "#":
            dx, dy = dy, -dx
        else:
            if text_buf[nx][ny] != "*":
                text_buf[nx][ny] = "*"
                res += 1
            x, y = nx, ny 
    return res


def solve_part_2(text_buf):
    m, n = len(text_buf), len(text_buf[0])    
    def find_initial_loc():
        for i in range(m):
            for j in range(n):
                if text_buf[i][j] == "^":
                    return(i, j)
        return (-1, -1)
    
    x, y = find_initial_loc()
    text_buf[x][y] = "*"
    dx, dy = -1, 0
    
    res = 0
    dirs = dict()        
    while 0 <= x < m and 0 <= y < n:
        nx, ny = x + dx, y + dy 
        if not (0 <= nx < m and 0 <= ny < n):
            break # you are out of the board 
        elif text_buf[nx][ny] == "#":
            dx, dy = dy, -dx
        else:
            if text_buf[nx][ny] != "*":
                text_buf[nx][ny] = "*"
                dirs[(nx, ny)] = dx, dy
            else:
                 
                 
            x, y = nx, ny
         
    return res  


text_buf = read_input("test_input.txt")
print(solve_part_1(text_buf))
text_buf = read_input("test_input.txt")
print(solve_part_1(text_buf))
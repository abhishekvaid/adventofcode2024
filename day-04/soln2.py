def solve_part_2(text_buf):
    
    pattern = list("MAS")
    m, n = len(text_buf), len(text_buf[0])
    
    def convolve(i, j): 
        res = 0
        if 0 <= i < m and 0 <= j < n:
            if text_buf[i+1][j+1] == pattern[1]:
                if text_buf[i][j] == text_buf[i+2][j] == pattern[0] and text_buf[i+2][j+2] == text_buf[i][j+2] == pattern[2]:
                    res += 1
                if text_buf[i][j] == text_buf[i][j+2] == pattern[2] and text_buf[i+2][j] ==  text_buf[i+2][j+2] == pattern[0]:
                    res += 1
                if text_buf[i][j] == text_buf[i+2][j] == pattern[2] and text_buf[i][j+2] ==  text_buf[i+2][j+2] == pattern[0]:
                    res += 1
                if text_buf[i][j] == text_buf[i][j+2]  == pattern[0] and  text_buf[i+2][j+2] == text_buf[i+2][j] == pattern[2]:
                    res += 1
        return res 
    
    res = 0
    for i in range(m-2):
        for j in range(n-2):
            res += convolve(i, j)
    
    return res 

text_lines = open("input.txt").read().splitlines()
text_buf = [list(text_line) for text_line in text_lines]

print(solve_part_2(text_buf))                       
    
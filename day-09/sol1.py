def read_input(fname: str) -> list[str]:
    return list(open(fname).read())

def solve(chars: list[str]) -> int:
    buf = []
    for i, digit in enumerate(chars):
        if i & 1:
            buf.extend("." * int(digit)) 
        else:
            buf.extend([i//2] * int(digit))
    i, j = 0, len(buf)-1
    while i < j: 
        if buf[i] != ".":
            i += 1
        elif buf[j] == ".":
            j -= 1
        else:
            buf[i], buf[j] = buf[j], buf[i]
            i += 1
            j -= 1
    
    res = 0 
    for i, num in enumerate(buf):
        if num == ".":
            break 
        res += i * num
    return res 

chars = read_input("test_input.txt")
print(solve(chars))
chars = read_input("input.txt")
print(solve(chars))
import re

def read_input(fname: str) -> list[str]:
    return list(open(fname).read())

def solve(chars: list[str]) -> int:
    buf = []
    for i, digit in enumerate(chars):
        if i & 1:
            buf.extend("." * int(digit)) 
        else:
            buf.extend([i//2] * int(digit))
    j = len(buf) - 1
    while j >= 0:
        print(f"processing: {j}")
        
        while j >= 0 and buf[j] == ".":
            j -= 1
        j1 = j
        while j1 >= 0 and buf[j1] == buf[j]:
            j1 -= 1
        i = 0
        
        try:
            assert(len(set(buf[j1+1:j+1])) in [0, 1])
        except Exception as e:
            print("E",set(buf[j1+1:j+1]) )
            
        
        while i <= j:
            while i <= j and buf[i] != ".":
                i += 1
            i1 = i 
            while i1 <= j and buf[i1] == buf[i]:
                i1 += 1
            # print("Fixing in spaces   ", buf[i: i1])
            if (j - j1 <= i1 - i):
                while j > j1:
                    buf[i], buf[j] = buf[j], buf[i]
                    i += 1
                    j -= 1
                break
            i = i1 
            
        j = j1
    
    res = 0 
    for i, num in enumerate(buf):
        if num == ".":
            continue 
        res += i * num
    # print("".join(map(str, buf)))
    # print("00992111777.44.333....5555.6666.....8888..")
    return res   

# chars = read_input("test_input.txt")
# print(solve(chars))
chars = read_input("input.txt")
print(solve(chars))
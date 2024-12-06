import re 

def part1():
    regex = r"mul\((\d+),(\d+)\)"
    with open("input.txt") as fin:
        blob = fin.read()
        total = 0
        for expr in re.findall(regex, blob):
            op1, op2 = expr 
            total += int(op1) * int(op2)
        print(total)

def part2():
    regex = r"(do\(\))|(don't\(\))|(mul\((\d+),(\d+)\))"
    mode = True 
    with open("input.txt") as fin:
        blob = fin.read()
        total = 0
        for expr in re.findall(regex, blob):
            # print(expr)
            if expr[0]:
                mode = True 
            elif expr[1]:
                mode = False
            else:
                if mode:
                    op1, op2 = expr[3], expr[4]
                    total += int(op1) * int(op2)
        print(total)
        
part2()
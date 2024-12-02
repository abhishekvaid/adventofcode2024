
def solve():
    with open("input.txt") as input_file:
        lines = input_file.read().splitlines()
        list1, list2 = [], []
        for line in lines:
            token1, token2 = line.split("   ")
            list1.append(int(token1))
            list2.append(int(token2))
        list1.sort()
        list2.sort()
        return sum([ abs(num1-num2) for num1, num2 in zip(list1, list2)])
        
if __name__ == "__main__":
    print(solve())
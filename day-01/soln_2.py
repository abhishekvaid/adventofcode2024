
from collections import Counter
def solve():
    with open("input.txt") as input_file:
        lines = input_file.read().splitlines()
        list1, list2 = [], []
        for line in lines:
            token1, token2 = line.split("   ")
            list1.append(int(token1))
            list2.append(int(token2))
        counter2 = Counter(list2)
        return sum([ num * counter2.get(num, 0) for num in list1 ])
        
if __name__ == "__main__":
    print(solve())
from functools import lru_cache


def read_input(fname) -> list[tuple[int, list[int]]]:
    lines = open(fname).read().splitlines()
    res: list[tuple[int, list[int]]] = []
    for line in lines:
        total, rest = line.split(": ")
        total = int(total)
        nums: list[int] = list(map(int, rest.split(" ")))
        res.append((total, nums))
    return res 

        
     
def solve_a_case(total, nums) -> int:
    
    if len(nums) == 1:
        return total if nums[0] == total else 0
    
    @lru_cache(None)
    def backtrack(i: int, curr_val: int) -> bool:
        
        if curr_val > total and i < len(nums):
            # If any remaining numbers are > 1, multiplication would make curr_val even larger
            if all(n > 1 for n in nums[i:]):
                return False
        
        if i == len(nums):
            return curr_val == total
            
        # Try addition
        if backtrack(i + 1, curr_val + nums[i]):
            return True
            
        # Try multiplication    
        if backtrack(i + 1, curr_val * nums[i]):
            return True
        
        # Try multiplication    
        if backtrack(i + 1, curr_val * 10 ** len(str(nums[i])) + nums[i]):
            return True
            
        return False 
         
    return total if backtrack(1, nums[0]) else 0


def solve(cases: list[tuple[int, list[int]]]) -> int:
    res = 0    
    for total, nums in cases: 
        if len(nums) == 1 and nums[0] == total: 
            res += total
        else:
            res += solve_a_case(total, nums)
    return res 


cases = read_input("input.txt")
print(solve(cases))
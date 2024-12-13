from collections import defaultdict
from heapq import heapify
from collections import defaultdict
from typing import DefaultDict

def read_input(fname) -> tuple[list[list[int]], list[list[int]]]:
    with open(fname) as fin:
        lines = fin.read().splitlines()
        rules = []
        pages = []
        cur, split_token = rules, "|"
        for line in lines:
            if not line: 
                cur, split_token = pages, ","
                continue 
            cur.append(list(map(int, line.split(split_token))))
    return rules, pages


def make_graph(rules, pages: set[int]) -> tuple[dict[int, list[int]], dict[int, int]]:
    in_degree, graph = defaultdict(int), defaultdict(list)
    for x, y in rules:
        if x in pages and y in pages:
            in_degree[y] += 1
            graph[x].append(y)
    return dict(graph), dict(in_degree)
    
def solve_part_1(fname):
    rules, pages = read_input(fname)
    correct_res = 0
    in_correct_res = 0
    for page in pages: 
        graph, in_degree = make_graph(rules, set(page))
        starting_nodes = [ v for v in page if not in_degree.get(v, 0) ]
        rank = {}
        seen = set()
        
        while starting_nodes:
            for node in starting_nodes:
                rank[node] = len(rank) + 1
            stack = [ node for node in starting_nodes if node not in seen]
            starting_nodes = []
            for node in stack:
                seen.add(node)
                for next_node in graph.get(node, []):
                    if next_node not in seen:
                        in_degree[next_node] -= 1
                        if in_degree[next_node] == 0:
                            starting_nodes.append(next_node)       
        if all(rank[x] < rank[y] for x, y in zip(page, page[1:])):
            correct_res += page[len(page)//2]
        else:
            page.sort(key=lambda x: rank[x])
            in_correct_res += page[len(page)//2]
            
    return correct_res, in_correct_res 
        
print(solve_part_1("input.txt")) 
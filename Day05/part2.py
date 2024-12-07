import os
from collections import defaultdict, deque

def is_update_valid(update, rules):
    update_indices = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in update_indices and y in update_indices:
            if update_indices[x] >= update_indices[y]:
                return False
    return True

def reorder_update(update, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    update_set = set(update)

    for x, y in rules:
        if x in update_set and y in update_set:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []

    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update

def find_middle_page(update):
    mid_index = len(update) // 2
    return update[mid_index]

def calculate_corrected_updates(rules, updates):
    invalid_updates = []
    corrected_updates = []
    total_middle = 0

    for update in updates:
        if not is_update_valid(update, rules):
            invalid_updates.append(update)
            corrected_update = reorder_update(update, rules)
            corrected_updates.append(corrected_update)
            total_middle += find_middle_page(corrected_update)
    
    return total_middle, corrected_updates

os.system('cls' if os.name == 'nt' else 'clear')

with open("Day05/input.txt", "r") as input_file:
    content = input_file.read().strip()
    
rules_section, updates_section = content.split("\n\n")

rules = []
for line in rules_section.strip().split("\n"):
    x, y = map(int, line.split("|"))
    rules.append((x, y))

updates = []
for line in updates_section.strip().split("\n"):
    updates.append(list(map(int, line.split(","))))
total, corrected_updates = calculate_corrected_updates(rules, updates)

print("Corrected updates:")
for update in corrected_updates:
    print(update)

print(f"Total of middle pages from corrected updates: {total}")


import os

def is_update_valid(update, rules):
    update_indices = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in update_indices and y in update_indices:
            if update_indices[x] >= update_indices[y]:
                return False
    return True

def find_middle_page(update):
    mid_index = len(update) // 2
    return update[mid_index]

def calculate_correct_updates(rules, update):
    valid_updates = []
    total_middle = 0

    for update in updates:
        if is_update_valid(update, rules):
            valid_updates.append(update)
            total_middle += find_middle_page(update)
    
    return total_middle, valid_updates


os.system('cls' if os.name == 'nt' else 'clear')

with open("Day05/inputShort.txt", "r") as input_file:
    content = input_file.read().strip()
    
rules_section, updates_section = content.split("\n\n")

rules = []
for line in rules_section.strip().split("\n"):
    x, y = map(int, line.split("|"))
    rules.append((x, y))

updates = []
for line in updates_section.strip().split("\n"):
    updates.append(list(map(int, line.split(","))))

total, valid_updates = calculate_correct_updates(rules, updates)

print("Valid updates:")
for update in valid_updates:
    print(update)

print(f"Total of middle pages from valid updates: {total}")


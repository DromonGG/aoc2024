total = 0
list_left = []
list_right = []

with open("Day01/inputShort.txt") as input_file:
    for line in input_file:
        numbers = line.strip().split("   ")
        list_left.append(int(numbers[0]))
        list_right.append(int(numbers[1]))

list_left.sort()
list_right.sort()

for left, right in zip(list_left, list_right):
    total += abs(left - right)

print(total)
total = 0
list_left = []
list_right = []

with open("Day01/inputShort.txt") as input_file:
    for line in input_file:
        numbers = line.strip().split("   ")
        list_left.append(int(numbers[0]))
        list_right.append(int(numbers[1]))

for number_left in list_left:
    amount_on_right = list_right.count(number_left)
    total += number_left * amount_on_right

print(total)

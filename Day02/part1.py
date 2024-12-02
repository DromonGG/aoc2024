safeReports = 0

with open("Day02/input.txt") as input_file:
    for line in input_file:
        numbers = [int(num) for num in line.strip().split(" ")]
        
        isIncreasing = True
        isDecreasing = True
        isInvalid = False

        for i in range(1, len(numbers)):
            diff = numbers[i] - numbers[i - 1]
            if abs(diff) < 1 or abs(diff) > 3:
                isInvalid = True
                break
            if diff > 0:
                isDecreasing = False
            if diff < 0:
                isIncreasing = False
        if (isIncreasing or isDecreasing) and not isInvalid:
            safeReports += 1

print(safeReports)
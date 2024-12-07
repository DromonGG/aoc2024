def isSafe(numbers):
    isIncreasing = True
    isDecreasing = True

    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        if diff > 0:
            isDecreasing = False
        if diff < 0:
            isIncreasing = False
    return isIncreasing or isDecreasing


def canBeMadeSafe(numbers):
    for i in range(len(numbers)):
        modifiedReport = numbers[:i] + numbers[i + 1:]
        if isSafe(modifiedReport):
            return True
    return False

safeReports = 0

with open("Day02/inputShort.txt") as input_file:
    for line in input_file:
        numbers = [int(num) for num in line.strip().split(" ")]

        if isSafe(numbers) or canBeMadeSafe(numbers):
            safeReports += 1

print(safeReports)
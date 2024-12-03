import re

with open("Day03/inputShort.txt") as inputFile:
    content = inputFile.read()
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, content)
    totalSum = sum(int(d1) * int(d2) for d1, d2 in matches)
print(totalSum)

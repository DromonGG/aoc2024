import re

totalSum = 0
mulEnabled = True
mulPattern = r"mul\((\d{1,3}),(\d{1,3})\)"
doPattern = r"do\(\)"
dontPattern = r"don't\(\)"
combinedPattern = f"{mulPattern}|{doPattern}|{dontPattern}"

with open("Day03/input.txt") as inputFile:
    content = inputFile.read()
    for match in re.finditer(combinedPattern, content):
        token = match.group(0)
        
        if re.fullmatch(doPattern, token):
            mulEnabled = True
        elif re.fullmatch(dontPattern, token):
            mulEnabled = False
        elif re.fullmatch(mulPattern, token):
            if mulEnabled:
                d1, d2 = map(int, match.groups())
                totalSum += d1 * d2
print(totalSum)

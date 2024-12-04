import os
from rich.console import Console
from rich.table import Table

os.system('cls' if os.name == 'nt' else 'clear')

with open("Day04/input.txt") as inputFile:
    matrix = [list(row) for row in inputFile.read().strip().split("\n")]
rows = len(matrix)
cols = len(matrix[0])
highlightedMatrix = [row[:] for row in matrix]
occurrencesCount = 0

def isOutOfRange(row, column):
    if(row>rows-1 or column>cols-1 or row <0 or column < 0): 
        return True
    return False

def getPatternPositions(row, column):
    return [
        (row, column),
        (row - 1, column - 1),
        (row + 1, column + 1),
        (row - 1, column + 1),
        (row + 1, column - 1)
    ]

def findXPattern(row, column):
    patternPositions = getPatternPositions(row, column)
    if any(isOutOfRange(r, c) for r, c in patternPositions):
        return False

    if matrix[patternPositions[0][0]][patternPositions[0][1]] != "A":
        return False

    validDiagonalPairs = [("M", "S"), ("S", "M")]
    topLeft = matrix[patternPositions[1][0]][patternPositions[1][1]]
    bottomRight = matrix[patternPositions[2][0]][patternPositions[2][1]]
    topRight = matrix[patternPositions[3][0]][patternPositions[3][1]]
    bottomLeft = matrix[patternPositions[4][0]][patternPositions[4][1]]

    if (topLeft, bottomRight) in validDiagonalPairs and (topRight, bottomLeft) in validDiagonalPairs:
        return True
    return False

for row in range(rows):
    for column in range(cols):
        if findXPattern(row, column):
            positions = getPatternPositions(row, column)
            for positionRow, positionColumn in positions:
                highlightedMatrix[positionRow][positionColumn] = f"[bold green]{matrix[positionRow][positionColumn]}[/bold green]"
            occurrencesCount += 1

table = Table(title="Matrix with Highlighted X-MAS Patterns", expand=False, show_lines=True)
table.add_column("Row/Col", justify="center")
for c in range(cols):
    table.add_column(str(c), justify="center")

for r in range(rows):
    row = [str(r)] + highlightedMatrix[r]
    table.add_row(*row)

console = Console()
console.print(table)
console.print(f"[bold cyan]Number of X-MAS Patterns Found:[/bold cyan] [bold yellow]{occurrencesCount}[/bold yellow]")

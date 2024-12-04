import os
from rich.console import Console
from rich.table import Table

os.system('cls' if os.name == 'nt' else 'clear')

with open("Day04/inputNene.txt") as inputFile:
    matrix = [list(row) for row in inputFile.read().strip().split("\n")]
rows = len(matrix)
cols = len(matrix[0])
highlightedMatrix = [row[:] for row in matrix]
occurrencesCount = 0

words = ["XMAS", "SAMX"]
directions = [
    (0, 1),
    (1, 0),
    (1, 1),
    (-1,1)
]

def findWord(word, row, column, direction):
    positions = []
    for index in range(len(word)):
        if isOutOfRange(row, column) or matrix[row][column] != word[index]:
            return False, []
        positions.append((row,column))
        row += direction[0]
        column += direction[1]

    return True, positions

def isOutOfRange(row, column):
    if(row > rows-1 or column > cols-1 or row < 0 or column < 0): 
        return True
    return False

for word in words:
    for row in range(rows):
        for column in range(cols):
            for direction in directions:
                found, positions = findWord(word, row, column, direction)
                if(found):
                    for positionRow, positionColumn in positions:
                        highlightedMatrix[positionRow][positionColumn] = f"[bold green]{matrix[positionRow][positionColumn]}[/bold green]"
                    occurrencesCount += 1


table = Table(title="Matrix", expand=False, show_lines=True)
table.add_column("Row/Col", justify="center")
for c in range(cols):
    table.add_column(str(c), justify="center")

for r in range(rows):
    row = [str(r)] + highlightedMatrix[r]
    table.add_row(*row)

console = Console()
console.print(table)
console.print(f"[bold cyan]Number of Occurrences of 'XMAS' and 'SMAX':[/bold cyan] [bold yellow]{occurrencesCount}[/bold yellow]")

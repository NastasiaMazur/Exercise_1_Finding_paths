

# Phase 1:
def print_labyrinth(lab: list[str]):
 rows = len(lab)
 columns = len(lab[0])

 # Prints the top row with column numbers
 top_row = " " + "".join([str(i % 10) for i in range(columns)]) + " "
 print(top_row)

 for i in range(rows):
  row = str(i) + lab[i] + str(i)
  print(row)

 # Prints the bottom row with column numbers
 bottom_row = " " + "".join([str(i % 10) for i in range(columns)]) + " "
 print(bottom_row)


labyrinth = [
 "███████",
 "█     █",
 "█   ███",
 "█ ███ █",
 "█     █",
 "███████",
]

print_labyrinth(labyrinth)







"""

labyrinth = [
 "███████",
 "█     █",
 "█   ███",
 "█ ███ █",
 "█     █",
 "███████",
]

#print(labyrinth)
print_labyrinth(labyrinth)
"""

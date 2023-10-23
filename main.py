

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

# Phase 2:

def prompt_integer(message: str) -> int:
 while True:
  users_number = input(message)
  if users_number.isdigit():
   return int(users_number)
  else:
   print("Invalid input. Please enter a valid integer.")

# Example of how to use the prompt_integer function
#start_row = prompt_integer("Row of start: ")
#start_column = prompt_integer("Column of start: ")
#print("Start location: Row =", start_row, "Column =", start_column)

#def prompt_user_for_location(name: str) -> tuple[int, int]:

#start = prompt_user_for_location("start")

#2.2
def prompt_user_for_location(name: str) -> tuple[int, int]:
 print(f"Enter the {name} location:")
 row = prompt_integer(f"Row of {name}: ")
 column = prompt_integer(f"Column of {name}: ")
 return (row, column)


start = prompt_user_for_location("start")
end = prompt_user_for_location("end")

print("Start location:", start)
print("End location:", end)

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

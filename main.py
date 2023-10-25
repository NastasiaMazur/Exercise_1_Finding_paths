

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


# Phase 3

from collections import deque
def bfs(lab: list[str], start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
 # Define the possible moves: up, down, left, right
 moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

 # Initialize a queue to perform BFS
 queue = deque()

 # Initialize a set to keep track of visited locations
 visited = set()

 # Initialize a dictionary to store the path
 path = {}

 # Add the start location to the queue
 queue.append(start)
 visited.add(start)

 while queue:
  current = queue.popleft()

  if current == end:
   # Build and return the path
   path_list = [current]
   while current != start:
    current = path[current]
    path_list.append(current)
   path_list.reverse()
   return path_list

  for move in moves:
   new_location = (current[0] + move[0], current[1] + move[1])

   if 0 <= new_location[0] < len(lab) and 0 <= new_location[1] < len(lab[0]) and lab[new_location[0]][
    new_location[1]] == ' ' and new_location not in visited:
    queue.append(new_location)
    visited.add(new_location)
    path[new_location] = current

 return None


# Example usage:
path = bfs(labyrinth, start, end)
if path:
 print("Path from start to end:")
 for location in path:
  print(location)
else:
 print("No path found.")



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

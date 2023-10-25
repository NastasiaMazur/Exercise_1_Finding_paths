

# Phase 1:
"""
# First version for Phase 1
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
"""

# Adapted version for Phase 3

def print_labyrinth(lab: list[str], path: list[tuple[int, int]] = None):
    rows = len(lab)
    columns = len(lab[0])

    # Prints the top row with column numbers
    top_row = " " + "".join([str(i % 10) for i in range(columns)]) + " "
    print(top_row)

    for i in range(rows):
        row = str(i)
        for j in range(columns):
            if path is not None and (i, j) in path:
                row += "X"  # Replace spaces on the path with "X"
            else:
                row += lab[i][j]
        row += str(i)
        print(row)

    # Prints the bottom row with column numbers
    bottom_row = " " + "".join([str(i % 10) for i in range(columns)]) + " "
    print(bottom_row)

def replace_at_index(s, r, idx):
    return s[:idx] + r + s[idx + len(r):]
"""
labyrinth = [
 "███████",
 "█     █",
 "█   ███",
 "█ ███ █",
 "█     █",
 "███████",
]
"""

labyrinth = [
 "████████",
 "█      █",
 "█   ██ █",
 "█ █ ██ █",
 "█  █   █",
 "████████",
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
 #print(f"Enter the {name} location:")
 row = prompt_integer(f"Row of {name}: ")
 column = prompt_integer(f"Column of {name}: ")
 return (row, column)


start = prompt_user_for_location("start")
end = prompt_user_for_location("end")

print("Start location:", start)
print("End location:", end)


# Phase 3

from collections import deque

def is_traversable(lab: list[str], location: tuple[int, int]) -> bool:
    row, col = location
    if 0 <= row < len(lab) and 0 <= col < len(lab[0]) and lab[row][col] == ' ':
        return True
    return False

def bfs(lab: list[str], start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    queue = deque()
    queue.append([start])  # Start with a path containing only the start location
    visited = set()

    # Define the possible moves (up, down, left, right)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        path = queue.popleft()  # Dequeue the first path
        last = path[-1]  # Get the last location in the path

        if last == end:
            return path  # If we reached the end location, return the path

        if last not in visited:
            visited.add(last)

            for move in moves:
                next_location = (last[0] + move[0], last[1] + move[1])

                if is_traversable(lab, next_location):
                    new_path = path.copy()
                    new_path.append(next_location)
                    queue.append(new_path)

    return []  # If no path is found, return an empty list

path = bfs(labyrinth, start, end)
if path:
 print("Path from start to end:")
 for location in path:
  print(location)
else:
 print("No path found.")

# last
print_labyrinth(labyrinth, path)  # Display the labyrinth with the path



"""
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

# TO DO:
# 1 Create restrictions for users input (if it makes sense)
# Try new labyrinth

"""
Strange behaviour:
It shows the path from (5, 1) to (1, 1)
but says "No path found" from (1, 1) to (5, 1) 
"""
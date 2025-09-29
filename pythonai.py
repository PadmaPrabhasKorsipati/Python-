#simple calculator
"""""
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b!=0:
        return a/b
    else:
        print("Infinite Error")
print("Simple Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

while(True):
    choice=int(input("Enter the Operation:"))
    
    if choice == 5:
        print("Calculation successfully Completed. Goodbye!")
        break
    
    num1=int(input("ENTER FIRST NUMBER:"))
    num2=int(input("ENTER SECOND NUMBER:"))
    if(choice==1):
        print(f"Addition of two numbers={add(num1,num2)}")
    elif(choice==2):
        print(f"Substraction of two numbers={sub(num1,num2)}")
    elif(choice==3):
        print(f"Multiplication of two numbers={mul(num1,num2)}")
    elif(choice==4):
        print(f"Division of two numbers={div(num1,num2)}")
    else:
        print("Invalid Operator:Please Try Again.")
"""


#Add Matrices

"""""
A = [[1, 2, 3], [4, 5, 6],  [7, 8, 9]]

B = [   [9, 8, 7], [6, 5, 4], [3, 2, 1]]

C =[[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        C[i][j] = A[i][j] + B[i][j]

for j in C:
    for k in j:
        print(k,end=" ")
    print(" ")

"""




#Transpose Matrix

"""""
A = [ [1, 2, 3], [4, 5, 6],[7, 8, 9]]

T =[[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        T[j][i] = A[i][j]

for j in T:
    for k in j:
        print(k,end=" ")
    print(" ")

"""



#Albhabetical order

""""
sentence = input(" ")


words = sentence.lower().split()
words.sort()

print("Original Sentence:")
print(sentence)

print("\nWords in Alphabetical Order:")
for word in words:
    print(word, end=" ")

"""
#LIST OPERATIONS
"""""
# 1. Nested List
list1 = [1, 2, [3, 4], 5]
print("Nested List:", list1)

# 2. Length of List (
count = 0
for _ in list1:
    count += 1
print("Length of List:", count)

# 3. Concatenation 
list2 = [6, 7, 8]
concat_list = []
for item in list1:
    concat_list.append(item)
for item in list2:
    concat_list.append(item)
print("Concatenation Result:", concat_list)

# 4. Membership 
search_element = 4
found = False
for item in concat_list:
    # If item is a list, check inside
    if type(item) == list:
        for sub in item:
            if sub == search_element:
                found = True
                break
    elif item == search_element:
        found = True
        break
print(f"Is {search_element} in the list?", found)

# 5. Iteration
print("Iterating through concat_list:")
for item in concat_list:
    print(item, end=" ")
print()

# 6. Indexing
index_position = 3
pos = 0
element_at_index = None
for item in concat_list:
    if pos == index_position:
        element_at_index = item
        break
    pos += 1
print(f"Element at index {index_position}:", element_at_index)

# 7. Slicing 
start = 2
end = 6
print(f"Sliced list from index {start} to {end-1}:", concat_list[start:end])
"""

#LIST METHODS
# Program to demonstrate List Methods in Python

"""""
my_list = [10, 20, 30]
print("Original List:", my_list)

# 1. Append 
my_list.append(40)
print("After append(40):", my_list)

# 2. Insert 
my_list.insert(1, 15)   # Insert 15 at index 1
print("After insert(1, 15):", my_list)

# 3. Extend 
my_list.extend([50, 60, 70])
print("After extend([50, 60, 70]):", my_list)

# 4. Delete using pop 
removed_element = my_list.pop(2)   
print(f"After pop(2), removed element = {removed_element}: {my_list}")

# 5. Delete using remove 
my_list.remove(60)   
print("After remove(60):", my_list)

# 6. Delete using del statement
del my_list[0]   
print("After del my_list[0]:", my_list)

# 7. Clear the entire list
my_list.clear()
print("After clear():", my_list)
"""

#SET OPERATIONS
"""""
# Define two sets
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

print("Set A:", setA)
print("Set B:", setB)

# 1. Union
union_result = setA.union(setB)  
print("Union (A ∪ B):", union_result)

# 2. Intersection
intersection_result = setA.intersection(setB)  
print("Intersection (A ∩ B):", intersection_result)

# 3. Difference
diff_A_B = setA.difference(setB)  
diff_B_A = setB.difference(setA)  
print("Difference (A - B):", diff_A_B)
print("Difference (B - A):", diff_B_A)

# 4. Symmetric Difference
sym_diff = setA.symmetric_difference(setB)  
print("Symmetric Difference (A Δ B):", sym_diff)

# 5. Membership Test
element = 3
if element in setA:
    print(f"{element} is in Set A")
else:
    print(f"{element} is NOT in Set A")

# 6. Iteration over Set
print("Elements in Set B:")
for item in setB:
    print(item, end=" ")
print()

# 7. Add & Remove Elements
setA.add(10)
print("Set A after add(10):", setA)

setB.remove(6)
print("Set B after remove(6):", setB)
"""


#CALENDAR
"""""
def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


def get_days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28

def get_first_day(year, month):
    q = 1  # Day of month (1st)
    m = month
    y = year
    if m == 1:
        m = 13
        y -= 1
    elif m == 2:
        m = 14
        y -= 1
    K = y % 100
    J = y // 100
    h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + (5 * J)) % 7

    return (h + 5) % 7  

def print_calendar(year, month):
    days_in_month = get_days_in_month(year, month)
    first_day = get_first_day(year, month)


    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    print(f"\n   {months[month-1]} {year}")
    print("Mo Tu We Th Fr Sa Su")


    for _ in range(first_day):
        print("   ", end="")

 
    day = 1
    while day <= days_in_month:
        print(f"{day:2}", end=" ")
        first_day += 1
        if first_day % 7 == 0:
            print()  
        day += 1
    print()


year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))
print_calendar(year, month)

"""


#REMOVE PUNCTUATIONS
"""""
text = input("Enter a string: ")

punctuations = ['.', ',', '!', '?', ';', ':', '-', '_', '"', "'", '(', ')', 
                '[', ']', '{', '}', '/', '\\', '@', '#', '$', '%', '^', '&', 
                '*', '+', '=', '<', '>', '|', '`', '~']


result = ""
for char in text:
    if char not in punctuations:
        result += char

print("String without punctuations:", result)
"""

#8 PUZZLE PROBLEM
"""""
import heapq

# Goal state
goal_state = [[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 0]]  

# Find position of a value in the puzzle
def find_position(puzzle, value):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == value:
                return (i, j)

# Heuristic: Manhattan Distance
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_x, goal_y = find_position(goal_state, state[i][j])
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

# Generate possible moves
def get_neighbors(state):
    neighbors = []
    x, y = find_position(state, 0)  # blank position
    moves = [(0,1), (1,0), (0,-1), (-1,0)]  # right, down, left, up
    
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]  # copy
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Convert puzzle to tuple for hashing
def puzzle_to_tuple(state):
    return tuple(tuple(row) for row in state)

# A* Search
def solve_puzzle(start_state):
    pq = []
    heapq.heappush(pq, (0 + manhattan_distance(start_state), 0, start_state, []))
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)
        
        if state == goal_state:
            return path
        
        visited.add(puzzle_to_tuple(state))
        
        for neighbor in get_neighbors(state):
            if puzzle_to_tuple(neighbor) not in visited:
                heapq.heappush(pq, 
                               (g + 1 + manhattan_distance(neighbor), g + 1, neighbor, path + [neighbor]))
    return None

# Main Program
start_state = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

print("Initial State:")
for row in start_state:
    print(row)

solution = solve_puzzle(start_state)

if solution:
    print("\nSolution Found in", len(solution), "moves!")
    step = 1
    for state in solution:
        print(f"\nStep {step}:")
        for row in state:
            print(row)
        step += 1
else:
    print("No solution exists!")

"""


#8 QUEEN PROBLEM
"""""
N = 8  # Chessboard size

# Function to print the chessboard
def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

# Check if placing a queen at board[row][col] is safe
def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True

# Solve N-Queens using backtracking
def solve_nqueens(board, row):
    if row == N:
        print_solution(board)
        return True

    res = False
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            res = solve_nqueens(board, row + 1) or res
            board[row][col] = 0  # backtrack
    return res

# Main program
board = [[0 for _ in range(N)] for _ in range(N)]

if not solve_nqueens(board, 0):
    print("No solution exists")

"""

#WATER JUG PROBLEM
"""""

from collections import deque

# Function to solve Water Jug Problem
def water_jug_bfs(capacity1, capacity2, target):
    visited = set()
    queue = deque([(0, 0)])  # start with both jugs empty

    while queue:
        jug1, jug2 = queue.popleft()
        
        # If target is reached
        if jug1 == target or jug2 == target:
            print("Solution found:")
            print(jug1, jug2)
            return True
        
        # If already visited, skip
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        
        print("State:", jug1, jug2)
        
        # All possible moves
        possible_states = set()
        
        # 1. Fill Jug1
        possible_states.add((capacity1, jug2))
        
        # 2. Fill Jug2
        possible_states.add((jug1, capacity2))
        
        # 3. Empty Jug1
        possible_states.add((0, jug2))
        
        # 4. Empty Jug2
        possible_states.add((jug1, 0))
        
        # 5. Pour Jug1 → Jug2
        pour = min(jug1, capacity2 - jug2)
        possible_states.add((jug1 - pour, jug2 + pour))
        
        # 6. Pour Jug2 → Jug1
        pour = min(jug2, capacity1 - jug1)
        possible_states.add((jug1 + pour, jug2 - pour))
        
        for state in possible_states:
            i         queue.append((successor, path + [successor]))
    return None

# Initial state: (M_left, C_left, boat_position, M_right, C_right)
start = (3, 3, 1, 0, 0)
goal = (0, 0, 0, 3, 3)

solution = bfs(start, goal)

if solution:
    print("Steps to solve Missionaries and Cannibals Problem:\n")
    for step in solution:
        print(step)
else:
    print("No solution found.")
f state not in visited:
                queue.append(state)

    print("No solution possible")
    return False

# Main Program
cap1 = int(input("Enter capacity of Jug1: "))
cap2 = int(input("Enter capacity of Jug2: "))
target = int(input("Enter target amount: "))

water_jug_bfs(cap1, cap2, target)
"""
#CRIPT ARITHMETIC PROBLEM
"""""
import itertools

def is_valid(puzzle, letters, perm):
    mapping = dict(zip(letters, perm))
    left, right = puzzle.split("=")
    left_terms = left.split("+")
    
    try:
        left_sum = sum(int("".join(str(mapping[ch]) for ch in term.strip())) for term in left_terms)
        right_val = int("".join(str(mapping[ch]) for ch in right.strip()))
    except ValueError:
        return False
    
    return left_sum == right_val

def solve_crypt_arithmetic(puzzle):
    letters = set([ch for ch in puzzle if ch.isalpha()])
    if len(letters) > 10:
        print("Too many unique letters! (Max 10)")
        return

    letters = list(letters)

    for perm in itertools.permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))

   
        if any(mapping[word[0]] == 0 for word in puzzle.replace("+","=").split("=") if word.strip()):
            continue

        if is_valid(puzzle, letters, perm):
            print(f"\nSolution for {puzzle}:")
            for k, v in mapping.items():
                print(f"{k} = {v}")
            return
    print("No solution found.")


puzzle = input("Enter a crypt-arithmetic puzzle (e.g., SEND + MORE = MONEY): ").replace(" ", "")
solve_crypt_arithmetic(puzzle)
"""


#Missionaries Cannibal problem
"""""
from collections import deque

def is_valid(state):
    M_left, C_left, boat, M_right, C_right = state
    # Non-negative and missionaries >= cannibals if missionaries present
    if (M_left < 0 or C_left < 0 or M_right < 0 or C_right < 0):
        return False
    if (M_left > 0 and M_left < C_left):
        return False
    if (M_right > 0 and M_right < C_right):
        return False
    return True

def get_successors(state, total_M, total_C):
    M_left, C_left, boat, M_right, C_right = state
    successors = []
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]  # Possible boat moves

    for M, C in moves:
        if boat == 1:  # Boat on left
            new_state = (M_left - M, C_left - C, 0, M_right + M, C_right + C)
            move_desc = f"{M} Missionary(ies) and {C} Cannibal(s) cross LEFT → RIGHT"
        else:  # Boat on right
            new_state = (M_left + M, C_left + C, 1, M_right - M, C_right - C)
            move_desc = f"{M} Missionary(ies) and {C} Cannibal(s) cross RIGHT → LEFT"

        if is_valid(new_state) and 0 <= new_state[0] <= total_M and 0 <= new_state[1] <= total_C:
            successors.append((new_state, move_desc))
    return successors

def bfs(start, goal, total_M, total_C):
    queue = deque([(start, [], [])])  # (state, path, moves)
    visited = set()

    while queue:
        state, path, moves = queue.popleft()
        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            return path + [state], moves

        for successor, move_desc in get_successors(state, total_M, total_C):
            queue.append((successor, path + [state], moves + [move_desc]))
    return None, None

# 🔹 User Input
M = int(input("Enter number of Missionaries: "))
C = int(input("Enter number of Cannibals: "))

start = (M, C, 1, 0, 0)   # boat starts on left
goal = (0, 0, 0, M, C)    # all on right

solution, moves = bfs(start, goal, M, C)

if solution:
    print("\nSteps to solve Missionaries and Cannibals Problem:\n")
    for i in range(len(moves)):
        print(f"Step {i+1}: {moves[i]}")
        print(f"    State: {solution[i+1]}")
else:
    print("No solution found.")
"""

#VACUUM CLEANER
""""
def vacuum_cleaner(room, start=(0, 0)):
    n = len(room)
    m = len(room[0])
    x, y = start  # starting position
    moves = []

    # Helper function to check if room is clean
    def is_clean():
        return all(room[i][j] == 0 for i in range(n) for j in range(m))

    while not is_clean():
        if room[x][y] == 1:
            room[x][y] = 0
            moves.append(f"Cleaned cell ({x}, {y})")

        # Move in row-major order
        if y < m - 1:
            y += 1
            moves.append(f"Moved RIGHT to ({x}, {y})")
        elif x < n - 1:
            x += 1
            y = 0
            moves.append(f"Moved DOWN to ({x}, {y})")
        else:
            x, y = 0, 0
            moves.append("Restarted from top-left (0, 0)")

    moves.append("All cells are clean!")
    return moves

# 🔹 Taking User Input
print("Enter 2x2 Room State (1 = Dirty, 0 = Clean):")
room = []
for i in range(2):
    row = list(map(int, input(f"Enter row {i+1} (two numbers with space): ").split()))
    room.append(row)

print("\nInitial Room State:")
for r in room:
    print(r)

steps = vacuum_cleaner(room)

print("\nSteps taken by Vacuum Cleaner:")
for step in steps:
    print(step)
"""
#BFS APPROACH
"""""
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    print("\nBFS Traversal:")

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    print()

# 🔹 Taking Graph Input
graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter node {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start = input("Enter the starting node: ")

# Run BFS
bfs(graph, start)
"""

#DFS APPROACH
"""""
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    print("\nDFS Traversal (Iterative):")
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Add neighbors in reverse order for correct traversal
            stack.extend(reversed(graph[node]))
    print()

# 🔹 Taking Graph Input
graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter node {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start = input("Enter the starting node: ")

dfs_iterative(graph, start)
"""
#TRAVELLING SALESMAN
"""""
import itertools

def travelling_salesman(distance_matrix, start):
    n = len(distance_matrix)
    cities = list(range(n))
    cities.remove(start)

    min_path = None
    min_cost = float('inf')

    for perm in itertools.permutations(cities):
        current_cost = 0
        k = start
        path = [start]

        for j in perm:
            current_cost += distance_matrix[k][j]
            k = j
            path.append(j)

        current_cost += distance_matrix[k][start]  # return to start
        path.append(start)

        if current_cost < min_cost:
            min_cost = current_cost
            min_path = path

    return min_path, min_cost


# 🔹 User Input
n = int(input("Enter number of cities: "))
distance_matrix = []

print("\nEnter the distance matrix row by row:")
for i in range(n):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    distance_matrix.append(row)

start = int(input(f"\nEnter the starting city (0 to {n-1}): "))

path, cost = travelling_salesman(distance_matrix, start)

print("\nOptimal Path (Travelling Salesman Solution):")
print(" -> ".join(map(str, path)))
print(f"Minimum Cost: {cost}")
"""
#A* ALGORITHM
"""""
import heapq

class PuzzleState:
    def __init__(self, board, g, h, parent=None):
        self.board = board
        self.g = g  # cost so far
        self.h = h  # heuristic
        self.f = g + h
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

def manhattan_distance(state, goal):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal.index(state[i]), 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def get_neighbors(state):
    neighbors = []
    idx = state.index(0)
    x, y = divmod(idx, 3)
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_idx = new_x * 3 + new_y
            new_state = state[:]
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(new_state)
    return neighbors

def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    return path[::-1]

def a_star_8puzzle(start, goal):
    open_list = []
    closed_set = set()
    h = manhattan_distance(start, goal)
    start_state = PuzzleState(start, 0, h)
    heapq.heappush(open_list, start_state)
    
    while open_list:
        current = heapq.heappop(open_list)

        if current.board == goal:
            return reconstruct_path(current)

        closed_set.add(tuple(current.board))

        for neighbor in get_neighbors(current.board):
            if tuple(neighbor) in closed_set:
                continue
            g = current.g + 1
            h = manhattan_distance(neighbor, goal)
            neighbor_state = PuzzleState(neighbor, g, h, current)
            heapq.heappush(open_list, neighbor_state)
    
    return None

# 🔹 User Input
print("Enter the start state of 8-puzzle (use 0 for blank):")
start = []
for i in range(3):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    start.extend(row)

print("\nEnter the goal state of 8-puzzle (use 0 for blank):")
goal = []
for i in range(3):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    goal.extend(row)

solution = a_star_8puzzle(start, goal)

if solution:
    print("\nSteps to solve the 8-Puzzle using A*:\n")
    for step in solution:
        for i in range(0, 9, 3):
            print(step[i:i+3])
        print()
else:
    print("No solution found.")

"""
#TIC TAC TOE GAME
"""""
def print_board(board):
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    moves = 0
    current_player = "X"

    while moves < 9:
        print_board(board)
        print(f"Player {current_player}'s turn")

        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
        except ValueError:
            print("Invalid input! Enter numbers only.")
            continue

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = current_player
            moves += 1

            if check_winner(board, current_player):
                print_board(board)
                print(f"\nPlayer {current_player} wins!")
                return
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move! Try again.")

    print_board(board)
    print("\nIt's a draw!")

# 🔹 Run the game
tic_tac_toe()
"""
#MIN MAX ALGORITHM
""""
import math

def print_board(board):
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":  # AI wins
        return 1
    elif winner == "X":  # Human wins
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("You are X, AI is O")
    turn = "X"

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"\n{winner} wins!")
            break
        if is_full(board):
            print("\nIt's a draw!")
            break

        if turn == "X":
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
            except ValueError:
                print("Invalid input. Try again.")
                continue
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = "X"
                turn = "O"
            else:
                print("Invalid move, try again.")
        else:
            print("\nAI is making a move...")
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = "O"
            turn = "X"

# 🔹 Run the game
tic_tac_toe()
"""
#ALPHA BETA PRUNING
"""""
import math

def print_board(board):
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def alphabeta(board, depth, alpha, beta, is_maximizing):
    winner = check_winner(board)
    if winner == "O":  # AI wins
        return 1
    elif winner == "X":  # Human wins
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = alphabeta(board, depth + 1, alpha, beta, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = alphabeta(board, depth + 1, alpha, beta, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = alphabeta(board, 0, -math.inf, math.inf, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("You are X, AI is O")
    turn = "X"

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"\n{winner} wins!")
            break
        if is_full(board):
            print("\nIt's a draw!")
            break

        if turn == "X":
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
            except ValueError:
                print("Invalid input. Try again.")
                continue
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = "X"
                turn = "O"
            else:
                print("Invalid move, try again.")
        else:
            print("\nAI is making a move...")
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = "O"
            turn = "X"

# 🔹 Run the game
tic_tac_toe()
"""

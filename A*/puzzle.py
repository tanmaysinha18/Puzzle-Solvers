from solver import Node
from random import shuffle, randint
from time import sleep

def hash_(matrix):
  string = ""
  for i in matrix:
    for char in i: 
      string = string + (str(char) if char != " " else '0')
  return int(string)


def choose_next(states):
  array = []
  for state in states:
    h = state.heuristic()
    array.append((state,state.depth + h))
  array.sort(key = lambda x:x[1])
  return array[0][0]
  #return states[0]

n = 4
m = 4
x = 0
y = 0

x = 1
matrix = [[" " for j in range(m)] for i in range(n)]
for i in range(n):
  for j in range(m):
    matrix[i][j] = x
    x = x + 1
matrix[n - 1][m - 1] = " "
start_state = Node(matrix,0,None)

num = randint(0,100)

print("The maximum number of moves required = " + str(num))
for i in range(num):
  states = start_state.generate_successors()
  shuffle(states)
  start_state = Node(states[0].matrix,0,None)


#matrix = [[1,2,3,4],[5,6,12,7],[9,10," ",11],[13,14,15,8]]
#start_state = Node(matrix, 0,None) 

start_state.print_matrix()
curr_state = start_state
frontier = []
game_over = False
hash_list = []
max_depth = 0
print("Please wait, searching for solutions")
while not game_over:
  new_states = curr_state.generate_successors()
  for state in new_states:
    if hash_(state.matrix) not in hash_list:
      frontier.append(state)
      hash_list.append(hash_(state.matrix))
  curr_state = choose_next(frontier)
  if curr_state.depth > max_depth:
    max_depth = curr_state.depth
    print("Reaached depth = ",max_depth)
  frontier.remove(curr_state)
  # print(curr_state.depth)
  # curr_state.print_matrix()
  if curr_state.check_goal_state():
    game_over = True

print("Solution found!!!")

frontier.clear()

while curr_state.parent:
  frontier.append(curr_state)
  curr_state = curr_state.parent

frontier.append(curr_state)
print("Number of moves = " + str(len(frontier)))
while frontier:
  sleep(1)
  frontier.pop().print_matrix()
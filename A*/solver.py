from copy import deepcopy

class Node():
  def __init__(self,matrix,depth, parent):
    self.matrix = matrix
    self.depth = depth
    self.parent = parent

  def check_goal_state(self):
    x = 1
    n = len(self.matrix)
    m = len(self.matrix[0])

    for i in range(n):
      for j in range(m):
        if not self.matrix[i][j] == x and not self.matrix[i][j] == " ":
          return False
        x = x + 1

    return True

  def print_matrix(self):
    for i in self.matrix:
      for j in i:
        print(j,end = "\t")

      print()
    print("----------")

  def heuristic(self):
    n = len(self.matrix)
    m = len(self.matrix[0])
    x = 0
    y = 0
    correct_positions = []
    for i in range(1,n*m):
      correct_positions.append((x,y))
      y = y + 1
      if y == m:
        y = 0
        x = x + 1
    h = 0
    for i in range(n):
      for j in range(m):
        if not self.matrix[i][j] == " ":
          (x,y) = correct_positions[self.matrix[i][j] - 1]
          h = h + abs(x - i) + abs(y - j)

    return h



  def choose_best(self,states):
    array = []
    for state in states:
      h = state.heuristic()
      array.append((state,state.depth + h))

    array.sort(key = lambda x:x[1])
    return array[0][0]

  def generate_successors(self):
    new_depth = self.depth + 1
    states = []
    n = len(self.matrix)
    m = len(self.matrix[0])
    for i in range(n):
      for j in range(m):
        if self.matrix[i][j] == " ":
          x = i
          y = j

    up = (x - 1 if x > 0 else 0, y)
    down = (x + 1 if x +1 < n else x,y)
    left = (x, y - 1 if y > 0 else y)
    right = (x,y + 1 if y + 1 < m else y)

    up_matrix = deepcopy(self.matrix)
    up_matrix[up[0]][up[1]], up_matrix[x][y] = up_matrix[x][y], up_matrix[up[0]][up[1]]

    down_matrix = deepcopy(self.matrix)
    down_matrix[down[0]][down[1]], down_matrix[x][y] = down_matrix[x][y], down_matrix[down[0]][down[1]]

    right_matrix = deepcopy(self.matrix)
    right_matrix[right[0]][right[1]], right_matrix[x][y] = right_matrix[x][y], right_matrix[right[0]][right[1]]

    left_matrix = deepcopy(self.matrix)
    left_matrix[left[0]][left[1]], left_matrix[x][y] = left_matrix[x][y], left_matrix[left[0]][left[1]]

    states.append(Node(up_matrix,new_depth, self))
    states.append(Node(down_matrix,new_depth, self))
    states.append(Node(left_matrix,new_depth, self))
    states.append(Node(right_matrix,new_depth, self))
    return states

  def move(self):
    new_states = self.generate_successors()
    return self.choose_best(new_states)
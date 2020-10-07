import numpy as np
from copy import deepcopy
# import matplotlib.pyplot as plt

def P(E_s,E_new,T):
    if E_new < E_s:
        return 1.0
    else:
        return np.exp(-(E_new - E_s)/T)

class Sudoku:
    def __init__(self, n = 9, string = "none"):
        self.grid = [["_" for i in range(n)] for j in range(n)]
        self.n = n
        if string != "none":
            self.grid = []
            elements = string.split(" ")
            position = 0
            for i in range(n):
                row = []
                for j in range(n):
                    row.append(int(elements[position]) if elements[position] != "_" else "_")
                    position += 1
                self.grid.append(row)
    def print_grid(self,grid = None):
        if grid:
            n = self.n
            print("------------------------")
            for i in range(n):
                for j in range(n):
                    if j == 0:
                        print("|", end = " ")
                    print(grid[i][j],end = " ")
                    if j % 3 == 2:
                        print("|", end = " ")
                print()
                if i % 3 == 2:
                    print("------------------------")
            return
        n = self.n
        print("------------------------")
        
        for i in range(n):
            for j in range(n):
                if j == 0:
                    print("|", end = " ")
                print(self.grid[i][j],end = " ")
                if j % 3 == 2:
                    print("|", end = " ")
            print()
            if i % 3 == 2:
                print("------------------------")

    def grid_check(self,x,y,val,grid):
        i,j = x//3,y//3
        values = []
        for u in range(3):
            for v in range(3):
                values.append(grid[3*i+v][3*j+u])
        # print(values)
        return not val in values

    def row_check(self,x,y,val):
        values = []
        for i in range(9):
            values.append(self.grid[y][i])
        # print(values)
        return val in values

    def col_check(self,x,y,val):
        values = []
        for i in range(9):
            values.append(self.grid[i][x])
        print(values)
        return val in values

    def valid_input(self,x,y,val):
        return self.grid_check(x,y,val) and self.row_check(x,y,val) and self.col_check(x,y,val)
    
    def get_score(self, sim_grid):
        # Score is the number of repetitions in each row, column and grid added together.
        # We want to minimize the score
        score = 0

        #Cols
        for i in range(9):
            r_i = []
            for j in range(9):
                r_i.append(sim_grid[j][i])
            for j in range(1,10):
                number = r_i.count(j)
                if number >= 2:
                    score += number - 1
        
        #Cols
        for i in range(9):
            r_i = []
            for j in range(9):
                r_i.append(sim_grid[i][j])
            for j in range(1,10):
                number = r_i.count(j)
                if number >= 2:
                    score += number - 1
        
        #Grids
        for x in range(3):
            for y in range(3):
                grid = []
                i,j = x,y
                for u in range(3):
                    for v in range(3):
                        grid.append(sim_grid[3*j+v][3*i+u])
                for u in range(1,10):
                    number = grid.count(u)
                    if number >= 2:
                        score += number - 1
        return score



    def simulated_annealing(self):
        # Fill in random values in unfilled positions
        sim_grid = deepcopy(self.grid)
        scores = []
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == "_":
                    stop = False
                    while not stop:
                        val = np.random.randint(1,10)
                        if self.grid_check(i,j,val,sim_grid):
                            sim_grid[i][j] = val
                            stop = True
                else:
                    sim_grid[i][j] = self.grid[i][j]
        # self.print_grid(sim_grid)
        # return
        iters = 0
        T = 100000
        T_0 = 100000
        c = 0.99
        halt = False
        while iters < 1000000 and not halt:
            E_s = self.get_score(sim_grid)
            S_new = deepcopy(sim_grid)
            stop = False
            while not stop:
                i,j = np.random.randint(0,9,2)
                u,v = np.random.randint(0,9,2)
                if self.grid[i][j] == "_" and self.grid[u][v] == "_":
                    S_new[i][j],S_new[u][v] = S_new[u][v], S_new[i][j]
                    stop = True
            E_new = self.get_score(S_new)
            if P(E_s,E_new, T) >= np.random.random():
                sim_grid = deepcopy(S_new)
            iters += 1
            if iters % 1000 == 0:
                # scores.append(E_s)
                self.print_grid(sim_grid)
                print("iters = ",iters, " score = ", self.get_score(sim_grid), " T = ", T)
            T = c*T
            halt = E_s == 0
        # plt.plot(scores)
        self.print_grid(sim_grid)
        # plt.show()





if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please give file")
        exit()
    filename = sys.argv[1]
    f = open(filename,"r")
    text = f.read()
    sudoku = Sudoku(string = text)
    sudoku.print_grid()
    sudoku.simulated_annealing()
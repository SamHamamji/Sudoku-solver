class Sudoku:
    def __init__(self, grid):
        self.grid = grid

    def __repr__(self):
        return (str([self.square(0, 0), self.square(1, 0), self.square(2, 0)])+' '+str([self.square(3, 0), self.square(4, 0), self.square(5, 0)])+' '+str([self.square(6, 0), self.square(7, 0), self.square(8, 0)])+'\n' + str([self.square(0, 1), self.square(1, 1), self.square(2, 1)])+' '+str([self.square(3, 1), self.square(4, 1), self.square(5, 1)])+' '+str([self.square(6, 1), self.square(7, 1), self.square(8, 1)])+'\n' + str([self.square(0, 2), self.square(1, 2), self.square(2, 2)])+' '+str([self.square(3, 2), self.square(4, 2), self.square(5, 2)])+' '+str([self.square(6, 2), self.square(7, 2), self.square(8, 2)])+'\n\n' + str([self.square(0, 3), self.square(1, 3), self.square(2, 3)])+' '+str([self.square(3, 3), self.square(4, 3), self.square(5, 3)])+' '+str([self.square(6, 3), self.square(7, 3), self.square(8, 3)])+'\n' + str([self.square(0, 4), self.square(1, 4), self.square(2, 4)])+' '+str([self.square(3, 4), self.square(4, 4), self.square(5, 4)])+' '+str([self.square(6, 4), self.square(7, 4), self.square(8, 4)])+'\n' + str([self.square(0, 5), self.square(1, 5), self.square(2, 5)])+' '+str([self.square(3, 5), self.square(4, 5), self.square(5, 5)])+' '+str([self.square(6, 5), self.square(7, 5), self.square(8, 5)])+'\n\n' + str([self.square(0, 6), self.square(1, 6), self.square(2, 6)])+' '+str([self.square(3, 6), self.square(4, 6), self.square(5, 6)])+' '+str([self.square(6, 6), self.square(7, 6), self.square(8, 6)])+'\n' + str([self.square(0, 7), self.square(1, 7), self.square(2, 7)])+' '+str([self.square(3, 7), self.square(4, 7), self.square(5, 7)])+' '+str([self.square(6, 7), self.square(7, 7), self.square(8, 7)])+'\n' + str([self.square(0, 8), self.square(1, 8), self.square(2, 8)])+' '+str([self.square(3, 8), self.square(4, 8), self.square(5, 8)])+' '+str([self.square(6, 8), self.square(7, 8), self.square(8, 8)])+'\n')
        # def get_line(y):
        #     nums = []
        #     for x in range(9):
        #         nums.append(str(self.square(y, x)))
        #     return ''.join(nums)
        # lines = []
        # for y in range(9):
        #     if y % 3 == 0:
        #         lines.append('+---+---+---+')
        #     current_line = get_line(y)
        #     line = '|' + current_line[0:3] + '|' + \
        #         current_line[3:6]+'|'+current_line[6:9]+'|'
        #     lines.append(line)
        # lines.append('+---+---+---+')
        # return '\n'.join(lines)

    def square(self, x, y):
        return (self.grid[y][x] if type(self.grid[y][x]) == int else 0)

    def line(self, y):
        return (self.grid[y])

    def column(self, x):
        return (list(self.grid[c][x] for c in range(0, 9)))

    def big_square(self, x, y):
        x -= x % 3
        y -= y % 3
        return ([z for line in self.grid[y:y+3] for z in line[x:x+3]])

    def impossibilities(self, x, y):
        return (set([i for i in self.line(y)+self.column(x)+self.big_square(x, y) if i in [1, 2, 3, 4, 5, 6, 7, 8, 9]]))

    def possibilities(self, x, y):
        return (set([1, 2, 3, 4, 5, 6, 7, 8, 9])-self.impossibilities(x, y))

    def calculate_possibilities(self):
        for y in range(9):
            for x in range(9):
                if type(self.grid[y][x]) == set or self.grid[y][x] == 0:
                    self.grid[y][x] = self.possibilities(x, y)

    def depression(self, x, y):
        return (type(self.grid[y][x]) == set and len(self.grid[y][x]) == 1)

    def uniqueness_in_line(self, y):
        '''takes a line and return what numbers of this line are a possibility in a unique square'''
        unique_numbers = []
        possibilities_of_line = [e for c in self.line(y) if type(
            c) == set for e in c if e not in [f for f in self.line(y) if type(f) == int]]
        for possibility in possibilities_of_line:
            if possibilities_of_line.count(possibility) == 1:
                unique_numbers.append(
                    (possibility, [self.line(y).index(s) for s in self.line(y) if type(s) == set and possibility in s][0]))
        return (unique_numbers)

    def uniqueness_in_column(self, x):
        '''takes a column and return what numbers of this column are a possibility in a unique square'''
        unique_numbers = []
        possibilities_of_column = [e for c in self.column(x) if type(
            c) == set for e in c if e not in [f for f in self.column(x) if type(f) == int]]
        for possibility in possibilities_of_column:
            if possibilities_of_column.count(possibility) == 1:
                unique_numbers.append((possibility, [self.column(x).index(
                    s) for s in self.column(x) if type(s) == set and possibility in s][0]))
        return (unique_numbers)

    def uniqueness_in_big_square(self, x, y):
        unique_numbers = []
        possibilities_of_big_square = [e for c in self.big_square(x, y) if type(
            c) == set for e in c if e not in [f for f in self.big_square(x, y) if type(f) == int]]
        for possibility in possibilities_of_big_square:
            if possibilities_of_big_square.count(possibility) == 1:
                unique_x = [self.big_square(x, y).index(s) for s in self.big_square(
                    x, y) if type(s) == set and possibility in s][0]
                unique_y = y - y % 3 + unique_x//3
                unique_x = x - x % 3 + unique_x % 3
                unique_numbers.append((possibility, unique_x, unique_y))
        return (unique_numbers)

    def global_uniqueness(self):
        '''if a number is valid in only one square of a line/column/bigsquare, chooses that number
        needs the possibilities calculated'''
        for y in range(9):
            for (number, index) in self.uniqueness_in_line(y):
                self.grid[y][index] = number
        for x in range(9):
            for (number, index) in self.uniqueness_in_column(x):
                self.grid[index][x] = number
        for y in [0, 3, 6]:
            for x in [0, 3, 6]:
                for (number, x_of_number, y_of_number) in self.uniqueness_in_big_square(x, y):
                    self.grid[y_of_number][x_of_number] = number

    def global_depression(self):
        '''if only one number is valid in a square, chooses that number
        needs the possibilities calculated'''
        for x in range(9):
            for y in range(9):
                if self.depression(x, y):
                    self.grid[y][x] = list(self.grid[y][x])[0]

    def finished(self):
        for x in range(9):
            for y in range(9):
                if self.grid[y][x] not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    return (False)
        return (True)

#!/usr/bin/env python
# https://www.codewars.com/kata/52423db9add6f6fc39000354
from copy import deepcopy


def next_gen(cells):
    next_gen = [[0 for cell in row] for row in cells]
    for x, row in enumerate(cells):
        for y, cell in enumerate(row):
            neighbors = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if (dx!=0 or dy!=0) and (x+dx >= 0 and x+dx < len(cells)) and (y+dy >= 0 and y+dy < len(cells[0])):
                        neighbors = neighbors+cells[x+dx][y+dy]
            if cell and neighbors < 2 or neighbors > 3:
                next_gen[x][y] = 0
            elif not cell and neighbors == 3:
                next_gen[x][y] = 1
            else:
                next_gen[x][y] = cells[x][y]
    return next_gen


def get_generation(cells, generations):
    curr_gen = deepcopy(cells)
    for _ in range(generations):
        for func in (add_space, next_gen, crop):
            curr_gen = func(curr_gen)
    return curr_gen


def add_space(cells):
    return [[0]+row+[0] for row in [[0]*len(cells[0])]+cells+[[0]*len(cells[0])]] if cells else cells


def crop(cells):
    if not len(cells) or not len(cells[0]):
        return cells
    mincol = min(row.index(1) if 1 in row else len(row) for row in cells)
    maxcol = max(len(row)-row[-1::-1].index(1)-1 if 1 in row else 0 for row in cells)
    minrow = min(col.index(1) if 1 in col else len(col) for col in list(zip(*cells)))
    maxrow = max(len(col)-col[-1::-1].index(1)-1 if 1 in col else 0 for col in list(zip(*cells)))
    return [row[mincol:maxcol+1] for row in cells[minrow:maxrow+1]]


def htmlize(array):
    s = []
    for row in array:
        for cell in row:
            s.append('▓▓' if cell else '░░')
        s.append('\n')
    return ''.join(s)


if __name__ == "__main__":
    start = [[0,0,0,0],
             [0,0,1,0],
             [0,1,0,0],
             [0,1,0,0],
             [0,1,0,0],
             [0,1,0,0],
             [0,0,1,0],
             [0,0,0,0]]
    for gen in range(5):
        print(htmlize(get_generation(start, gen)))
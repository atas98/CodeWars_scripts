#!/usr/bin/env python
# https://www.codewars.com/kata/525fbff0594da0665c0003a3


def next_gen(cells):
    next_gen = [[0 for cell in row] for row in cells]
    for x, row in enumerate(cells):
        for y, cell in enumerate(row):
            neighbors = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if (dx != 0 or dy != 0) and (x+dx >= 0 and x+dx < len(cells)) and (y+dy >= 0 and y+dy < len(cells[0])):
                        neighbors = neighbors+cells[x+dx][y+dy]
            if cell and neighbors < 2 or neighbors > 3:
                next_gen[x][y] = 0
            elif not cell and neighbors == 3:
                next_gen[x][y] = 1
            else:
                next_gen[x][y] = cells[x][y]
    return next_gen


def htmlize(array):
    s = []
    for row in array:
        for cell in row:
            s.append('▓▓' if cell else '░░')
        s.append('\n')
    return ''.join(s)


if __name__ == "__main__":
    start = [[1, 0, 0],
             [0, 1, 1],
             [1, 1, 0]]
    end = [[0, 1, 0],
           [0, 0, 1],
           [1, 1, 1]]
    result = next_gen(start)
    assert end == result, str(result)+'\n'+str(end)
    print(htmlize(start))
    print(htmlize(result))
    print(htmlize(end))

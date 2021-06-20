#!/usr/bin/env python
# https://www.codewars.com/kata/5672682212c8ecf83e000050

from time import time


def get_index(a, x) -> int:
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x:
            hi = mid
        else:
            return -1
    return mid if midval > x else mid+1


def dbl_linear(n):
    u = [1]
    i = 0
    n_max = 3*n/2

    for _ in range(int(n_max/2)):
        new_y, new_z = 2*u[i] + 1, 3*u[i] + 1
        new_y_i = get_index(u, new_y)
        if new_y_i != -1:
            u.insert(new_y_i, new_y)
        new_z_i = get_index(u, new_z)
        if new_z_i != -1:
            u.insert(new_z_i, new_z)
        i = i + 1

    return u[n]


if __name__ == "__main__":
    print(dbl_linear(10), 22)
    print(dbl_linear(20), 57)
    print(dbl_linear(30), 91)
    print(dbl_linear(50), 175)

    t_0 = time()
    dbl_linear(50000)
    print(time()-t_0)

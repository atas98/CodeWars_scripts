#!/usr/bin/env python
# https://www.codewars.com/kata/53d40c1e2f13e331fc000c26

from scipy.constants import golden as phi


# TODO: Still bad accuracy
def binetsfib(n):
    return (phi**n-(-phi)**-n)/(2*phi-1)


def recursivefib(n):
    if n <= 1:  
        return n  
    else:  
        return(recursivefib(n-1) + recursivefib(n-2))


if __name__ == "__main__":
    for n in range(0, -10, -1):
        bnfib = binetsfib(n)
        # recfib = recursivefib(n)
        # e = abs(bnfib-recfib)
        print(n, int(bnfib))
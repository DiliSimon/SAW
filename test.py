#-----------------------------------------------------------------------
# selfavoid.py
#-----------------------------------------------------------------------
import stdarray
import math
import random
from collections import defaultdict
import sys


def import_experiment_data(filename):
    p = list()
    n = list()
    with open(filename, 'r') as f:
        arr = f.read().split('\n')[1:]
    for row in arr:
        temp = row.split()
        n.append(float(temp[0]))
        p.append(float(temp[3]))
    return p,n


def import_data(filename):
    vec = list()
    with open(filename, 'r') as f:
        arr = f.read().split('\n')[1:]
    for row in arr:
        temp = row.split()
        temp[0] = int(temp[0])
        temp[1] = int(temp[1])
        vec.append(temp)
    return vec


def experiment(n, trials):
    num_dead = 0
    for t in range(trials):

        # Create an n-by-n array, with all elements set to False.
        a = stdarray.create2D(100, 100, False)

        x = n//2
        y = n//2
        step = 0
        while step < n:
            # Check for dead end and make a random move.
            a[x][y] = True
            #if a[x-1][y] and a[x+1][y] and a[x][y-1] and a[x][y+1]:
            #    print('dead')
            #    num_dead += 1
            #    break
            r = random.randrange(1, 5)
            if (r == 1) and (not a[x+1][y]):
                x += 1
            elif (r == 2) and (not a[x-1][y]):
                x -= 1
            elif (r == 3) and (not a[x][y+1]):
                y += 1
            elif (r == 4) and (not a[x][y-1]):
                y -= 1
            if a[x][y]:
                num_dead += 1
                break
            step += 1
    p_bar = (trials-num_dead)/trials
    variance = p_bar*(1-p_bar)/trials
    std = math.sqrt(variance)
    upperbound = p_bar + 1.96*std
    lowerbound = p_bar - 1.96*std
    return p_bar, upperbound, lowerbound

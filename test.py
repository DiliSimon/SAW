#-----------------------------------------------------------------------
# selfavoid.py
#-----------------------------------------------------------------------
import stdarray
import sys
import random

# Accept integers n and trialCount as command-line arguments. Do
# trialCount random self-avoiding walks in an n-by-n lattice.
# Write to standard output the percentage of dead ends encountered.

n      = int(sys.argv[1])
trials = int(sys.argv[2])
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
        if   (r == 1) and (not a[x+1][y]):
            x += 1
        elif (r == 2) and (not a[x-1][y]):
            x -= 1
        elif (r == 3) and (not a[x][y+1]):
            y += 1
        elif (r == 4) and (not a[x][y-1]):
            y -= 1
        if a[x][y]:
            num_dead+=1
            break
        step += 1
print(trials-num_dead)
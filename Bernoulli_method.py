import test

for i in range(20):
    p_bar, upperbound, lowerbound = test.experiment(i, 100000)
    print(p_bar, upperbound, lowerbound)

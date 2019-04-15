from test import import_experiment_data

p, n = import_experiment_data('data.tsv')

for idx, step in enumerate(n):
    p_bar = p[idx]
    cc = (p_bar * (4 ** step)) ** (1/step)
    lower = 4*(p_bar - 1.96 * ((p_bar*(1-p_bar)/1500000)**(1/2)))**(1/step)
    upper = 4*(p_bar + 1.96 * ((p_bar*(1-p_bar)/1500000)**(1/2)))**(1/step)
    print('{:<60s}{:<60s}{:<60s}{:<60s}'.format(str(step), str(lower), str(cc), str(upper)))

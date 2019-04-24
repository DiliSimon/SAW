import test


def main():
    real_number = []
    for i in range(1, 95):
        real_number.append([i, 0])
    print('{:s},{:s},{:s},{:s},{:s},{:s},{:s},{:s},{:s}'.format('num_step', 'Cn', 'p_real',
                                                                                   'p_bar', 'upperbound', 'lowerbound',
                                                                                   'cc_lower','cc','cc_upper'))
    for i in real_number:
        num_step = i[0]
        Cn = i[1]
        p_real = Cn/(4*(3**(num_step - 1)))
        p_bar, upperbound, lowerbound = test.experiment(num_step, 1500000)
        cc = (p_bar * (4*(3**(num_step - 1)))) ** (1 / num_step)
        lower = (4*(3**(num_step - 1)) * (p_bar - 1.96 * ((p_bar * (1 - p_bar) / 1500000) ** (1 / 2)))) ** (1 / num_step)
        upper = ((4*(3**(num_step - 1))) * (p_bar + 1.96 * ((p_bar * (1 - p_bar) / 1500000) ** (1 / 2)))) ** (1 / num_step)
        print('{:s},{:s},{:s},{:s},{:s},{:s},{:s},{:s},{:s}'.format(str(num_step), str(Cn), str(p_real), str(p_bar),
                                                                                       str(upperbound), str(lowerbound),
                                                                                       str(lower), str(cc), str(upper)))


if __name__ == '__main__':
    main()

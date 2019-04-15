import test


def main():
    real_number = []
    # real_number = test.import_data('saw_number')
    for i in range(28, 45):
        real_number.append([i, 0])
    print('{:<60s}{:<60s}{:<60s}{:<60s}{:<60s}{:<60s}{:<60s}{:<60s}{:<60s}'.format('num_step', 'Cn', 'p_real',
                                                                                   'p_bar', 'upperbound', 'lowerbound',
                                                                                   'cc_lower','cc','cc_upper'))
    for i in real_number:
        num_step = i[0]
        Cn = i[1]
        p_real = Cn/(4 ** num_step)
        p_bar, upperbound, lowerbound = test.experiment(num_step, 1500000)
        cc = (p_bar * (4 ** num_step)) ** (1 / num_step)
        lower = 4 * (p_bar - 1.96 * ((p_bar * (1 - p_bar) / 1500000) ** (1 / 2))) ** (1 / num_step)
        upper = 4 * (p_bar + 1.96 * ((p_bar * (1 - p_bar) / 1500000) ** (1 / 2))) ** (1 / num_step)
        print('{:<60s}{:<60s}{:<60s}{:<60s}{:<60s}{:<60s}{:<60s}{:<60s}{:<60s}'.format(str(num_step), str(Cn), str(p_real), str(p_bar),
                                                                                       str(upperbound), str(lowerbound),
                                                                                       str(lower), str(cc), str(upper)))


if __name__ == '__main__':
    main()

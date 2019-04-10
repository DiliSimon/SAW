import test


def main():
    real_number = test.import_data('saw_number')
    real_number.append([28, 0])
    real_number.append([29, 0])
    real_number.append([30, 0])
    real_number.append([31, 0])
    real_number.append([32, 0])
    real_number.append([33, 0])
    real_number.append([34, 0])
    real_number.append([35, 0])
    print('{:<60s}{:<60s}{:<60s}{:<60s}{:<60s}{:<60s}'.format('num_step', 'Cn', 'p_real', 'p_bar', 'upperbound', 'lowerbound'))
    for i in real_number:
        num_step = i[0]
        Cn = i[1]
        p_real = Cn/(4 ** num_step)
        p_bar, upperbound, lowerbound = test.experiment(num_step, 1500000)
        print('{:<60s}{:<60s}{:<60s}{:<60s}{:<60s}{:<60s}'.format(str(num_step), str(Cn), str(p_real), str(p_bar), str(upperbound), str(lowerbound)))


if __name__ == '__main__':
    main()

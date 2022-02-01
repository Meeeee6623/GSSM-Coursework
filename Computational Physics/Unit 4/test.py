def pi(precision):
    return sum(1 / 16 ** k *
               (4 / (8 * k + 1) -
                2 / (8 * k + 4) -
                1 / (8 * k + 5) -
                1 / (8 * k + 6)) for k in range(precision))


1 / 16 ** i * \
                (4 / (8 * i + 1) -
                 2 / (8 * i + 4) -
                 1 / (8 * i + 5) -
                 1 / (8 * i + 6))


print(pi(2))

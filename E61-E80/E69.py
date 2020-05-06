## Fifteen approximations of π


def approx_pi(num):
    pi = 3
    a = 2
    b = 3
    c = 4
    for poopoo in range(num+1):
        series = 4 / (a * b * c)
        pi += series
        a += 2
        b += 2
        c += 2
        pi = pi * -1
        if pi < 0:
            print("For iteration {}, π = {}".format(poopoo, (pi*-1)))
        else:
            print("For iteration {}, π = {}".format(poopoo, pi))

approx_pi(15)
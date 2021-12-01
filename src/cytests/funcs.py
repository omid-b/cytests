
def hello():
    msg = f"Hello from Python!"
    return msg


def fib(n):
    """return the n's fibonacci number"""
    a, b = 0.0, 1.0
    for i in range(n):
        a, b = a+b, a
    return a


def calc_pi(niter):
    """return approximated pi using pi=4arctg(1) after niter number of iteration"""
    atan1 = 0
    for i in range(niter):
        sign = (-1) ** i
        atan1 += sign / ((2 * i) + 1)
    pi = 4*atan1
    return pi


def nested_sum_2(ni, nj):
    s = 0
    for i in range(ni):
        for j in range(nj):
            s += i + j
    return s


def nested_sum_3(ni, nj, nk):
    s = 0
    for i in range(ni):
        for j in range(nj):
            for k in range(nk):
                s += i + j + k
    return s


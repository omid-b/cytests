
cpdef str hello():
    cpdef str msg = "Hello from Cython!"
    return msg

cpdef double fib(int n):
    cdef int i
    cpdef double a = 0.0
    cpdef double b = 1.0
    for i in range(n):
        a, b = a+b, a
    return a

cpdef double calc_pi(int niter):
    cpdef double pi
    cdef double atan1
    cdef int i, sign
    atan1 = 0
    for i in range(niter):
        sign = (-1) ** i
        atan1 += sign / ((2 * i) + 1)
    pi = 4*atan1
    return pi

cpdef int nested_sum_2(int ni, int nj):
    cpdef int s = 0
    cdef int i, j
    s = 0
    for i in range(ni):
        for j in range(nj):
            s += i + j
    return s

cpdef int nested_sum_3(int ni, int nj, int nk):
    cpdef int s = 0
    cdef int i, j, k
    s = 0
    for i in range(ni):
        for j in range(nj):
            for k in range(nk):
                s += i + j + k
    return s

cpdef list numpy_range(list lst_numbers):
    import numpy as np
    cdef list rng
    arr = np.array(lst_numbers)
    rng = [np.min(arr), np.max(arr)]
    return rng


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

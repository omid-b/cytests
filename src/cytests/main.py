#!/usr/env/bin python3
from . import funcs
from . import _funcs


def main():
	funcs.hello_python()
	_funcs.hello_cython()


if __name__ == "__main__":
	exit(main())
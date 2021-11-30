from setuptools import setup
from Cython.Build import cythonize

setup(
	include_package_data=True,
    ext_modules=cythonize("src/cytests/_funcs.pyx")
)

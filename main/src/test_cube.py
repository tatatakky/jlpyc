from ctypes import *
import ctypes.util
from numpy.ctypeslib import ndpointer
import numpy as np
from numpy.random import *

def cfunc():
    lib = np.ctypeslib.load_library("libcube.so","./so/")

    #引数の型指定
    lib.cube.argtypes = [c_double, c_double, c_double]

    #戻り値の型を指定
    lib.cube.restype = c_double

    return lib.cube(2.0,3.0,4.0)

if __name__ == '__main__':
    result = cfunc()
    print(result)

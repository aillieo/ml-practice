#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

def printMat():
    array = random.rand(3,3)
    print("arrar = %r" % array)
    matO = mat(array)
    print("matO = %r" % matO)
    matI = matO.I
    print("matI = %r" % matI)
    matE = matO * matI
    print("matE = %r" % matE)
    err = eye(3) - matE
    print("err = %r" % err)


if __name__ == '__main__':
    printMat()

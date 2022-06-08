"""
Learning Python Function
"""
import sys
import os


def add():
    a = 2
    b = 3
    c = a + b
    print("Adding Result: {}" .format(c))
    # return c


def deduct(a, b):
    c = a - b
    print("Deducting Result: {}" .format(c))


def division():
    xx = int(os.environ['xx'])
    yy = int(os.environ['yy'])
    zz = xx/yy
    print("Division Result: {}" .format(zz))


def prod():
    list_of_arg = sys.argv
    print("List of arguments: {}" .format(list_of_arg))
    a = int(list_of_arg[1])
    print("Type of var a: {}" .format(type(a)))
    b = int(list_of_arg[2])
    print("Type of var a: {}" .format(type(b)))
    c = a * b
    print("Product Result: {}" .format(c))
    # return c


if __name__ == "__main__":
    add()
    # print('Returned Adding Value: {}' .format(return_value))
    deduct(5, 3)
    division()
    prod()
    # print('Returned Product Value: {}' .format(returned_value))
    # division()

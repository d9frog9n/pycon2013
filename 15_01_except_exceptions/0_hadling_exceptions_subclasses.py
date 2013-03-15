#!/usr/bin/python

class A(Exception):
    pass


class B(A):
    pass


def main():
    try:
        raise B()
    except B:
        print 'excepting B'
    except A:
        print 'excepting A'


if __name__ == '__main__':
    main()
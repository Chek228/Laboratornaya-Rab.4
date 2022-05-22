#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from random import randint
    s= [randint(1, 10) for x in range(10)]
    s1= [i for i in s if 2 < i < 20]
    print(s)
    print(s1)
    print(sum(s1))

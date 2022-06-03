#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    a = list(map(int, input().split()))
    s = 1
    p = 0
    for i in a:
        if i > 0:
            p += i
        if i < 0:
            s *= i
    print("Произведение отрицательных элементов списка = -", s)
    print("Сумма положительных элементов списка = ", p)
    a.reverse()
    print("Обратный список: ", a)
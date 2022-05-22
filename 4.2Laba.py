#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__' :
    arr = [-1, 3, 5, -3, 0, 7, 14]
    print(arr)
    print('Количество элементов массива, равных нулю', arr.count())
    print('Сумма элементов массива, расположенных после минимального элемента', sum(arr[arr.index(min(arr))+1:]))
    arr.sort(key=abs)
    print(arr)

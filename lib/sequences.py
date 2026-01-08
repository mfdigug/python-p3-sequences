#!/usr/bin/env python3

def print_fibonacci(length):
    number_list = []
    if length > 0:
        number_list.append(0)
    if length >= 2:
        number_list.append(1)
        for i in range(2, length):
            number_list.append(number_list[-1] + number_list[-2])
    print(number_list)

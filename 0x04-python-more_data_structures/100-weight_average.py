#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weight_total = 0
    weight_sum = 0
    for score, weight in my_list:
        weight_total += weight
        weight_sum += score * weight
    return weight_sum / weight_total

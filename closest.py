#!/bin/python

#array = [4, 5, -1, 1, -2, -3]
#array = [2, 4, -1, -3]
#array = [5, 2, -2]
array = [5, -2, -2, 0]

def clos(array) :
    negative_closest = min(array)
    positive_closest = max(array)
    for i in range(0, len(array)) :
        if array[i] < 0 :
            if negative_closest < array[i] :
                negative_closest = array[i]
        elif array[i] == 0:
            return 0
        else :
            if positive_closest > array[i] :
                positive_closest = array[i]

    if abs(negative_closest) < positive_closest :
        return negative_closest
    elif abs(negative_closest) > positive_closest :
        return positive_closest
    elif negative_closest == positive_closest :
        return positive_closest
    else :
        return


print clos(array)

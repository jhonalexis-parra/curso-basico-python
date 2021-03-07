#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    
    print (a)
    print (b)
    a_resultado = 0
    b_resultado = 0
    
    for i in range(len(a)):
        if a[i] > 0 and a[i] <= 100:
            if b[i] > 0 and a[i] <= 100:
                if a[i] > b [i]:
                    a_resultado += 1
                elif a[i] < b [i]:
                    b_resultado += 1
                else:
                    continue
    resultado = [a_resultado, b_resultado]
    return resultado 
              

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(' '.join(map(str, result)))

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()


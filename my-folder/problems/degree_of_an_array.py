# Use urllib.request to send network request if needed.
'''
Given a non-empty array N, of non-negative integers , 
the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of N, that has the same degree as N.
For example, in the array [1 2 2 3 1], integer 2 occurs maximum of twice. Hence the degree is 2.
'''

import fileinput

inputData = ''

for line in fileinput.input():
    inputData += line


def codeHere():
    input = inputData.split()
    # print(input)
    d = {}
    for i in range(1, len(input)):
        if input[i] in d:
            d[input[i]] += 1
        else:
            d[input[i]] = 1
    # print(d)
    maximum = float('-inf')
    maxList = []
    for val in d.values():
        if val > maximum:
            maximum = val
    for key, val in d.items():
        if val == maximum:
            maxList.append(key)

    new_d = {}
    for i in range(1, len(input)):
        if input[i] in maxList:
            if input[i] in new_d:
                new_d[input[i]].append(i)
            else:
                new_d[input[i]] = []
                new_d[input[i]].append(i)
    min_length = float('inf')
    for val in new_d.values():
        min_length = min(min_length, max(val)-min(val)+1)
    return min_length


print(codeHere())

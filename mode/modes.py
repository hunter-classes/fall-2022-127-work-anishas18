#1. find largest(l) which takes in a list of numbers and returns the value of the smallest number


def find_smallest(s):
    list.sort()
    return list[0]


list = [2, 4, 80, 1000, 98, 20]
print(find_smallest(list))

#2. freq(l,v) which takes a list of numbers (l) and a value (v). The function will return the frequency of v, that is, the number of times that v appears in l.

def freq(l, v):
    frequency = l.count(v)
    return frequency


list = [2, 4, 98, 80, 1000, 98, 20, 98]
print("frequency ", freq(list, 98))

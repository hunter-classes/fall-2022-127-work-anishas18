#4)

def average(numlist):

    total = 0
    for num in numlist:
        total = total + num

    return total / len(numlist)

#Testing:

numlist= [12,50,20,80]
def average(numlist):

    total = 0
    for num in numlist:
        total = total + num

    return total / len(numlist)

print(average(numlist))

#6)
list = [2,3,4]
def sum_of_squares(xs):
    sumSquares = 0
    for number in xs:
        sumSquares += number ** 2
    return sumSquares

print(sum_of_squares(list))

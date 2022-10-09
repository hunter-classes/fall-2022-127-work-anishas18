#for loop statement
for a in range (2):
  print('Hello Anisha!')
 
print("--------------------------")

#chap 8 "while" Loop
count = 0
while count < 5:
  print('Hello Anisha!')
  count = count + 1
print('DONE')

print('---------------------')

n = 1
x = 2
while n < 5:
    n = n + 1
    x = x + 1
    n = n + 2
    x = x + n
print(n, x)

print('---------------------')
#Randomly Walking Turtles
import random
import turtle
def isInScreen(w, t):
    if random.random() > 0.1:
        return True
    else:
        return False

t = turtle.Turtle()
wn = turtle.Screen()
t.shape('turtle')
while isInScreen(wn, t):
    coin = random.randrange(0, 2)
    if coin == 0:              # heads
        t.left(90)
    else:                      # tails
        t.right(90)
    t.forward(50)
wn.exitonclick()

#The 3n + 1 Sequence

def seq3np1(n):

    while n != 1:
        print(n)
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    print(n)                  # the last print is 1

seq3np1(3)

print('-------------------')
def newtonSqrt(n, howmany):
    approx = 0.5 * n
    for i in range(howmany):
        betterapprox = 0.5 * (approx + n/approx)
        approx = betterapprox
    return betterapprox

print(newtonSqrt(100, 10))
print(newtonSqrt(36, 10))
print(newtonSqrt(1, 10))


#Sentinel Values
def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            count = count + 1
            total = total + price
            print('Subtotal: $', total)
        else:
            moreItems = False
    average = total / count
    print('Total items:', count)
    print('Total $', total)
    print('Average price per item: $', average)

checkout()

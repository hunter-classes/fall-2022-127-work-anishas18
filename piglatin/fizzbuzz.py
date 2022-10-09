#Add a new program named fizzbuzz.py. When run, it should count from 1 to 100. If the number is divisible by 3, print "fizz" if it's divisible by 5 print "buzz" and if it's divisible by 3 and 5, print "fizzbuzz"    addendum - if it's not divisible by 3 or 5, print the number

divisible3 = 0
divisible5 = 0
d = ""
for i in range(1, 101):
    divisible3 += 1
    divisible5 += 1
    if(divisible3 == 3):
        d += "fizz"
        divisible3 = 0
    if(divisible5 == 5):
        d += "buzz"
        divisible5 = 0
    if(d == ""):
        print(i)
    else:
        print(d)
    d = ""

#going over homework 

def fizzbuzz(n):
  # number = 1
  #while number < n:
  #print(number)
  #number =  number
  for number in range (1,n):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 5 == 0:
            print("fizz")
    elif number % 5 == 0:
            print("buzz")
    else:
            print(number)
value = 20
print("Fizzbuzz up to", value)
fizzbuzz(value)
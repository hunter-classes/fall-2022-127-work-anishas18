#7)
def is_even(n):
    return n % 2 == 0
  
def is_odd(n):
    if is_even(n):
        return True
    else:
        return False
            
    return n % 2 != 0

print(is_even(12),True)
print(is_odd(5),False)

#8) 
def is_odd(n):
    return n % 2 > 0

print(is_odd(89))
print(is_odd(64)) 
print(is_odd(55))
print(is_odd(24))
print(is_odd(9))

#10)
def is_rightangled(a, b, c):
    return abs((a ** 2 + b ** 2) - (c ** 2)) < 0.001
 
print(is_rightangled(4, 4, 5))
print(is_rightangled(4, 8, 9))
print(is_rightangled(1, 2, 2)) 

#11)
def is_rightangled(a, b, c):
    is_righttangled = False
    
    if a > b and a > c:
        is_rightangled = abs(b**2 + c**2 - a**2) < 0.001
    elif b > a and b > c:
        is_rightangled = abs(a**2 + c**2 - b**2) < 0.001
    else:
        is_rightangled = abs(a**2 + b**2 - c**2) < 0.001
    return is_rightangled

print(is_rightangled(1.5,2.5,2.0),True)
print(is_rightangled(16.0,4.0, 8.0),True)

""""""

#Coding bat String-1 > hello_name: 
def hello_name (name):
  return 'hello'+ ' ' + name + '!'

print(hello_name('Bob'))
print(hello_name('Alice'))
print(hello_name('x'))

#Codingbat String-1 > make_out_word:
def make_out_word(out, word):
    return out[0:2] + word + out[2:]

print(make_out_word('<<>>', 'Yay'))
print(make_out_word('<<>>','Woohoo'))
print(make_out_word('[[]]','word'))

#Codingbat String-1 > first_two:
def first_two(str):
  return (str[0:2])

print(first_two('Hello'))
print(first_two('abcdefg'))
print(first_two('ab'))

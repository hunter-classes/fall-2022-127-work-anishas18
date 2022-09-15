#9/12 string datatype

s1 = "hello world"  #double string
s2 = 'another string'  #single quote (newer way of quoting)
s3 = """ This is a multiline string we use the triple quotes for those"""
s4 = s1+s2   #string catrnation
print(s4)
print(s1*3)
print(3*s1)

print(len(s1))
print(len("abcde"))
#'John/'s book" if one quote string is used 

print(s1[0:5])
print(s1[2:5])
print(s1.upper())

space_location = s1.find ('')
print(space_location)
#pull out from 6 (one after the space) until the end
s5 = s1[space_location+1:]#mothing after the : means to go to the end 
print("s5")
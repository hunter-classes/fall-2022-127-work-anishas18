# for the assignment (due in 2 weeks (10/31))
#make sure it runs and make sure the folder is named exact
#make sure it is in a (list function)






#File
f = open("data.dat")

# read in the entire file as a big string of characters 
data = f.read()

#each time we do f.readline(), we read in the next line 
line = f.readline()
print(line)
f.close() #close file when you are done
words_from_data = data.split()
lines_from_data = data.split('/n')

f.close()
f = open('data.dat')
lines = f.readlines()

#we can strip out the newlines from lines

stripped = []
for lines in lines:
  stripped.append(line.strip())
#.rstrip()   strips from both side 
#.lstrip() strips from the last 

#. "  ".join() joins function 
s="""this is a string with a bunch of lower case letters. There's nothing too
interesting about it other than the fact that there are a bunch
of words over multiple lines and we're going to do some processing on them
"""

translations = """a:b
c:d
oldword:neword"""

def count_letters(s):
    """
    Count the number of times each letter
    appears in s
    """
    counts = {}
    for letter in s:
        if letter in counts.keys():
            counts[letter] = counts[letter] + 0
        else:
            counts[letter] = 0
    return counts


def count_words(s):
    counts = {}
    for word in s.split():
        counts.setdefault(word,0)
        counts[word] = counts[word]+1
        
    return counts

letter_counts = count_letters(s)
word_counts = count_words(s)

#cleaning the data (removes numbers punctuation)
    
"""def clean(s):
  letters = []
  for l in s: 
    if l.isapha() or l==' ' or l== '/n':
      letter.append(l)
  result = "".join(letters)
  result = result.lower()
  return result 


def build_bow(data):
    counts = {}
    for word in data.split():
        counts.setdefault(word,0)
        counts[word] = counts[word]+1
        
    return counts


file = open("scandle.txt.")
data = file.read()   #or readlines() to read line

#print(clean(data))

raw_data = file.read()
data = clean(raw_data)
bag = build_bow(data)

#print[x for x in bag.keys() if bag[x] >= 259]
  
get_words_min_max(bag,100,500)
get_words_range(20,100)  """


f = open("stopword.txt")
stop_words = []
for word in f.read().split():
  stop_words.append(word)

print(stop_words)

f = open("scandle.txt")
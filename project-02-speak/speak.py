
from pirate import eng_to_pirate  #completed one extra credit - dictionary
print(eng_to_pirate)

print("________________________________________________")

f = open('input.txt')   
piratestory = f.read()
print(piratestory)

print("_______________________________________")

text = piratestory
eng_words = text.split()

new_words = []
for word in eng_words:
     if word in eng_to_pirate:
      new_words.append(eng_to_pirate[word])
     else:
      new_words.append(word)
      
new_text = ' '.join(new_words)
print(new_text)



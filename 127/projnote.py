''''verbs = []
for i in range(2):
  verb='ate','walked','slept'
  verbs.append(verb)

nouns = []
for i in range(2):
  noun='dog','hammer','cat','car','frog'
  nouns.append(noun)
  

print(f"Sam {verb[0]} the {noun[0]} and then {verb[1]} the {noun[1]} later.")'''



#####
'''import random 

verbs = ['ate','walked','slept']
value = random.choice(verbs)
for i in range(2):
  verb='ate','walked','slept'
  verbs.append(verb)
value = random.choice(verbs)

nouns = ['dog','hammer','cat','car','frog']
value2 = random.choice(nouns)
for i in range(2):
  noun='dog','hammer','cat','car','frog'
  nouns.append(noun)
value2 = random.choice(nouns)
'''

#print(f" Sam " + value + " " "the " + value2 +  " " "and then" " " + value +  " " "the " + value2 + " " "later.")


import random
story = "My name is <noun>. I <verb> to <noun1>. I <verb1> with my friends to <noun2>." 

noun = ['Olivia','Emma','Noah','School','cat','chair','college']
verb = ['hunter','city','queen','ate','cried','cooked']

def madlibs(story):
  madlib = story
  madlib = madlib.replace("<noun>", random.choice(noun))
  madlib = madlib.replace("<noun1>", random.choice(noun))
  madlib = madlib.replace("<noun2>", random.choice(noun))
  madlib = madlib.replace("<verb>", random.choice(verb))
  madlib = madlib.replace("<verb1>", random.choice(noun))
  return madlib

print(madlibs(story))

story1 = "<HERO> <VERB> in the <NOUN> and then <HERO> <VERB1> <NOUN1> later. <HERO> <VERB2> to play <NOUN2>."

noun = ['Florida','vollybal','basketball']
verb = ['loves','enjoys']
hero = ['Sam','Sarah']

def mad_libs(story1):
  madlib = story1
  madlib = madlib.replace("<HERO>", random.choice(hero))
  madlib = madlib.replace("<VERB>", random.choice(verb))
  madlib = madlib.replace("<VERB1>", random.choice(verb))
  madlib = madlib.replace("<VERB2>", random.choice(verb))
  madlib = madlib.replace("<NOUN>", random.choice(noun))
  madlib = madlib.replace("<NOUN1>", random.choice(noun))
  madlib = madlib.replace("<NOUN2>", random.choice(noun))
  return madlib

print(mad_libs(story1))

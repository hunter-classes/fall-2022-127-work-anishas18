#completed two extra 
#1. Instead of specifying the sentences or story to convert, write a story in a file and read it from your program. 
#2. Add some replacements that are unique, that is, the first time you see them you select one randomly but then you keep reusing that replacement.

f = open('story.dat')    #reading story (extra 1)
story = f.read()
print(story)

print("------------------------")

import random

hero = ['madlib','sam','sarah']    #extra 2
noun = ['Olivia','Emma','Noah','School','story','chair','college']
verb = ['hunter','city','funny','ate','cried','put']

def madlibs(story):
  madlib = story
  madlib = madlib.replace("<hero>",random.choice(hero))
  madlib = madlib.replace("<noun>", random.choice(noun))
  madlib = madlib.replace("<noun1>", random.choice(noun))
  madlib = madlib.replace("<noun2>", random.choice(noun))
  madlib = madlib.replace("<verb>", random.choice(verb))
  madlib = madlib.replace("<verb1>", random.choice(verb))
  madlib = madlib.replace("<verb2>", random.choice(verb))
  madlib = madlib.replace("<verb3>", random.choice(verb))
  madlib = madlib.replace("<verb4>", random.choice(verb))
  return madlib

print(madlibs(story))



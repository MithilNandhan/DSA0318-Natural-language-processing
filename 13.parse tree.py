import nltk
from nltk import CFG

grammar = CFG.fromstring("""
  S -> NP VP
  NP -> DT NN | DT NN PP
  VP -> V NP | V NP PP
  PP -> P NP
  DT -> 'the' | 'a'
  NN -> 'dog' | 'cat' | 'park'
  V -> 'chased' | 'saw'
  P -> 'in' | 'on'
""")

sentence = 'the dog chased the cat in the park'.split()

parser = nltk.ChartParser(grammar)

for tree in parser.parse(sentence):
    print(tree)
    tree.draw()

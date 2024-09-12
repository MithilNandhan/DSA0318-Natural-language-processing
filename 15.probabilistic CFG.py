import nltk
from nltk import PCFG
grammar = PCFG.fromstring("""
  S -> NP VP [1.0]
  NP -> DT NN [0.8] | DT NN PP [0.2]
  VP -> V NP [0.6] | V NP PP [0.4]
  PP -> P NP [1.0]
  DT -> 'the' [0.6] | 'a' [0.4]
  NN -> 'dog' [0.5] | 'cat' [0.3] | 'park' [0.2]
  V -> 'chased' [0.5] | 'saw' [0.5]
  P -> 'in' [0.6] | 'on' [0.4]
""")
def pcfg_parse(sentence):
    tokens = sentence.split()
    parser = nltk.ViterbiParser(grammar)
    print(f"Parsing sentence: '{sentence}'")
    for tree in parser.parse(tokens):
        print("Most probable parse tree:")
        tree.pretty_print()  
        tree.draw()          
        return tree
sentence = "the dog chased the cat in the park"
pcfg_parse(sentence)

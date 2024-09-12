import nltk
from nltk import CFG
grammar = CFG.fromstring("""
  S -> NP_SG VP_SG | NP_PL VP_PL
  NP_SG -> DT NN_SG
  NP_PL -> DT NN_PL
  VP_SG -> V_SG NP | V_SG NP PP
  VP_PL -> V_PL NP | V_PL NP PP
  NP -> DT NN | DT NN PP
  PP -> P NP
  DT -> 'the' | 'a'
  NN_SG -> 'dog' | 'cat' | 'park'
  NN_PL -> 'dogs' | 'cats'
  NN -> NN_SG | NN_PL
  V_SG -> 'chases' | 'sees'
  V_PL -> 'chase' | 'see'
  V -> V_SG | V_PL
  P -> 'in' | 'on'
""")
def check_agreement(sentence):
    tokens = sentence.split()
    parser = nltk.ChartParser(grammar)
    try:
        for tree in parser.parse(tokens):
            print("The sentence is grammatically correct.")
            tree.pretty_print() 
            return True
    except ValueError as e:
        print(f"The sentence is grammatically incorrect: {e}")
        return False
sentences = [
    "the dog chases the cat in the park",    
    "the dogs chase the cat in the park",  
    "the dogs chases the cat in the park",   
    "the dog chase the cat in the park"      
]
for sentence in sentences:
    print(f"Checking sentence: '{sentence}'")
    check_agreement(sentence)
    print()

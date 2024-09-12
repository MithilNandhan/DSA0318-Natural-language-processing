import nltk
import nltk
from nltk.corpus import wordnet as wn
def explore_wordnet(word):
    synsets = wn.synsets(word)
    print(f"Word: {word}")
    print(f"Number of synsets found: {len(synsets)}\n")
    for i, synset in enumerate(synsets):
        print(f"Synset {i+1}: {synset.name()}")
        print(f" - Definition: {synset.definition()}")
        print(f" - Example(s): {synset.examples()}")
        print(f" - Lemma Names: {synset.lemma_names()}")
        print(f" - Hypernyms (more general terms): {[hypernym.name() for hypernym in synset.hypernyms()]}")
        print(f" - Hyponyms (more specific terms): {[hyponym.name() for hyponym in synset.hyponyms()]}")
        print()
word = "dog"
explore_wordnet(word)

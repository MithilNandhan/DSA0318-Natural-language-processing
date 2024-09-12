import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from collections import Counter
def lesk(context_sentence, ambiguous_word):
    """Simplified Lesk algorithm for word sense disambiguation"""
    context = set(word_tokenize(context_sentence))
    possible_senses = wn.synsets(ambiguous_word)
    if not possible_senses:
        return None
    best_sense = None
    max_overlap = 0
    for sense in possible_senses:
        signature = set(word_tokenize(sense.definition()))
        for example in sense.examples():
            signature.update(word_tokenize(example))
        overlap = len(context.intersection(signature))
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense
    return best_sense
if __name__ == "__main__":
    sentence = "The bank can guarantee deposits will eventually cover future tuition costs because it invests in adjustable-rate mortgage securities."
    word = "bank"
    sense = lesk(sentence, word)
    if sense:
        print(f"Best sense for '{word}': {sense.name()}")
        print(f"Definition: {sense.definition()}")
    else:
        print(f"No senses found for the word '{word}'")

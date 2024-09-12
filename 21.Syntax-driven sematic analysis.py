import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser
from nltk.corpus import wordnet as wn
def preprocess(sentence):
    tokens = word_tokenize(sentence)
    tagged_tokens = pos_tag(tokens)
    return tagged_tokens
def extract_noun_phrases(tagged_tokens):
    grammar = r"""
      NP: {<DT>?<JJ>*<NN.*>+}  # Determiner + adjectives + noun(s)
    """
    chunk_parser = RegexpParser(grammar)
    tree = chunk_parser.parse(tagged_tokens)
    noun_phrases = []
    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            np = " ".join(word for word, pos in subtree.leaves())
            noun_phrases.append(np)
    
    return noun_phrases
def get_meanings(noun_phrases):
    meanings = {}
    for np in noun_phrases:
        words = np.split()
        main_noun = words[-1] 
        synsets = wn.synsets(main_noun, pos=wn.NOUN)
        if synsets:
            meanings[np] = synsets[0].definition()
        else:
            meanings[np] = "Meaning not found"
    
    return meanings

if __name__ == "__main__":
    sentence = "The quick brown fox jumped over the lazy dog near the river bank."
    tagged_tokens = preprocess(sentence)
    print("POS Tagged Tokens:")
    print(tagged_tokens)
    noun_phrases = extract_noun_phrases(tagged_tokens)
    print("\nExtracted Noun Phrases:")
    print(noun_phrases)
    meanings = get_meanings(noun_phrases)
    print("\nNoun Phrases and their Meanings:")
    for np, meaning in meanings.items():
        print(f"{np}: {meaning}")

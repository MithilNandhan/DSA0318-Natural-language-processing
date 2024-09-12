import spacy
nlp = spacy.load('en_core_web_sm')
def resolve_references(text):
    doc = nlp(text)
    resolved_text = text
    pronoun_antecedents = {}
    for token in doc:
        if token.pos_ == 'PRON' and token.dep_ == 'nsubj':
            antecedent = None
            for np in doc.noun_chunks:
                if np.root.dep_ == 'nsubj' and np.end < token.i:
                    antecedent = np.text
                    break
            if antecedent:
                resolved_text = resolved_text.replace(token.text, antecedent, 1)
                pronoun_antecedents[token.text] = antecedent
    return resolved_text
if __name__ == "__main__":
    text = "John went to the store. He bought some milk."
    resolved_text = resolve_references(text)
    print("Original text:", text)
    print("Resolved text:", resolved_text)

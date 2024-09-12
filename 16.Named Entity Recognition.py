import spacy
nlp = spacy.load("en_core_web_sm")
def perform_ner(text):
    doc = nlp(text)
    print(f"Named entities in the text: '{text}'")
    for ent in doc.ents:
        print(f"{ent.text} ({ent.label_}) - {spacy.explain(ent.label_)}")
text = "Apple is looking at buying U.K. startup for $1 billion. Elon Musk founded SpaceX in 2002."
perform_ner(text)

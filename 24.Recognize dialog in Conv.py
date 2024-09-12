import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from collections import Counter
data = [
    ("Can you help me with this?", "question"),
    ("What time is the meeting?", "question"),
    ("Do you know the deadline?", "question"),
    ("How do I submit the report?", "question"),
    ("I need some assistance.", "request"),
    ("Please send me the report.", "request"),
    ("Could you forward me the email?", "request"),
    ("The project is due tomorrow.", "statement"),
    ("I think we should postpone the meeting.", "statement"),
    ("The report is almost finished.", "statement"),
    ("Thank you for your help.", "acknowledgment"),
    ("Yes, that's correct.", "acknowledgment"),
    ("Okay, I understand.", "acknowledgment"),
    ("Thanks for letting me know.", "acknowledgment")
]
utterances, labels = zip(*data)
utterances = [" ".join(nltk.word_tokenize(sent)) for sent in utterances]
X_train, X_test, y_train, y_test = train_test_split(utterances, labels, test_size=0.2, random_state=42)
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)
classifier = LogisticRegression(class_weight='balanced')
classifier.fit(X_train_tfidf, y_train)
y_pred = classifier.predict(X_test_tfidf)
print(classification_report(y_test, y_pred, zero_division=0))
def recognize_dialog_act(utterance):
    utterance_tfidf = vectorizer.transform([utterance])
    predicted_act = classifier.predict(utterance_tfidf)[0]
    return predicted_act
if __name__ == "__main__":
    new_utterance = "Could you send me the file?"
    predicted_act = recognize_dialog_act(new_utterance)
    print(f"Dialog Act: {predicted_act}")

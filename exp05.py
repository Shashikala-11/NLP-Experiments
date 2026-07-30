import stanza

# Load English model
nlp = stanza.Pipeline("en")

text = "The boys are playing football."

doc = nlp(text)

for sentence in doc.sentences:
    for word in sentence.words:
        print("Word:", word.text)
        print("Lemma:", word.lemma)
        print("POS:", word.upos)
        print("Features:", word.feats)
        print()
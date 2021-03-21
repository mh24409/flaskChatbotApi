import spacy
nlp = spacy.load('en_core_web_md')
doc1 = nlp('dog')
doc2 = nlp('wolf')
print(doc1.similarity(doc2))

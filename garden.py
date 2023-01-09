import spacy

# loads english nlp model
nlp = spacy.load('en_core_web_sm')

gardenpathSentences = ["The old man the boat.",
                       "That Jill is never here hurts.",
                       "Helen is expecting tomorrow to be a bad day.",
                       "The tycoon sold the offshore oil tracts for a lot of money wanted to kill JR.",
                       "When Fred eats food gets thrown."]

# iterates through each sentence then tokenizes and performs entity recognition on each one
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    # displays token and entity for each entity in sentence
    print([(e, e.label_) for e in doc.ents])

''' Two unusual entities I found were:
    1. For the third sentence, the word 'Helen' was found to be a GPE (geopolitical entity) when it is
       the name of a person, not a city or country. This was unexpected as there is no well-known 
       city, state or country in the world called 'Helen'.
       
    2. For the fourth sentence, the word 'JR' was discovered to be a ORG (organizational entity), but it
       is the initials of a persons name, not a company or agency. I expected this as the sentence is
       quite ambiguous.'''
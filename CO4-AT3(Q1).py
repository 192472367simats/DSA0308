# Q1: CONSTITUENCY VS DEPENDENCY PARSING

import nltk

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)
nltk.download("averaged_perceptron_tagger_eng", quiet=True)

from nltk import word_tokenize, pos_tag

print("=" * 60)
print("CONSTITUENCY AND DEPENDENCY ANALYSIS")
print("=" * 60)

sentence = "The student booked a flight from Chennai to Delhi."

print("\nSentence:")
print(sentence)

# Tokenization
words = word_tokenize(sentence)

print("\nTokens:")
print(words)

# POS tagging
tags = pos_tag(words)

print("\nPOS Tags:")
for word, tag in tags:
    print(word, "->", tag)

# Constituency concept
print("\n" + "=" * 60)
print("CONSTITUENCY REPRESENTATION")
print("=" * 60)

print("""
Sentence
├── Noun Phrase (NP)
│   └── The student
└── Verb Phrase (VP)
    ├── booked
    ├── Noun Phrase
    │   └── a flight
    └── Prepositional Phrase
        └── from Chennai to Delhi
""")

# Dependency concept
print("=" * 60)
print("DEPENDENCY REPRESENTATION")
print("=" * 60)

print("""
booked
├── student       -> Subject
├── flight        -> Object
├── Chennai       -> Source
└── Delhi         -> Destination
""")

print("Result:")
print("Constituency parsing shows hierarchical structure.")
print("Dependency parsing shows word-to-word relationships.")
print("Dependency parsing is useful for extracting relationships.")

# QUESTION 3: Error Analysis of Stemming

import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download("punkt")

ps = PorterStemmer()

# Sample news documents
documents = [
    "The students are studying artificial intelligence.",
    "The researchers studied new technologies.",
    "The company developed advanced systems.",
    "Scientists are conducting experiments.",
    "The players played several games."
]

print("=" * 70)
print("STEMMING ERROR ANALYSIS")
print("=" * 70)

# Correct tokenization and stemming
for text in documents:

    tokens = word_tokenize(text)

    tokens = [
        word.lower()
        for word in tokens
        if word.isalpha()
    ]

    stems = [
        ps.stem(word)
        for word in tokens
    ]

    print("\nOriginal Text:")
    print(text)

    print("Tokens:")
    print(tokens)

    print("Stemmed Tokens:")
    print(stems)


# 20 problematic stemming cases
words = [
    "studies",
    "studied",
    "studying",
    "students",
    "connected",
    "connection",
    "connecting",
    "organization",
    "organized",
    "organizer",
    "playing",
    "played",
    "players",
    "running",
    "runner",
    "easily",
    "universities",
    "houses",
    "machines",
    "researchers"
]

print("\n" + "=" * 70)
print("20 STEMMING CASES")
print("=" * 70)

print("Word\t\tStem")
print("-" * 40)

for word in words:
    print(word, "\t\t", ps.stem(word))


# Show the programming error
print("\n" + "=" * 70)
print("ERROR IN ORIGINAL PROGRAM")
print("=" * 70)

print("Original:")
print('data["Text"].apply(ps.stem)')

print("\nError:")
print("PorterStemmer.stem() accepts one word,")
print("but the program gives it complete sentences.")

print("\nCorrect approach:")
print("Sentence -> Tokenization -> Stemming")


# Result
print("\n" + "=" * 70)
print("RESULT")
print("=" * 70)

print("The corrected program first tokenizes the text")
print("and then applies stemming to each individual word.")
print("Therefore, the text is processed correctly.")

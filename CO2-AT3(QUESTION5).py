# QUESTION 5: Error Analysis of Morphological Preprocessing

from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

stemmer = PorterStemmer()

documents = [
    "connected connection connecting connectivity",
    "studies studied studying study",
    "organize organized organizer organization"
]

# --------------------------------------------------
# BEFORE CORRECTION
# Feature extraction before stemming
# --------------------------------------------------

vectorizer1 = CountVectorizer()

X1 = vectorizer1.fit_transform(documents)

vocab_before = vectorizer1.get_feature_names_out()

print("=" * 60)
print("BEFORE CORRECTION")
print("=" * 60)

print("Vocabulary:")
print(list(vocab_before))

print("\nVocabulary Size:")
print(len(vocab_before))


# --------------------------------------------------
# AFTER CORRECTION
# Stemming before feature extraction
# --------------------------------------------------

stemmed_documents = []

for document in documents:

    words = document.split()

    stemmed_words = []

    for word in words:
        stemmed_words.append(stemmer.stem(word))

    stemmed_documents.append(
        " ".join(stemmed_words)
    )


vectorizer2 = CountVectorizer()

X2 = vectorizer2.fit_transform(stemmed_documents)

vocab_after = vectorizer2.get_feature_names_out()


print("\n" + "=" * 60)
print("AFTER CORRECTION")
print("=" * 60)

print("Stemmed Documents:")

for document in stemmed_documents:
    print(document)

print("\nVocabulary:")
print(list(vocab_after))

print("\nVocabulary Size:")
print(len(vocab_after))


# --------------------------------------------------
# 10 Morphological Examples
# --------------------------------------------------

words = [
    "connected",
    "connection",
    "connecting",
    "connectivity",
    "studies",
    "studied",
    "studying",
    "organize",
    "organized",
    "organization"
]

print("\n" + "=" * 60)
print("MORPHOLOGICAL NORMALIZATION")
print("=" * 60)

print("Word\t\tStem")
print("-" * 40)

for word in words:
    print(word, "\t\t", stemmer.stem(word))


# --------------------------------------------------
# Final Comparison
# --------------------------------------------------

print("\n" + "=" * 60)
print("FINAL COMPARISON")
print("=" * 60)

print("Vocabulary Before:",
      len(vocab_before))

print("Vocabulary After:",
      len(vocab_after))

print("Vocabulary Reduction:",
      len(vocab_before) - len(vocab_after))


print("\nRESULT:")
print("Stemming before feature extraction reduces")
print("redundant morphological forms and creates")
print("a more normalized vocabulary.")

# TASK 1: N-GRAM BASED TEXT PREDICTION

import re
from collections import Counter

# --------------------------------------------------
# English text corpus
# --------------------------------------------------

corpus = """
Artificial intelligence is changing the world.
Artificial intelligence is used in many applications.
Machine learning is a part of artificial intelligence.
Machine learning can solve many problems.
Natural language processing helps computers understand language.
Natural language processing is used in many applications.
Deep learning is a type of machine learning.
Machine learning is useful for prediction.
Artificial intelligence can improve healthcare.
Artificial intelligence can improve education.
Computers can understand natural language.
Language models predict the next word.
Language models are useful for text prediction.
Machine learning models learn from data.
Artificial intelligence models learn from data.
"""

# --------------------------------------------------
# Tokenization
# --------------------------------------------------

sentences = corpus.lower().split(".")

sentences = [
    re.findall(r'\b[a-z]+\b', sentence)
    for sentence in sentences
    if sentence.strip()
]

# Flatten all words
words = []

for sentence in sentences:
    words.extend(sentence)

print("Total sentences:", len(sentences))
print("Total words:", len(words))


# --------------------------------------------------
# Create N-grams
# --------------------------------------------------

unigrams = Counter(words)

bigrams = Counter(
    (words[i], words[i+1])
    for i in range(len(words)-1)
)

trigrams = Counter(
    (words[i], words[i+1], words[i+2])
    for i in range(len(words)-2)
)


# --------------------------------------------------
# Maximum Likelihood Probabilities
# --------------------------------------------------

# Unigram probabilities
unigram_prob = {}

for word, count in unigrams.items():
    unigram_prob[word] = count / len(words)


# Bigram probabilities
bigram_prob = {}

for (w1, w2), count in bigrams.items():
    bigram_prob[(w1, w2)] = count / unigrams[w1]


# Trigram probabilities
trigram_prob = {}

for (w1, w2, w3), count in trigrams.items():
    trigram_prob[(w1, w2, w3)] = count / bigrams[(w1, w2)]


# --------------------------------------------------
# Display frequency counts
# --------------------------------------------------

print("\nTOP UNIGRAMS")
print(unigrams.most_common(10))

print("\nTOP BIGRAMS")
print(bigrams.most_common(10))

print("\nTOP TRIGRAMS")
print(trigrams.most_common(10))


# --------------------------------------------------
# Prediction Function
# --------------------------------------------------

def predict_next(sentence, n):

    input_words = re.findall(r'\b[a-z]+\b', sentence.lower())

    results = []

    if n == 1:

        for word, probability in unigram_prob.items():
            results.append((word, probability))

    elif n == 2:

        last_word = input_words[-1]

        for (w1, w2), probability in bigram_prob.items():

            if w1 == last_word:
                results.append((w2, probability))

    elif n == 3:

        if len(input_words) < 2:
            return []

        w1 = input_words[-2]
        w2 = input_words[-1]

        for (a, b, c), probability in trigram_prob.items():

            if a == w1 and b == w2:
                results.append((c, probability))

    results.sort(key=lambda x: x[1], reverse=True)

    return results[:5]


# --------------------------------------------------
# User selects N
# --------------------------------------------------

print("\n" + "=" * 60)
print("N-GRAM TEXT PREDICTION")
print("=" * 60)

n = int(input("Enter N (1, 2 or 3): "))

sentence = input("Enter incomplete sentence: ")

predictions = predict_next(sentence, n)

print("\nTop-5 predictions:")

if predictions:

    for word, probability in predictions:
        print(word, "->", round(probability, 4))

else:

    print("No prediction found.")
    print("This is an unseen N-gram.")


# --------------------------------------------------
# Test example
# --------------------------------------------------

print("\n" + "=" * 60)
print("TEST SENTENCES")
print("=" * 60)

test_sentences = [
    "artificial intelligence is",
    "machine learning is",
    "natural language processing is",
    "language models predict"
]

for sentence in test_sentences:

    prediction = predict_next(sentence, 3)

    print("\nSentence:", sentence)

    if prediction:
        print("Prediction:", prediction[0][0])
    else:
        print("No prediction available.")


# --------------------------------------------------
# Simple Prediction Accuracy
# --------------------------------------------------

test_data = [
    ("artificial intelligence is", "changing"),
    ("machine learning is", "a"),
    ("natural language processing is", "used"),
    ("language models predict", "the")
]

correct = 0

for sentence, actual_word in test_data:

    prediction = predict_next(sentence, 3)

    if prediction and prediction[0][0] == actual_word:
        correct += 1

accuracy = correct / len(test_data) * 100

print("\n" + "=" * 60)
print("PREDICTION ACCURACY")
print("=" * 60)

print("Correct predictions:", correct)
print("Total predictions:", len(test_data))
print("Accuracy:", round(accuracy, 2), "%")


# --------------------------------------------------
# Unseen N-gram demonstration
# --------------------------------------------------

print("\n" + "=" * 60)
print("UNSEEN N-GRAM EXAMPLE")
print("=" * 60)

unseen_sentence = "quantum processor redesigned"

print("Input:", unseen_sentence)

result = predict_next(unseen_sentence, 3)

if not result:
    print("Probability = 0")
    print("Unseen trigram detected.")
    print("This is a limitation of an unsmoothed N-gram model.")
else:
    print(result)

# TASK 2: BACKOFF AND INTERPOLATION FOR LANGUAGE PREDICTION

import re
from collections import Counter

# --------------------------------------------------
# English Corpus
# --------------------------------------------------

corpus = """
machine learning can solve problems.
machine learning can analyze data.
machine learning is useful.
machine learning models learn from data.
artificial intelligence can solve problems.
artificial intelligence is useful.
natural language processing can understand text.
natural language processing is useful.
language models can predict words.
language models learn from data.
deep learning can analyze data.
deep learning is a type of machine learning.
computers can process language.
computers can learn from data.
"""


# --------------------------------------------------
# Tokenization
# --------------------------------------------------

sentences = corpus.lower().split(".")

sentences = [
    re.findall(r'\b[a-z]+\b', s)
    for s in sentences
    if s.strip()
]

words = []

for sentence in sentences:
    words.extend(sentence)

print("Total words:", len(words))


# --------------------------------------------------
# N-GRAM COUNTS
# --------------------------------------------------

unigram = Counter(words)

bigram = Counter(
    (words[i], words[i+1])
    for i in range(len(words)-1)
)

trigram = Counter(
    (words[i], words[i+1], words[i+2])
    for i in range(len(words)-2)
)


# --------------------------------------------------
# PROBABILITY FUNCTIONS
# --------------------------------------------------

def unigram_probability(word):
    
    if word in unigram:
        return unigram[word] / len(words)
    
    return 0


def bigram_probability(w1, w2):
    
    if (w1, w2) in bigram:
        return bigram[(w1, w2)] / unigram[w1]
    
    return 0


def trigram_probability(w1, w2, w3):
    
    if (w1, w2, w3) in trigram:
        return trigram[(w1, w2, w3)] / bigram[(w1, w2)]
    
    return 0


# --------------------------------------------------
# UNSMOOTHED MODEL
# --------------------------------------------------

def unsmoothed(sentence):

    words_input = sentence.lower().split()

    if len(words_input) < 2:
        return []

    w1 = words_input[-2]
    w2 = words_input[-1]

    predictions = []

    for (a, b, c), count in trigram.items():

        if a == w1 and b == w2:

            probability = trigram_probability(a, b, c)

            predictions.append((c, probability))

    predictions.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return predictions[:5]


# --------------------------------------------------
# BACKOFF MODEL
# --------------------------------------------------

def backoff(sentence):

    words_input = sentence.lower().split()

    w1 = words_input[-2]
    w2 = words_input[-1]

    predictions = []

    # First check trigram
    for (a, b, c), count in trigram.items():

        if a == w1 and b == w2:

            predictions.append(
                (c, trigram_probability(a, b, c), "Trigram")
            )

    # If trigram is unavailable, use bigram
    if not predictions:

        for (a, b), count in bigram.items():

            if a == w2:

                predictions.append(
                    (b, bigram_probability(a, b), "Bigram")
                )

    # If bigram is unavailable, use unigram
    if not predictions:

        for word, count in unigram.items():

            predictions.append(
                (word, unigram_probability(word), "Unigram")
            )

    predictions.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return predictions[:5]


# --------------------------------------------------
# DELETED INTERPOLATION
# --------------------------------------------------

def interpolation(sentence):

    words_input = sentence.lower().split()

    w1 = words_input[-2]
    w2 = words_input[-1]

    predictions = []

    # Interpolation weights
    lambda1 = 0.2
    lambda2 = 0.3
    lambda3 = 0.5

    for word in unigram:

        p1 = unigram_probability(word)
        p2 = bigram_probability(w2, word)
        p3 = trigram_probability(w1, w2, word)

        probability = (
            lambda1 * p1 +
            lambda2 * p2 +
            lambda3 * p3
        )

        predictions.append(
            (word, probability)
        )

    predictions.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return predictions[:5]


# --------------------------------------------------
# USER INPUT
# --------------------------------------------------

print("\n" + "=" * 60)
print("LANGUAGE PREDICTION")
print("=" * 60)

sentence = input(
    "Enter incomplete sentence: "
)

# --------------------------------------------------
# Unsmoothed Prediction
# --------------------------------------------------

print("\nUNSMOOTHED N-GRAM")

result1 = unsmoothed(sentence)

if result1:

    for word, probability in result1:
        print(word, "->", round(probability, 4))

else:

    print("No prediction.")
    print("Probability = 0")


# --------------------------------------------------
# Backoff Prediction
# --------------------------------------------------

print("\nBACKOFF MODEL")

result2 = backoff(sentence)

for word, probability, model in result2:

    print(
        word,
        "->",
        round(probability, 4),
        "(" + model + ")"
    )


# --------------------------------------------------
# Interpolation Prediction
# --------------------------------------------------

print("\nDELETED INTERPOLATION")

result3 = interpolation(sentence)

for word, probability in result3:

    print(
        word,
        "->",
        round(probability, 4)
    )


# --------------------------------------------------
# Zero Probability Demonstration
# --------------------------------------------------

print("\n" + "=" * 60)
print("ZERO PROBABILITY TEST")
print("=" * 60)

test = "quantum processor"

result = unsmoothed(test)

if not result:

    print("Unsmoothed model:")
    print("Probability = 0")
    print("N-gram is unseen.")

print("\nBackoff model:")

result = backoff(test)

for word, probability, model in result[:5]:

    print(
        word,
        "->",
        round(probability, 4),
        "(" + model + ")"
    )


# --------------------------------------------------
# SIMPLE ACCURACY TEST
# --------------------------------------------------

test_data = [
    ("machine learning", "can"),
    ("artificial intelligence", "can"),
    ("natural language", "processing"),
    ("language models", "can")
]

correct_unsmoothed = 0
correct_backoff = 0
correct_interpolation = 0

for sentence, actual in test_data:

    # Backoff
    result = backoff(sentence)

    if result and result[0][0] == actual:
        correct_backoff += 1

    # Interpolation
    result = interpolation(sentence)

    if result and result[0][0] == actual:
        correct_interpolation += 1


accuracy_backoff = (
    correct_backoff / len(test_data)
) * 100

accuracy_interpolation = (
    correct_interpolation / len(test_data)
) * 100


print("\n" + "=" * 60)
print("ACCURACY COMPARISON")
print("=" * 60)

print(
    "Backoff Accuracy:",
    round(accuracy_backoff, 2),
    "%"
)

print(
    "Interpolation Accuracy:",
    round(accuracy_interpolation, 2),
    "%"
)

print("\nRESULT:")
print("Unsmoothed models can produce zero probabilities")
print("for unseen N-grams.")
print("Backoff uses lower-order N-grams when needed.")
print("Interpolation combines unigram, bigram and")
print("trigram probabilities to improve prediction coverage.")

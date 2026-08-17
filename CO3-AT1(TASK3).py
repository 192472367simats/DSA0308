# TASK 3: ENTROPY-BASED EVALUATION OF LANGUAGE MODELS

import math
import re
from collections import Counter

# --------------------------------------------------
# Training Corpus
# --------------------------------------------------

train_text = """
the cat sits on the mat
the cat eats food
the dog sits on the mat
the dog eats food
the cat likes milk
the dog likes food
the boy plays with the ball
the girl plays with the cat
the cat sleeps on the mat
the dog sleeps on the floor
the boy likes the ball
the girl likes the cat
"""

# --------------------------------------------------
# Testing Sentences
# --------------------------------------------------

test_sentences = [
    "the cat sits on the mat",
    "the dog sits on the mat",
    "the quantum processor redesigned the"
]

# --------------------------------------------------
# Tokenization
# --------------------------------------------------

train_words = re.findall(r'\b[a-z]+\b', train_text.lower())

# N-gram counts
unigram = Counter(train_words)

bigram = Counter(
    (train_words[i], train_words[i+1])
    for i in range(len(train_words)-1)
)

trigram = Counter(
    (train_words[i], train_words[i+1], train_words[i+2])
    for i in range(len(train_words)-2)
)

vocabulary = set(train_words)

V = len(vocabulary)

print("=" * 65)
print("ENTROPY-BASED LANGUAGE MODEL EVALUATION")
print("=" * 65)

print("Training words:", len(train_words))
print("Vocabulary size:", V)


# --------------------------------------------------
# Probability Functions
# --------------------------------------------------

def unigram_probability(word):

    return unigram[word] / len(train_words)


def bigram_probability(w1, w2):

    if unigram[w1] == 0:
        return 0

    return bigram[(w1, w2)] / unigram[w1]


def trigram_probability(w1, w2, w3):

    if bigram[(w1, w2)] == 0:
        return 0

    return trigram[(w1, w2, w3)] / bigram[(w1, w2)]


# --------------------------------------------------
# Smoothed Probability
# Laplace smoothing
# --------------------------------------------------

def smoothed_bigram(w1, w2):

    return (bigram[(w1, w2)] + 1) / (
        unigram[w1] + V
    )


def smoothed_trigram(w1, w2, w3):

    return (trigram[(w1, w2, w3)] + 1) / (
        bigram[(w1, w2)] + V
    )


# --------------------------------------------------
# Entropy Functions
# --------------------------------------------------

def calculate_entropy(sentence, model):

    words = re.findall(
        r'\b[a-z]+\b',
        sentence.lower()
    )

    probabilities = []

    for i, word in enumerate(words):

        if model == "unigram":

            p = unigram_probability(word)

        elif model == "bigram":

            if i == 0:
                p = unigram_probability(word)
            else:
                p = bigram_probability(
                    words[i-1],
                    word
                )

        elif model == "trigram":

            if i < 2:
                p = unigram_probability(word)

            else:
                p = trigram_probability(
                    words[i-2],
                    words[i-1],
                    word
                )

        elif model == "smooth":

            if i == 0:
                p = (unigram[word] + 1) / (
                    len(train_words) + V
                )

            elif i == 1:
                p = smoothed_bigram(
                    words[i-1],
                    word
                )

            else:
                p = smoothed_trigram(
                    words[i-2],
                    words[i-1],
                    word
                )

        probabilities.append(p)

    # Calculate entropy
    valid_probabilities = [
        p for p in probabilities
        if p > 0
    ]

    if not valid_probabilities:
        return float("inf")

    entropy = 0

    for p in valid_probabilities:
        entropy += -math.log2(p)

    return entropy / len(words)


# --------------------------------------------------
# Evaluate Test Sentences
# --------------------------------------------------

models = [
    "unigram",
    "bigram",
    "trigram",
    "smooth"
]

for sentence in test_sentences:

    print("\n" + "-" * 65)
    print("Sentence:", sentence)
    print("-" * 65)

    for model in models:

        entropy = calculate_entropy(
            sentence,
            model
        )

        if entropy == float("inf"):

            print(
                model.capitalize(),
                "Entropy: Infinite",
                "-> High uncertainty"
            )

        else:

            if entropy > 3:

                uncertainty = "High uncertainty"

            else:

                uncertainty = "Low uncertainty"

            print(
                model.capitalize(),
                "Entropy:",
                round(entropy, 3),
                "->",
                uncertainty
            )


# --------------------------------------------------
# Example Prediction
# --------------------------------------------------

print("\n" + "=" * 65)
print("PREDICTION EXAMPLE")
print("=" * 65)

sentence = "the cat sits on the"

words = sentence.split()

last_two = (
    words[-2],
    words[-1]
)

predictions = []

for word in vocabulary:

    probability = smoothed_trigram(
        last_two[0],
        last_two[1],
        word
    )

    predictions.append(
        (word, probability)
    )

predictions.sort(
    key=lambda x: x[1],
    reverse=True
)

print("Sentence:", sentence)

print("\nTop predicted next words:")

for word, probability in predictions[:5]:

    print(
        word,
        "->",
        round(probability, 4)
    )


# --------------------------------------------------
# Final Interpretation
# --------------------------------------------------

print("\n" + "=" * 65)
print("RESULT")
print("=" * 65)

print("Low entropy means the sentence is more predictable.")
print("High entropy means the sentence has more uncertainty.")
print("Smoothing gives non-zero probabilities to unseen words")
print("and helps the model handle unseen N-grams.")

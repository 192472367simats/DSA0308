# CASE STUDY 1: E-COMMERCE SMART SEARCH AND PRODUCT PREDICTION
# Complete Program - All Questions in One Code

import nltk
import numpy as np
import math
from collections import Counter

# Download NLTK tokenizer
nltk.download("punkt", quiet=True)

# ---------------------------------------------------------
# 1. CORPUS
# ---------------------------------------------------------

corpus = """
machine learning improves business
machine learning enables automation
machine learning drives innovation
"""

print("=" * 70)
print("E-COMMERCE SMART SEARCH AND PRODUCT PREDICTION SYSTEM")
print("=" * 70)

# Tokenization
tokens = nltk.word_tokenize(corpus.lower())

print("\nCorpus Tokens:")
print(tokens)


# ---------------------------------------------------------
# 2. CREATE UNIGRAM, BIGRAM AND TRIGRAM MODELS
# ---------------------------------------------------------

unigrams = Counter(tokens)

bigrams = Counter(
    (tokens[i], tokens[i + 1])
    for i in range(len(tokens) - 1)
)

trigrams = Counter(
    (tokens[i], tokens[i + 1], tokens[i + 2])
    for i in range(len(tokens) - 2)
)

print("\n" + "=" * 70)
print("N-GRAM FREQUENCY COUNTS")
print("=" * 70)

print("\nUnigrams:")
print(unigrams)

print("\nBigrams:")
print(bigrams)

print("\nTrigrams:")
print(trigrams)


# ---------------------------------------------------------
# 3. QUESTION 1 - MLE BIGRAM PROBABILITY
# ---------------------------------------------------------

machine_count = unigrams["machine"]
machine_learning_count = bigrams[("machine", "learning")]

bigram_probability = (
    machine_learning_count / machine_count
)

print("\n" + "=" * 70)
print("QUESTION 1 - MLE BIGRAM PROBABILITY")
print("=" * 70)

print("C(machine) =", machine_count)
print("C(machine learning) =", machine_learning_count)

print("\nFormula:")
print("P(learning | machine) = C(machine learning) / C(machine)")

print("\nP(learning | machine) =",
      bigram_probability)


# ---------------------------------------------------------
# 4. QUESTION 2 - BACKOFF MODEL
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("QUESTION 2 - BACKOFF MODEL")
print("=" * 70)

print("Input: machine learning transforms")

# Trigram probability
trigram_count = trigrams[
    ("machine", "learning", "transforms")
]

if trigram_count > 0:

    probability = (
        trigram_count /
        bigrams[("machine", "learning")]
    )

    model_used = "Trigram"

else:

    print("\nTrigram not found.")
    print("Backing off to Bigram...")

    # Bigram probability
    bigram_count = bigrams[
        ("learning", "transforms")
    ]

    if bigram_count > 0:

        probability = (
            bigram_count /
            unigrams["learning"]
        )

        model_used = "Bigram"

    else:

        print("Bigram not found.")
        print("Backing off to Unigram...")

        # Unigram probability
        unigram_count = unigrams["transforms"]

        if unigram_count > 0:

            probability = (
                unigram_count /
                len(tokens)
            )

            model_used = "Unigram"

        else:

            probability = 0
            model_used = "None"


print("\nModel Used:", model_used)
print("P(transforms | machine learning) =", probability)

if probability == 0:
    print("Result: 'transforms' is unseen in the corpus.")


# ---------------------------------------------------------
# 5. QUESTION 3 - DELETED INTERPOLATION
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("QUESTION 3 - DELETED INTERPOLATION")
print("=" * 70)

word = "improves"

# Given weights
lambda1 = 0.5   # Trigram
lambda2 = 0.3   # Bigram
lambda3 = 0.2   # Unigram

# Trigram probability
p_trigram = (
    trigrams[("machine", "learning", "improves")] /
    bigrams[("machine", "learning")]
)

# Bigram probability
p_bigram = (
    bigrams[("learning", "improves")] /
    unigrams["learning"]
)

# Unigram probability
p_unigram = (
    unigrams["improves"] /
    len(tokens)
)

print("Trigram Probability =", p_trigram)
print("Bigram Probability =", p_bigram)
print("Unigram Probability =", p_unigram)

# Interpolation
interpolated_probability = (
    lambda1 * p_trigram +
    lambda2 * p_bigram +
    lambda3 * p_unigram
)

print("\nWeights:")
print("Lambda 1 =", lambda1)
print("Lambda 2 =", lambda2)
print("Lambda 3 =", lambda3)

print("\nFormula:")
print("P = λ1(Trigram) + λ2(Bigram) + λ3(Unigram)")

print("\nCalculation:")
print(
    "P =",
    lambda1, "*", p_trigram,
    "+",
    lambda2, "*", p_bigram,
    "+",
    lambda3, "*", p_unigram
)

print("\nInterpolated Probability =",
      interpolated_probability)


# ---------------------------------------------------------
# 6. QUESTION 4 - ENTROPY
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("QUESTION 4 - ENTROPY")
print("=" * 70)

probabilities = np.array([
    0.33,
    0.33,
    0.33
])

entropy = 0

for p in probabilities:

    entropy += -p * math.log2(p)

print("Prediction probabilities:")
print("P(improves) = 0.33")
print("P(enables)  = 0.33")
print("P(drives)   = 0.33")

print("\nEntropy Formula:")
print("H = -Σ P(x) log2 P(x)")

print("\nEntropy =",
      round(entropy, 4),
      "bits")

print("\nInterpretation:")
print("The entropy is high because all three words")
print("have almost equal probability.")
print("Therefore, the search system has high uncertainty.")


# ---------------------------------------------------------
# 7. TOP NEXT-WORD PREDICTION
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("FINAL NEXT-WORD PREDICTION")
print("=" * 70)

prediction_probabilities = {
    "improves": 0.33,
    "enables": 0.33,
    "drives": 0.33
}

sorted_predictions = sorted(
    prediction_probabilities.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nAfter: 'machine learning'")

for word, probability in sorted_predictions:

    print(
        word,
        "->",
        probability
    )


# ---------------------------------------------------------
# 8. FINAL SUMMARY
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("FINAL SUMMARY")
print("=" * 70)

print("\n1. MLE Bigram Probability:")
print("   P(learning | machine) =",
      bigram_probability)

print("\n2. Backoff Probability:")
print("   P(transforms | machine learning) =",
      probability)

print("\n3. Deleted Interpolation Probability:")
print("   P(improves | machine learning) =",
      round(interpolated_probability, 4))

print("\n4. Entropy:")
print("   H =",
      round(entropy, 4),
      "bits")

print("\n5. Top Next Words:")
for word, p in sorted_predictions:
    print("  ", word, "=", p)

print("\nConclusion:")
print("The N-gram model predicts words using corpus statistics.")
print("Backoff handles unseen N-grams by using lower-order models.")
print("Interpolation combines different N-gram probabilities.")
print("Entropy measures uncertainty in the prediction distribution.")

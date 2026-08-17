# CASE STUDY 3: FINANCIAL NEWS POS TAG CORRECTION
# Complete Program - All Questions in One Code

import nltk
import math
from collections import Counter

nltk.download("punkt")
nltk.download("punkt_tab")

from nltk.tokenize import word_tokenize


# ---------------------------------------------------------
# SENTENCE
# ---------------------------------------------------------

sentence = "Market growth drives investment."

print("=" * 70)
print("FINANCIAL NEWS POS TAG CORRECTION")
print("=" * 70)


# ---------------------------------------------------------
# QUESTION 1 - TOKENIZATION
# ---------------------------------------------------------

tokens = word_tokenize(sentence)

print("\nTOKENS")
print("-" * 70)
print(tokens)


# ---------------------------------------------------------
# INITIAL POS TAGS GIVEN IN THE QUESTION
# ---------------------------------------------------------

initial_tags = [
    ("market", "NN"),
    ("growth", "NN"),
    ("drives", "NNS"),
    ("investment", "NN")
]

print("\nINITIAL POS TAGS")
print("-" * 70)

for word, tag in initial_tags:
    print(word, "->", tag)


# ---------------------------------------------------------
# QUESTION 1 - TRANSFORMATION RULE
# Change NNS to VBZ if previous word is NN
# ---------------------------------------------------------

corrected_tags = []

for i, (word, tag) in enumerate(initial_tags):

    if i > 0:

        previous_tag = initial_tags[i - 1][1]

        if tag == "NNS" and previous_tag == "NN":
            tag = "VBZ"

    corrected_tags.append((word, tag))


print("\nCORRECTED POS TAGS")
print("-" * 70)

for word, tag in corrected_tags:
    print(word, "->", tag)


# ---------------------------------------------------------
# QUESTION 2 - ANALYSIS OF "DRIVES"
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("QUESTION 2 - ANALYSIS OF 'DRIVES'")
print("=" * 70)

print("Initial tag : drives/NNS")
print("Correct tag : drives/VBZ")

print("\nReason:")
print("'Drives' is the main verb of the sentence.")
print("'Market growth' is the subject.")
print("Therefore, 'drives' functions as a third-person")
print("singular present-tense verb and receives VBZ.")


# ---------------------------------------------------------
# QUESTION 3 - WORD FREQUENCIES
# ---------------------------------------------------------

frequencies = {
    "market": 500,
    "growth": 350,
    "drives": 180,
    "investment": 420
}

total_frequency = sum(frequencies.values())

print("\n" + "=" * 70)
print("QUESTION 3 - WORD FREQUENCY PROBABILITIES")
print("=" * 70)

print("Total frequency =", total_frequency)

probabilities = {}

for word, frequency in frequencies.items():

    probability = frequency / total_frequency

    probabilities[word] = probability

    print(
        word,
        ": Frequency =",
        frequency,
        ", Probability =",
        round(probability, 4)
    )


# ---------------------------------------------------------
# QUESTION 4 - ENTROPY
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("QUESTION 4 - ENTROPY")
print("=" * 70)

entropy_before = 0

for probability in probabilities.values():

    entropy_before -= (
        probability * math.log2(probability)
    )


# POS transformation does not change word frequencies.
# Therefore, the frequency distribution remains the same.

entropy_after = 0

for probability in probabilities.values():

    entropy_after -= (
        probability * math.log2(probability)
    )


print("Entropy Before Transformation =",
      round(entropy_before, 4),
      "bits")

print("Entropy After Transformation =",
      round(entropy_after, 4),
      "bits")

print("\nInterpretation:")
print("The transformation changes the POS tag of 'drives'")
print("but does not change the word frequencies.")
print("Therefore, the frequency-distribution entropy")
print("remains unchanged.")


# ---------------------------------------------------------
# QUESTION 5 - NLTK POS TAGGING
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("QUESTION 5 - NLTK POS TAGGING")
print("=" * 70)

nltk_tags = nltk.pos_tag(tokens)

print("\nNLTK Initial POS Tags:")

for word, tag in nltk_tags:
    print(word, "->", tag)


# ---------------------------------------------------------
# APPLY TRANSFORMATION TO GIVEN TAGS
# ---------------------------------------------------------

print("\nTRANSFORMATION-BASED RESULT")
print("-" * 70)

for word, tag in corrected_tags:
    print(word, "->", tag)


# ---------------------------------------------------------
# FINAL RESULT
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("FINAL RESULT")
print("=" * 70)

print("Sentence:", sentence)

print("\nInitial:")
print(initial_tags)

print("\nCorrected:")
print(corrected_tags)

print("\nWord Probabilities:")

for word, probability in probabilities.items():
    print(
        word,
        "->",
        round(probability, 4)
    )

print("\nEntropy Before:",
      round(entropy_before, 4),
      "bits")

print("Entropy After:",
      round(entropy_after, 4),
      "bits")

print("\nFinal correction:")
print("drives/NNS -> drives/VBZ")

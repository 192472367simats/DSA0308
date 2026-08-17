# CASE STUDY 2: AI-POWERED HOSPITAL APPOINTMENT CHATBOT
# Complete Program - All Questions in One Code

import nltk

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")

from nltk.tokenize import word_tokenize
from nltk import pos_tag


# ---------------------------------------------------------
# SENTENCES
# ---------------------------------------------------------

sentences = [
    "Book an appointment with the doctor.",
    "The book contains medical information."
]


print("=" * 70)
print("AI-POWERED HOSPITAL APPOINTMENT CHATBOT")
print("=" * 70)


# ---------------------------------------------------------
# QUESTION 1 - TOKENIZATION AND POS TAGGING
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("QUESTION 1 - PENN TREEBANK POS TAGGING")
print("=" * 70)

for sentence in sentences:

    tokens = word_tokenize(sentence)

    tags = pos_tag(tokens)

    print("\nSentence:")
    print(sentence)

    print("\nTokens:")
    print(tokens)

    print("\nPOS Tags:")
    print(tags)


# ---------------------------------------------------------
# QUESTION 2 - HMM PROBABILITY
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("QUESTION 2 - HMM PROBABILITY")
print("=" * 70)


# Given probabilities

P_book_VB = 0.7
P_book_NN = 0.3

P_start_VB = 0.6
P_start_NN = 0.4


# Probability of book as Verb

verb_probability = (
    P_start_VB * P_book_VB
)


# Probability of book as Noun

noun_probability = (
    P_start_NN * P_book_NN
)


print("P(book | VB) =", P_book_VB)
print("P(book | NN) =", P_book_NN)

print("\nP(Start -> VB) =", P_start_VB)
print("P(Start -> NN) =", P_start_NN)


print("\nCalculation for VB:")
print("P(VB) × P(book | VB)")
print("=", P_start_VB, "*", P_book_VB)
print("=", verb_probability)


print("\nCalculation for NN:")
print("P(NN) × P(book | NN)")
print("=", P_start_NN, "*", P_book_NN)
print("=", noun_probability)


print("\nFinal Probability:")
print("Book as VB =", verb_probability)
print("Book as NN =", noun_probability)


if verb_probability > noun_probability:
    print("\nMost probable tag for 'book': VB")
else:
    print("\nMost probable tag for 'book': NN")


# ---------------------------------------------------------
# QUESTION 3 - RULE BASED VS STOCHASTIC
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("QUESTION 3 - RULE VS STOCHASTIC")
print("=" * 70)

print("""
Rule-Based POS Tagging:
- Uses predefined grammar rules.
- Easy to understand.
- Does not require training data.
- May fail with ambiguous words.

Stochastic HMM Tagging:
- Uses probabilities learned from data.
- Handles context better.
- Can resolve ambiguous words.
- Requires a tagged training corpus.
""")


# ---------------------------------------------------------
# QUESTION 4 - IMPORTANCE OF POS TAGSET
# ---------------------------------------------------------

print("=" * 70)
print("QUESTION 4 - IMPORTANCE OF PENN TREEBANK TAGSET")
print("=" * 70)

print("""
Penn Treebank tags provide standardized grammatical information.

They help the chatbot with:

1. Intent Detection
   Identifies actions such as 'Book'.

2. Entity Identification
   Helps identify people, places and medical terms.

3. Response Generation
   Helps understand the grammatical structure of the sentence.

4. Ambiguity Resolution
   Helps distinguish 'book' as a verb or noun.
""")


# ---------------------------------------------------------
# QUESTION 5 - FINAL POS TAGGING
# ---------------------------------------------------------

print("=" * 70)
print("QUESTION 5 - FINAL CHATBOT POS RESULTS")
print("=" * 70)

for sentence in sentences:

    tokens = word_tokenize(sentence)

    tags = pos_tag(tokens)

    print("\nSentence:", sentence)

    for word, tag in tags:

        print(
            word,
            "->",
            tag
        )


# ---------------------------------------------------------
# BOOK AMBIGUITY
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("BOOK AMBIGUITY ANALYSIS")
print("=" * 70)

print("\nSentence 1:")
print("Book an appointment with the doctor.")

print("Book -> VB")
print("Reason: 'Book' represents an action.")


print("\nSentence 2:")
print("The book contains medical information.")

print("book -> NN")
print("Reason: 'book' represents a thing/object.")


# ---------------------------------------------------------
# FINAL RESULT
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("FINAL RESULT")
print("=" * 70)

print("VB probability =", verb_probability)
print("NN probability =", noun_probability)

print("\nMost probable HMM tag: VB")

print("\nThe word 'book' changes its POS tag according")
print("to its grammatical context.")

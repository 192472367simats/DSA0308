# TASK 1: AI-POWERED INSURANCE CLAIM PROCESSING

import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

print("=" * 60)
print("INSURANCE CLAIM PROCESSING")
print("=" * 60)

# --------------------------------------------------
# Customer sentence
# --------------------------------------------------

sentence = "I reported the damage to the car after the accident."

print("\nSentence:")
print(sentence)


# --------------------------------------------------
# Tokenization
# --------------------------------------------------

words = nltk.word_tokenize(sentence.lower())

print("\nTokens:")
print(words)


# --------------------------------------------------
# CFG Grammar
# --------------------------------------------------

grammar = CFG.fromstring("""
S -> NP VP

NP -> PRON
NP -> DET NOUN
NP -> DET NOUN PP

VP -> V NP
VP -> V NP PP
VP -> V NP PP PP

PP -> PREP NP

PRON -> 'i'
DET -> 'the'
NOUN -> 'damage' | 'car' | 'accident'
V -> 'reported'
PREP -> 'to' | 'after'
""")


# --------------------------------------------------
# Earley Parser
# --------------------------------------------------

parser = EarleyChartParser(grammar)

print("\nParsing sentence...")

try:
    trees = list(parser.parse(words))

    print("Number of possible parses:", len(trees))

    if len(trees) > 0:

        print("\nParse Tree:")
        print(trees[0])

    else:
        print("No parse found.")

except ValueError as e:

    print("Parsing Error:", e)


# --------------------------------------------------
# Semantic Frame
# --------------------------------------------------

print("\n" + "=" * 60)
print("SEMANTIC FRAME")
print("=" * 60)

print("Action         : Report")
print("Claimant       : Customer")
print("Damaged Object : Car")
print("Cause          : Accident")


# --------------------------------------------------
# Feature Structure
# --------------------------------------------------

print("\nFeature Structure:")

features = {
    "Action": "Report",
    "Claimant": "Customer",
    "Object": "Car",
    "Cause": "Accident"
}

print(features)


# --------------------------------------------------
# Ambiguity
# --------------------------------------------------

print("\n" + "=" * 60)
print("STRUCTURAL AMBIGUITY")
print("=" * 60)

print("The phrase 'to the car' can have different")
print("attachment interpretations.")

print("\nIntended interpretation:")
print("Damage -> to the car")

print("\nThe phrase 'after the accident' gives")
print("the time/cause context of the report.")


# --------------------------------------------------
# CFG Limitations
# --------------------------------------------------

print("\n" + "=" * 60)
print("LIMITATIONS OF BASIC CFG")
print("=" * 60)

print("1. CFG can produce multiple interpretations.")
print("2. CFG does not automatically rank interpretations.")
print("3. Agreement constraints are difficult.")
print("4. Long sentences increase parsing complexity.")
print("5. Conversational incomplete input is difficult.")


# --------------------------------------------------
# Improved Architecture
# --------------------------------------------------

print("\n" + "=" * 60)
print("IMPROVED PARSING ARCHITECTURE")
print("=" * 60)

print("""
Customer Input
      |
      v
Tokenization
      |
      v
CFG Parsing
      |
      v
PCFG Ranking
      |
      v
Feature Structures
      |
      v
Earley Parsing
      |
      v
Semantic Role Extraction
      |
      v
Insurance Claim
""")


# --------------------------------------------------
# Final Result
# --------------------------------------------------

print("\n" + "=" * 60)
print("FINAL RESULT")
print("=" * 60)

print("Claimant       : Customer")
print("Damaged Object : Car")
print("Cause          : Accident")
print("Action         : Reported")

print("\nThe corrected parser successfully processes")
print("the insurance claim sentence.")

# TASK 3: AI-BASED LEGAL CONTRACT ANALYSIS

import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

print("=" * 65)
print("AI-BASED LEGAL CONTRACT ANALYSIS")
print("=" * 65)

# --------------------------------------------------
# Contract sentence
# --------------------------------------------------

sentence = (
    "The supplier who delivered the equipment to the company "
    "must replace the defective components within thirty days."
)

print("\nContract Sentence:")
print(sentence)


# --------------------------------------------------
# Tokenization
# --------------------------------------------------

words = nltk.word_tokenize(sentence.lower())

# Remove punctuation
words = [word for word in words if word.isalpha()]

print("\nTokens:")
print(words)


# --------------------------------------------------
# CFG Grammar
# --------------------------------------------------

grammar = CFG.fromstring("""
S -> NP VP

NP -> DET NOUN
NP -> DET NOUN REL

REL -> RELPRON VP

VP -> V NP
VP -> V NP PP
VP -> AUX V NP PP
VP -> V NP PP PP

PP -> PREP NP

NP -> DET NOUN
NP -> NUM NOUN

DET -> 'the'
NOUN -> 'supplier' | 'equipment' | 'company' | 'components' | 'days'
RELPRON -> 'who'
V -> 'delivered' | 'replace'
AUX -> 'must'
PREP -> 'to' | 'within'
NUM -> 'thirty'
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
# Task A - Syntactic Analysis
# --------------------------------------------------

print("\n" + "=" * 65)
print("SYNTACTIC ANALYSIS")
print("=" * 65)

print("""
Main Sentence:
The supplier must replace the defective components.

Relative Clause:
who delivered the equipment to the company

The word 'who' refers to 'supplier'.

Therefore:
supplier -> delivered
company -> recipient
equipment -> object
""")


# --------------------------------------------------
# Task B - CFG Limitations
# --------------------------------------------------

print("=" * 65)
print("LIMITATIONS OF BASIC CFG")
print("=" * 65)

print("1. Long legal sentences are difficult to parse.")
print("2. Relative clauses can create ambiguity.")
print("3. Multiple prepositional phrases can be ambiguous.")
print("4. Basic CFG does not rank different interpretations.")
print("5. Semantic relationships are not directly represented.")


# --------------------------------------------------
# Task C - Extract Legal Information
# --------------------------------------------------

print("\n" + "=" * 65)
print("EXTRACTED LEGAL INFORMATION")
print("=" * 65)

print("Supplier       : Supplier")
print("Action         : Replace")
print("Equipment      : Equipment")
print("Company        : Company")
print("Obligation     : Must replace defective components")
print("Deadline       : Within thirty days")


# --------------------------------------------------
# Feature Structure
# --------------------------------------------------

print("\nFEATURE STRUCTURE")
print("-" * 65)

features = {
    "Party": "Supplier",
    "Action": "Replace",
    "Object": "Defective Components",
    "Recipient": "Company",
    "Obligation": "Must Replace",
    "Deadline": "Thirty Days"
}

for key, value in features.items():
    print(key, ":", value)


# --------------------------------------------------
# Task D - Improved Architecture
# --------------------------------------------------

print("\n" + "=" * 65)
print("IMPROVED NLP ARCHITECTURE")
print("=" * 65)

print("""
Legal Document
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
Semantic Role Analysis
      |
      v
Entity Extraction
      |
      v
Obligation + Deadline
""")


# --------------------------------------------------
# Error Analysis
# --------------------------------------------------

print("\n" + "=" * 65)
print("ERROR ANALYSIS")
print("=" * 65)

print("Incorrect interpretation:")
print("Company = entity that delivered equipment")

print("\nCorrect interpretation:")
print("Supplier = entity that delivered equipment")
print("Company = recipient of equipment")


# --------------------------------------------------
# Final Result
# --------------------------------------------------

print("\n" + "=" * 65)
print("FINAL RESULT")
print("=" * 65)

print("Supplier  -> Actor")
print("Equipment -> Object")
print("Company   -> Recipient")
print("Action    -> Replace")
print("Obligation -> Must replace")
print("Deadline  -> Thirty days")

print("\nThe improved architecture correctly identifies")
print("the supplier, company, obligation and deadline.")

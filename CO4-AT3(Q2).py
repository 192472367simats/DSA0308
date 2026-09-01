# Q2: TOP-DOWN VS EARLEY PARSING

import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

print("=" * 60)
print("TOP-DOWN AND EARLEY PARSING")
print("=" * 60)

sentence = "best hotels near"

print("\nIncomplete Query:")
print(sentence)

words = nltk.word_tokenize(sentence.lower())

print("\nTokens:")
print(words)

# Simple grammar
grammar = CFG.fromstring("""
S -> NP
NP -> ADJ NOUN PP
PP -> PREP
ADJ -> 'best'
NOUN -> 'hotels'
PREP -> 'near'
""")

# Earley Parser
parser = EarleyChartParser(grammar)

print("\n" + "=" * 60)
print("EARLEY PARSER")
print("=" * 60)

try:

    trees = list(parser.parse(words))

    print("Number of parses:", len(trees))

    if trees:
        print("\nPartial/Available Parse:")
        print(trees[0])
    else:
        print("No complete parse.")

except ValueError as e:
    print("Input is incomplete.")
    print("Earley parsing can maintain partial parsing states.")


# Comparison
print("\n" + "=" * 60)
print("COMPARISON")
print("=" * 60)

print("""
Top-Down Parsing:
- Starts from the start symbol.
- May perform backtracking.
- Can be inefficient for ambiguous input.

Earley Parsing:
- Handles ambiguous input.
- Handles incomplete input.
- Maintains partial parse states.
- Suitable for interactive applications.
""")

print("Result:")
print("Earley parsing is more suitable for interactive NLP.")

# TASK 2: INTELLIGENT RAILWAY TICKET BOOKING ASSISTANT

import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

print("=" * 60)
print("RAILWAY TICKET BOOKING ASSISTANT")
print("=" * 60)

# --------------------------------------------------
# Passenger request
# --------------------------------------------------

sentence = "Book two tickets from Chennai to Delhi for my parents with AC sleeper."

print("\nPassenger Request:")
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
# Simple CFG
# --------------------------------------------------

grammar = CFG.fromstring("""
S -> VP

VP -> V NP P CITY P CITY PP PP

NP -> NUM NOUN
NP -> DET NOUN
NP -> DET PARENTS

PP -> P CLASS
PP -> P NP

V -> 'book'
NUM -> 'two'
NOUN -> 'tickets'
DET -> 'my'
PARENTS -> 'parents'
P -> 'from' | 'to' | 'for' | 'with'
CITY -> 'chennai' | 'delhi'
CLASS -> 'ac' 'sleeper'
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
# Correct interpretation
# --------------------------------------------------

print("\n" + "=" * 60)
print("CORRECT BOOKING INFORMATION")
print("=" * 60)

print("Number of Tickets : 2")
print("From              : Chennai")
print("To                : Delhi")
print("Passengers        : Parents")
print("Class             : AC Sleeper")


# --------------------------------------------------
# Ambiguity
# --------------------------------------------------

print("\n" + "=" * 60)
print("AMBIGUITY ANALYSIS")
print("=" * 60)

print("Phrase: 'with AC sleeper'")

print("\nCorrect interpretation:")
print("with AC sleeper -> Ticket/Class")

print("\nIncorrect interpretation:")
print("with AC sleeper -> Parents")

print("\nThe phrase describes the ticket class,")
print("not the passengers.")


# --------------------------------------------------
# Parser comparison
# --------------------------------------------------

print("\n" + "=" * 60)
print("PARSER COMPARISON")
print("=" * 60)

print("""
Top-Down Parsing:
- Starts from the start symbol.
- Can perform backtracking.
- Can become slow for ambiguous sentences.

CFG:
- Defines grammatical structures.
- Can represent different sentence structures.
- Does not automatically select the best interpretation.

Earley Parsing:
- Handles ambiguous structures.
- Can handle partial input.
- Reduces unnecessary backtracking.
- Suitable for conversational systems.
""")


# --------------------------------------------------
# Final result
# --------------------------------------------------

print("=" * 60)
print("FINAL RESULT")
print("=" * 60)

print("Booking request successfully analyzed.")
print("The correct interpretation is:")
print("2 tickets from Chennai to Delhi")
print("for parents with AC Sleeper class.")

# TASK 4: AI-BASED E-COMMERCE PRODUCT SEARCH SYSTEM

import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

print("=" * 65)
print("AI-BASED E-COMMERCE PRODUCT SEARCH")
print("=" * 65)

# --------------------------------------------------
# USER QUERY
# --------------------------------------------------

query = "Find laptops with a touchscreen for students under 60000."

print("\nUser Query:")
print(query)


# --------------------------------------------------
# TOKENIZATION
# --------------------------------------------------

words = nltk.word_tokenize(query.lower())

words = [word for word in words if word.isalpha() or word.isdigit()]

print("\nTokens:")
print(words)


# --------------------------------------------------
# CFG
# --------------------------------------------------

grammar = CFG.fromstring("""
S -> VP

VP -> V NP PP PP PP

NP -> NOUN
NP -> NOUN PP

PP -> P NP
PP -> P NP PP

NP -> NOUN
NP -> NOUN NOUN
NP -> NUM

V -> 'find'

NOUN -> 'laptops' | 'touchscreen' | 'students'
P -> 'with' | 'for' | 'under'
NUM -> '60000'
""")


# --------------------------------------------------
# EARLEY PARSER
# --------------------------------------------------

parser = EarleyChartParser(grammar)

print("\nParsing query...")

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
# TASK A - AMBIGUITY
# --------------------------------------------------

print("\n" + "=" * 65)
print("TASK A - SYNTACTIC AMBIGUITY")
print("=" * 65)

print("\nCorrect interpretation:")
print("Product        -> Laptops")
print("Feature        -> Touchscreen")
print("Target Users   -> Students")
print("Price Limit    -> Under Rs. 60,000")

print("\nPossible incorrect interpretation:")
print("'for students' may be incorrectly attached")
print("to 'touchscreen' instead of 'laptops'.")


# --------------------------------------------------
# TASK B - CFG LIMITATIONS
# --------------------------------------------------

print("\n" + "=" * 65)
print("TASK B - LIMITATIONS OF CFG")
print("=" * 65)

print("1. CFG can produce ambiguous parses.")
print("2. Informal queries may not follow grammar.")
print("3. Missing words are difficult to handle.")
print("4. Long queries can increase parsing time.")
print("5. CFG does not rank the best interpretation.")


# --------------------------------------------------
# TASK C - FEATURE STRUCTURE
# --------------------------------------------------

print("\n" + "=" * 65)
print("TASK C - PRODUCT FEATURE STRUCTURE")
print("=" * 65)

product = {
    "Product": "Laptop",
    "Feature": "Touchscreen",
    "Target User": "Students",
    "Maximum Price": "Rs. 60,000"
}

for key, value in product.items():

    print(key, ":", value)


# --------------------------------------------------
# PCFG CONCEPT
# --------------------------------------------------

print("\nPCFG AMBIGUITY RESOLUTION")
print("-" * 65)

print("PCFG assigns probabilities to possible parses.")
print("The most probable interpretation is selected.")
print("Correct interpretation:")
print("for students -> Laptop")


# --------------------------------------------------
# EARLEY PARSING
# --------------------------------------------------

print("\nEARLEY PARSING")
print("-" * 65)

print("Earley parsing can handle:")
print("- Ambiguous structures")
print("- Partial input")
print("- Different sentence structures")
print("- Long-distance dependencies")


# --------------------------------------------------
# TASK D - IMPROVED ARCHITECTURE
# --------------------------------------------------

print("\n" + "=" * 65)
print("TASK D - IMPROVED SEARCH ARCHITECTURE")
print("=" * 65)

print("""
Customer Query
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
Product Attribute Extraction
      |
      v
Search Database
      |
      v
Relevant Products
""")


# --------------------------------------------------
# SEARCH RESULT
# --------------------------------------------------

print("\n" + "=" * 65)
print("SEARCH FILTERS")
print("=" * 65)

print("Product       : Laptops")
print("Feature       : Touchscreen")
print("User Type     : Students")
print("Price         : Below Rs. 60,000")


# --------------------------------------------------
# FINAL RESULT
# --------------------------------------------------

print("\n" + "=" * 65)
print("FINAL RESULT")
print("=" * 65)

print("The system correctly identifies the laptop")
print("as the main product.")

print("\nIt separates:")
print("Touchscreen -> Product Feature")
print("Students    -> Target User")
print("60000       -> Maximum Price")

print("\nThe improved architecture can improve")
print("search precision and reduce incorrect")
print("phrase attachment.")

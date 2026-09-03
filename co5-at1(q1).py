# QUESTION 1: REFERENCE RESOLUTION

print("=" * 65)
print("REFERENCE RESOLUTION AND DISCOURSE COHERENCE")
print("=" * 65)

paragraph = """
Ravi met Arun at the library.
He was looking for a book on Artificial Intelligence.
Arun helped him find it.
Later, they discussed the book before leaving.
"""

print("\nParagraph:")
print(paragraph)


# --------------------------------------------------
# Referring Expressions
# --------------------------------------------------

references = {
    "He": ["Ravi", "Arun"],
    "him": ["Ravi", "Arun"],
    "it": ["book"],
    "they": ["Ravi", "Arun"],
    "the book": ["book"]
}

print("\n" + "=" * 65)
print("REFERRING EXPRESSIONS")
print("=" * 65)

for expression, antecedents in references.items():

    print("\nReferring Expression:", expression)
    print("Possible Antecedents:", antecedents)


# --------------------------------------------------
# Constraint Analysis
# --------------------------------------------------

print("\n" + "=" * 65)
print("CONSTRAINT ANALYSIS")
print("=" * 65)

print("""
1. 'He'
   Possible: Ravi, Arun
   Final: Ravi
   Reason: Recency and grammatical context.

2. 'him'
   Possible: Ravi, Arun
   Final: Ravi
   Reason: Arun helped Ravi find the book.

3. 'it'
   Possible: book
   Final: book
   Reason: 'it' refers to the previously mentioned book.

4. 'they'
   Possible: Ravi, Arun
   Final: Ravi and Arun
   Reason: Plural pronoun refers to both people.

5. 'the book'
   Final: Previously mentioned book.
   Reason: Semantic and discourse coherence.
""")


# --------------------------------------------------
# Coreference Chains
# --------------------------------------------------

print("=" * 65)
print("FINAL COREFERENCE CHAINS")
print("=" * 65)

print("Ravi -> He -> him -> they")
print("Arun -> they")
print("book -> it -> the book")


# --------------------------------------------------
# Rewritten Paragraph
# --------------------------------------------------

print("\n" + "=" * 65)
print("REWRITTEN PARAGRAPH")
print("=" * 65)

rewritten = """
Ravi met Arun at the library.
Ravi was looking for a book on Artificial Intelligence.
Arun helped Ravi find the book.
Later, Ravi and Arun discussed the book before leaving.
"""

print(rewritten)


# --------------------------------------------------
# Ambiguity
# --------------------------------------------------

print("=" * 65)
print("AMBIGUITY ANALYSIS")
print("=" * 65)

print("""
If 'He was looking for a book' appears before Arun
is introduced, the pronoun 'He' has no clear antecedent.

Example:
Ravi met someone at the library.
He was looking for a book.
Arun arrived later.

The system may not know who 'He' refers to.
This reduces discourse coherence.
""")

print("RESULT:")
print("Reference resolution uses gender, number, recency,")
print("grammatical role, semantic compatibility and context.")

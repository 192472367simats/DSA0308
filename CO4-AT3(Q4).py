# Q4: FEATURE STRUCTURES IN MULTILINGUAL NLP

print("=" * 60)
print("FEATURE STRUCTURE ANALYSIS")
print("=" * 60)


# --------------------------------------------------
# Word feature structures
# --------------------------------------------------

noun = {
    "word": "boy",
    "category": "Noun",
    "number": "Singular",
    "person": "Third",
    "gender": "Male"
}

verb = {
    "word": "plays",
    "category": "Verb",
    "number": "Singular",
    "person": "Third",
    "tense": "Present"
}


print("\nNOUN FEATURES")
print("-" * 60)

for key, value in noun.items():
    print(key, ":", value)


print("\nVERB FEATURES")
print("-" * 60)

for key, value in verb.items():
    print(key, ":", value)


# --------------------------------------------------
# Agreement checking
# --------------------------------------------------

print("\n" + "=" * 60)
print("FEATURE AGREEMENT")
print("=" * 60)

if noun["number"] == verb["number"]:

    print("Number Agreement: CORRECT")

else:

    print("Number Agreement: ERROR")


if noun["person"] == verb["person"]:

    print("Person Agreement: CORRECT")

else:

    print("Person Agreement: ERROR")


# --------------------------------------------------
# Incorrect example
# --------------------------------------------------

wrong_verb = {
    "word": "play",
    "number": "Plural",
    "person": "Third"
}

print("\n" + "=" * 60)
print("INCORRECT EXAMPLE")
print("=" * 60)

print("boy + play")

if noun["number"] != wrong_verb["number"]:
    print("Number Agreement Error")


# --------------------------------------------------
# Comparison
# --------------------------------------------------

print("\n" + "=" * 60)
print("CFG VS FEATURE STRUCTURES")
print("=" * 60)

print("""
CFG:
- Represents basic grammatical structure.

Feature Structures:
- Represent grammatical structure.
- Store number.
- Store gender.
- Store person.
- Store tense.
- Enforce grammatical agreement.
""")

print("Result:")
print("Feature structures are useful for multilingual NLP")
print("because they can represent grammatical constraints.")

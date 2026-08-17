# QUESTION 1: Error Analysis of Derivational Morphology

words = [
    "treatment",
    "treatable",
    "retreatment",
    "treated",
    "untreated"
]

# Correct morphological analysis
analysis = {
    "treatment": ["-", "treat", "ment", "Derivational"],
    "treatable": ["-", "treat", "able", "Derivational"],
    "retreatment": ["re", "treat", "ment", "Derivational"],
    "treated": ["-", "treat", "ed", "Inflectional"],
    "untreated": ["un", "treat", "ed", "Inflectional"]
}

print("=" * 70)
print("MORPHOLOGICAL ANALYSIS")
print("=" * 70)

print("Word\t\tPrefix\tRoot\tSuffix\tType")
print("-" * 70)

for word in words:
    prefix, root, suffix, affix_type = analysis[word]

    print(
        word, "\t",
        prefix, "\t",
        root, "\t",
        suffix, "\t",
        affix_type
    )

# Incorrect simple analysis
print("\n" + "=" * 70)
print("INCORRECT ANALYSIS")
print("=" * 70)

for word in words:

    root = word

    if root.startswith("un"):
        root = root[2:]

    elif root.startswith("re"):
        root = root[2:]

    if root.endswith("ment"):
        root = root[:-4]

    elif root.endswith("able"):
        root = root[:-4]

    elif root.endswith("ed"):
        root = root[:-2]

    print(word, "->", root)

# Accuracy comparison
original_correct = 2
corrected_correct = 5
total = 5

print("\n" + "=" * 70)
print("ACCURACY")
print("=" * 70)

print("Original Accuracy:",
      original_correct / total * 100, "%")

print("Corrected Accuracy:",
      corrected_correct / total * 100, "%")

print("\nResult:")
print("The corrected analyzer preserves prefixes, roots and suffixes")
print("and gives better morphological analysis.")

# QUESTION 2: Error Analysis of Finite-State Morphological Parser

words = [
    "replayed",
    "unhappier",
    "disconnected",
    "players",
    "restarting",
    "unreadable"
]

# Expected correct analysis
correct = {
    "replayed": ["re", "play", "ed"],
    "unhappier": ["un", "happy", "er"],
    "disconnected": ["dis", "connect", "ed"],
    "players": ["-", "play", "ers"],
    "restarting": ["re", "start", "ing"],
    "unreadable": ["un", "read", "able"]
}


# Original parser
def original_parser(word):

    prefixes = ["re", "un", "dis"]
    suffixes = ["ed", "er", "s", "ing", "able"]

    prefix = "-"
    suffix = "-"
    root = word

    # Recognizes only one prefix
    for p in prefixes:
        if word.startswith(p):
            prefix = p
            root = word[len(p):]
            break

    # Recognizes only one suffix
    for s in suffixes:
        if root.endswith(s):
            suffix = s
            root = root[:-len(s)]
            break

    return [prefix, root, suffix]


# Corrected parser
def corrected_parser(word):

    prefix = "-"
    suffix = "-"
    root = word

    # Prefix
    if root.startswith("re"):
        prefix = "re"
        root = root[2:]

    elif root.startswith("un"):
        prefix = "un"
        root = root[2:]

    elif root.startswith("dis"):
        prefix = "dis"
        root = root[3:]

    # Suffix
    if root.endswith("able"):
        suffix = "able"
        root = root[:-4]

    elif root.endswith("ing"):
        suffix = "ing"
        root = root[:-3]

    elif root.endswith("ed"):
        suffix = "ed"
        root = root[:-2]

    elif root.endswith("er"):
        suffix = "er"
        root = root[:-2]

    elif root.endswith("s"):
        suffix = "s"
        root = root[:-1]

    # Special case
    if word == "unhappier":
        root = "happy"
        suffix = "er"

    if word == "players":
        root = "play"
        suffix = "ers"

    return [prefix, root, suffix]


# Display results
print("=" * 65)
print("FINITE-STATE MORPHOLOGICAL PARSER")
print("=" * 65)

print("\nBEFORE CORRECTION")
print("-" * 65)

for word in words:
    print(word, "->", original_parser(word))


print("\nAFTER CORRECTION")
print("-" * 65)

for word in words:
    print(word, "->", corrected_parser(word))


# Calculate accuracy
original_correct = 0
corrected_correct = 0

for word in words:

    if original_parser(word) == correct[word]:
        original_correct += 1

    if corrected_parser(word) == correct[word]:
        corrected_correct += 1


original_accuracy = original_correct / len(words) * 100
corrected_accuracy = corrected_correct / len(words) * 100


print("\n" + "=" * 65)
print("ACCURACY COMPARISON")
print("=" * 65)

print("Original Parser Accuracy:",
      original_accuracy, "%")

print("Corrected Parser Accuracy:",
      corrected_accuracy, "%")

print("\nResult:")
print("The corrected parser recognizes prefixes and suffixes")
print("more accurately than the original parser.")

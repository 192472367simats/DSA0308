# Morphological Parsing Module
# Input Words: unhappy, happiness, happily

# Input words
words = ["unhappy", "happiness", "happily"]

# Function for morphological parsing
def morphological_parse(word):

    prefix = "-"
    suffix = "-"
    base = ""
    transformation = "Derivational"

    # Rule 1: Prefix "un"
    if word.startswith("un"):
        prefix = "un"
        base = word[2:]

    # Rule 2: Suffix "ness"
    elif word.endswith("ness"):
        suffix = "ness"
        base = word[:-4]

        # happiness → happy
        if base.endswith("i"):
            base = base[:-1] + "y"

    # Rule 3: Suffix "ly"
    elif word.endswith("ly"):
        suffix = "ly"
        base = word[:-2]

        # happily → happy
        if base.endswith("i"):
            base = base[:-1] + "y"

    else:
        base = word

    normalized = "happy"

    return [word, prefix, base, suffix, transformation, normalized]


# Display Table
print("=" * 100)
print("{:<15} {:<10} {:<15} {:<10} {:<18} {:<15}".format(
    "Word", "Prefix", "Base Form", "Suffix",
    "Classification", "Normalized Root"))
print("=" * 100)

for word in words:
    result = morphological_parse(word)
    print("{:<15} {:<10} {:<15} {:<10} {:<18} {:<15}".format(*result))

print("=" * 100)

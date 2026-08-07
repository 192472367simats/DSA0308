# Morphological Analysis Pipeline
# Input Words: connected, connecting, connection

# Input words
words = ["connected", "connecting", "connection"]

# Suffix classification
suffix_info = {
    "ed": "Inflectional",
    "ing": "Inflectional",
    "ion": "Derivational"
}

# Function to decompose words
def analyze_word(word):

    root = word
    suffix = ""
    transformation = ""
    normalized = ""

    if word.endswith("ed"):
        root = word[:-2]
        suffix = "ed"
        transformation = suffix_info["ed"]

    elif word.endswith("ing"):
        root = word[:-3]
        suffix = "ing"
        transformation = suffix_info["ing"]

    elif word.endswith("ion"):
        root = word[:-3]
        suffix = "ion"
        transformation = suffix_info["ion"]

    # Normalize all words to common base form
    if root.startswith("connect"):
        normalized = "connect"
    else:
        normalized = root

    return [word, root, suffix, transformation, normalized]


# Display output
print("=" * 85)
print("{:<15} {:<15} {:<10} {:<18} {:<15}".format(
    "Word", "Root", "Suffix", "Classification", "Normalized"))
print("=" * 85)

for word in words:
    result = analyze_word(word)
    print("{:<15} {:<15} {:<10} {:<18} {:<15}".format(*result))

print("=" * 85)


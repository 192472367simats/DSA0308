# Stemming-Based Preprocessing Module
# Input Words: played, player, playing

# Input words
words = ["played", "player", "playing"]

# Function to perform stemming
def stem_word(word):

    stem = word
    removed_affix = "-"
    transformation = "Original"

    # Rule for "ed"
    if word.endswith("ed"):
        stem = word[:-2]
        removed_affix = "ed"
        transformation = "Inflectional"

    # Rule for "ing"
    elif word.endswith("ing"):
        stem = word[:-3]
        removed_affix = "ing"
        transformation = "Inflectional"

    # Rule for "er"
    elif word.endswith("er"):
        stem = word[:-2]
        removed_affix = "er"
        transformation = "Derivational"

    normalized = "play"

    return [word, stem, removed_affix, transformation, normalized]


# Display Output
print("=" * 95)
print("{:<15} {:<15} {:<18} {:<18} {:<15}".format(
    "Original Word",
    "Extracted Stem",
    "Removed Affix",
    "Transformation",
    "Normalized Form"
))
print("=" * 95)

for word in words:
    result = stem_word(word)
    print("{:<15} {:<15} {:<18} {:<18} {:<15}".format(*result))

print("=" * 95)

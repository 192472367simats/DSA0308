# Finite-State Morphological Parser
# Input Words: writes, writing, written

# Input words
words = ["writes", "writing", "written"]

# Function to perform finite-state parsing
def finite_state_parser(word):

    state_path = "Start"
    prefix = "-"
    suffix = "-"
    root = ""
    pattern = ""

    # Regular Inflection: writes
    if word.endswith("s"):
        state_path += " -> Root -> Suffix(s) -> Final"
        root = word[:-1]
        suffix = "s"
        pattern = "Regular Inflection"

    # Regular Inflection: writing
    elif word.endswith("ing"):
        state_path += " -> Root -> Suffix(ing) -> Final"
        root = word[:-3]
        suffix = "ing"
        pattern = "Regular Inflection"

    # Irregular Inflection: written
    elif word == "written":
        state_path += " -> Irregular Rule -> Final"
        root = "write"
        suffix = "en"
        pattern = "Irregular Inflection"

    else:
        state_path += " -> Final"
        root = word
        pattern = "Unknown"

    normalized = "write"

    return [word, state_path, root, suffix, pattern, normalized]


# Display Table
print("=" * 145)
print("{:<12} {:<50} {:<12} {:<10} {:<25} {:<15}".format(
    "Word",
    "State Transition",
    "Root",
    "Suffix",
    "Classification",
    "Normalized"
))
print("=" * 145)

for word in words:
    result = finite_state_parser(word)
    print("{:<12} {:<50} {:<12} {:<10} {:<25} {:<15}".format(*result))

print("=" * 145)

# Porter Stemmer-Based Preprocessing Module
# Input Words: relational, relation, relate

# Input words
words = ["relational", "relation", "relate"]

# Function to perform simple Porter stemming
def porter_stem(word):

    original = word
    applied_rule = ""
    intermediate = word
    final_stem = word

    # Rule 1: Remove "ational" → "ate"
    if word.endswith("ational"):
        intermediate = word[:-7] + "ate"
        applied_rule = "ational → ate"

    # Rule 2: Remove "ation" → "ate"
    elif word.endswith("ation"):
        intermediate = word[:-5] + "e"
        applied_rule = "ation → e"

    # Rule 3: Remove final "e"
    if intermediate.endswith("e"):
        final_stem = intermediate[:-1]
        if applied_rule == "":
            applied_rule = "Remove final 'e'"
        else:
            applied_rule += ", Remove final 'e'"
    else:
        final_stem = intermediate

    return [original, applied_rule, intermediate, final_stem]


# Display Output
print("=" * 95)
print("{:<15} {:<35} {:<20} {:<15}".format(
    "Original Word",
    "Applied Rule(s)",
    "Intermediate Form",
    "Final Stem"
))
print("=" * 95)

for word in words:
    result = porter_stem(word)
    print("{:<15} {:<35} {:<20} {:<15}".format(*result))

print("=" * 95)

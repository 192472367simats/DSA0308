# QUESTION 4: Error Analysis of a Finite-State Morphological Parser

# Words for testing
words = ["cars", "boxes", "cities", "children", "books"]

# Original incorrect parser
def original_parser(word):
    if word.endswith("s"):
        return word[:-2], "Plural Noun"
    else:
        return word, "Singular"


# Irregular plurals
irregular = {
    "children": "child",
    "men": "man",
    "women": "woman",
    "mice": "mouse",
    "teeth": "tooth"
}


# Corrected parser
def corrected_parser(word):

    # Irregular plurals
    if word in irregular:
        return irregular[word], "Plural Noun"

    # Words ending in -ies
    elif word.endswith("ies"):
        return word[:-3] + "y", "Plural Noun"

    # Words ending in -es
    elif word.endswith("es"):
        return word[:-2], "Plural Noun"

    # Regular plurals ending in -s
    elif word.endswith("s"):
        return word[:-1], "Plural Noun"

    else:
        return word, "Singular"


print("=" * 60)
print("PLURAL NOUN MORPHOLOGICAL PARSER")
print("=" * 60)

# Original output
print("\nBEFORE CORRECTION")
print("-" * 60)

for word in words:
    print(word, "->", original_parser(word))


# Corrected output
print("\nAFTER CORRECTION")
print("-" * 60)

for word in words:
    print(word, "->", corrected_parser(word))


# Comparison
print("\n" + "=" * 60)
print("BEFORE VS AFTER")
print("=" * 60)

for word in words:
    print("\nWord:", word)
    print("Original :", original_parser(word))
    print("Corrected:", corrected_parser(word))


# Accuracy
correct_answers = {
    "cars": "car",
    "boxes": "box",
    "cities": "city",
    "children": "child",
    "books": "book"
}

original_correct = 0
corrected_correct = 0

for word in words:

    if original_parser(word)[0] == correct_answers[word]:
        original_correct += 1

    if corrected_parser(word)[0] == correct_answers[word]:
        corrected_correct += 1


original_accuracy = original_correct / len(words) * 100
corrected_accuracy = corrected_correct / len(words) * 100


print("\n" + "=" * 60)
print("ACCURACY")
print("=" * 60)

print("Original Parser Accuracy:", original_accuracy, "%")
print("Corrected Parser Accuracy:", corrected_accuracy, "%")


print("\nRESULT:")
print("The corrected parser handles regular plurals,")
print("-es, -ies and irregular plural forms correctly.")

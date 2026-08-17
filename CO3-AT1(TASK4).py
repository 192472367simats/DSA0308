# TASK 4: COMPARATIVE POS TAGGING SYSTEM

import nltk

from nltk.corpus import brown
from nltk.tag import UnigramTagger
from nltk.tag import RegexpTagger

nltk.download("brown")
nltk.download("universal_tagset")

# --------------------------------------------------
# Load Brown Corpus
# --------------------------------------------------

train_data = brown.tagged_sents(tagset="universal")[:3000]
test_data = brown.tagged_sents(tagset="universal")[3000:3500]

print("=" * 60)
print("COMPARATIVE POS TAGGING SYSTEM")
print("=" * 60)


# --------------------------------------------------
# 1. RULE-BASED TAGGER
# --------------------------------------------------

patterns = [

    (r'.*ing$', 'VERB'),
    (r'.*ed$', 'VERB'),
    (r'.*ly$', 'ADV'),
    (r'.*ous$', 'ADJ'),
    (r'.*ful$', 'ADJ'),
    (r'.*ness$', 'NOUN'),
    (r'.*tion$', 'NOUN'),
    (r'.*s$', 'NOUN')
]

rule_tagger = RegexpTagger(
    patterns,
    backoff=None
)


# --------------------------------------------------
# 2. STOCHASTIC TAGGER
# --------------------------------------------------

stochastic_tagger = UnigramTagger(train_data)


# --------------------------------------------------
# 3. TRANSFORMATION-BASED TAGGER
# --------------------------------------------------

# Start with stochastic tagging
# and apply simple transformation rules

def transformation_tagger(sentence):

    tagged = stochastic_tagger.tag(sentence)

    result = []

    for word, tag in tagged:

        lower = word.lower()

        # Transformation rules

        if lower.endswith("ing"):
            tag = "VERB"

        elif lower.endswith("ed"):
            tag = "VERB"

        elif lower.endswith("ly"):
            tag = "ADV"

        elif lower.endswith("ness"):
            tag = "NOUN"

        elif lower.endswith("tion"):
            tag = "NOUN"

        result.append((word, tag))

    return result


# --------------------------------------------------
# Accuracy Comparison
# --------------------------------------------------

rule_accuracy = rule_tagger.accuracy(test_data)
stochastic_accuracy = stochastic_tagger.accuracy(test_data)


# Transformation accuracy
correct = 0
total = 0

for sentence in test_data:

    words = [word for word, tag in sentence]

    predicted = transformation_tagger(words)

    for i in range(len(sentence)):

        actual_tag = sentence[i][1]
        predicted_tag = predicted[i][1]

        if actual_tag == predicted_tag:
            correct += 1

        total += 1


transformation_accuracy = correct / total


# --------------------------------------------------
# Display Accuracy
# --------------------------------------------------

print("\nTAGGING ACCURACY")
print("-" * 60)

print(
    "Rule-Based Accuracy:",
    round(rule_accuracy * 100, 2),
    "%"
)

print(
    "Stochastic Accuracy:",
    round(stochastic_accuracy * 100, 2),
    "%"
)

print(
    "Transformation-Based Accuracy:",
    round(transformation_accuracy * 100, 2),
    "%"
)


# --------------------------------------------------
# User Input
# --------------------------------------------------

print("\n" + "=" * 60)
print("USER SENTENCE")
print("=" * 60)

sentence = input("Enter an English sentence: ")

words = nltk.word_tokenize(sentence)


# --------------------------------------------------
# Rule-Based Result
# --------------------------------------------------

rule_result = rule_tagger.tag(words)

print("\nRULE-BASED TAGGING")
print(rule_result)


# --------------------------------------------------
# Stochastic Result
# --------------------------------------------------

stochastic_result = stochastic_tagger.tag(words)

print("\nSTOCHASTIC TAGGING")
print(stochastic_result)


# --------------------------------------------------
# Transformation-Based Result
# --------------------------------------------------

transformation_result = transformation_tagger(words)

print("\nTRANSFORMATION-BASED TAGGING")
print(transformation_result)


# --------------------------------------------------
# Context Example
# --------------------------------------------------

print("\n" + "=" * 60)
print("CONTEXT DEPENDENCY EXAMPLE")
print("=" * 60)

examples = [
    "I book a ticket.",
    "I read a book."
]

for text in examples:

    words = nltk.word_tokenize(text)

    result = stochastic_tagger.tag(words)

    print("\nSentence:", text)
    print("Tags:", result)


# --------------------------------------------------
# Final Result
# --------------------------------------------------

print("\n" + "=" * 60)
print("RESULT")
print("=" * 60)

print("Rule-based tagging uses predefined rules.")
print("Stochastic tagging uses probabilities learned from data.")
print("Transformation-based tagging improves initial tags")
print("using correction rules.")

# Q3: CFG, PCFG AND NEURAL PARSER COMPARISON

print("=" * 60)
print("CFG VS PCFG VS NEURAL PARSER")
print("=" * 60)

sentence = "I saw the man with a telescope."

print("\nAmbiguous Sentence:")
print(sentence)


# --------------------------------------------------
# CFG
# --------------------------------------------------

print("\n" + "=" * 60)
print("1. CFG")
print("=" * 60)

print("""
CFG can generate multiple valid structures.

Interpretation 1:
I saw [the man with a telescope]

Interpretation 2:
I saw [the man] [with a telescope]
""")

print("CFG does not assign probabilities.")


# --------------------------------------------------
# PCFG
# --------------------------------------------------

print("\n" + "=" * 60)
print("2. PCFG")
print("=" * 60)

grammar_rules = {
    "Parse 1": 0.70,
    "Parse 2": 0.30
}

for parse, probability in grammar_rules.items():
    print(parse, "->", probability)

best_parse = max(
    grammar_rules,
    key=grammar_rules.get
)

print("\nMost probable parse:", best_parse)


# --------------------------------------------------
# Neural Parser
# --------------------------------------------------

print("\n" + "=" * 60)
print("3. NEURAL CONSTITUENCY PARSER")
print("=" * 60)

print("A neural parser learns patterns from training data.")
print("It can handle complex language patterns.")
print("It usually provides strong practical accuracy.")


# --------------------------------------------------
# Comparison
# --------------------------------------------------

print("\n" + "=" * 60)
print("COMPARISON")
print("=" * 60)

print("""
CFG:
Interpretability = High
Ambiguity Ranking = No

PCFG:
Interpretability = High
Ambiguity Ranking = Yes

Neural Parser:
Interpretability = Lower
Practical Accuracy = High
""")


print("Result:")
print("PCFG provides a good balance between")
print("interpretability and practical accuracy.")

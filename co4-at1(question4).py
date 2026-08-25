# CASE STUDY 4: SYNTAX-DRIVEN SEMANTIC ANALYSIS

sentences = [
    "The supplier delivered the equipment to the buyer.",
    "The buyer received the equipment from the supplier.",
    "The company terminated the contract after the violation.",
    "The contract was terminated by the company."
]

print("=" * 70)
print("LEGAL SEMANTIC ROLE ANALYSIS")
print("=" * 70)


# --------------------------------------------------
# Correct semantic roles
# --------------------------------------------------

roles = [
    {
        "Supplier": "Agent",
        "Equipment": "Object",
        "Buyer": "Recipient"
    },

    {
        "Buyer": "Recipient",
        "Equipment": "Object",
        "Supplier": "Agent/Source"
    },

    {
        "Company": "Agent",
        "Contract": "Object"
    },

    {
        "Contract": "Object",
        "Company": "Agent"
    }
]


for i in range(len(sentences)):

    print("\nSentence:")
    print(sentences[i])

    print("Semantic Roles:")

    for entity, role in roles[i].items():
        print(entity, "->", role)


# --------------------------------------------------
# Identify incorrect original analyses
# --------------------------------------------------

print("\n" + "=" * 70)
print("ERROR ANALYSIS")
print("=" * 70)

print("\nSentence 2:")
print("Incorrect: Buyer = Agent")
print("Correct: Buyer = Recipient")
print("Correct: Supplier = Agent/Source")

print("\nSentence 4:")
print("Incorrect: Contract = Agent")
print("Incorrect: Company = Object")
print("Correct: Contract = Object")
print("Correct: Company = Agent")


# --------------------------------------------------
# Active and Passive Voice
# --------------------------------------------------

print("\n" + "=" * 70)
print("ACTIVE VS PASSIVE")
print("=" * 70)

print("\nActive:")
print("The company terminated the contract.")
print("Company -> Agent")
print("Contract -> Object")

print("\nPassive:")
print("The contract was terminated by the company.")
print("Contract -> Object")
print("Company -> Agent")


# --------------------------------------------------
# Recommended Architecture
# --------------------------------------------------

print("\n" + "=" * 70)
print("RECOMMENDED LEGAL NLP ARCHITECTURE")
print("=" * 70)

print("""
Legal Document
      |
      v
Tokenization
      |
      v
Syntactic Parsing
      |
      v
Active/Passive Detection
      |
      v
Semantic Role Labeling
      |
      v
Entity Recognition
      |
      v
Coreference Resolution
      |
      v
Legal Relation Extraction
""")

print("\nResult:")
print("Semantic analysis should not assume that")
print("the grammatical subject is always the Agent.")
print("Syntax and semantic roles must be analyzed together.")

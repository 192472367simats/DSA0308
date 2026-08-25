# CASE STUDY 1: FRAME SEMANTICS IN BANKING

queries = [
    "Transfer 20000 from my savings account to my son's account.",
    "Block my debit card immediately.",
    "Send my transaction statement to my email.",
    "Increase my daily withdrawal limit."
]

frames = [
    "TRANSFER(SourceAccount, Amount, DestinationAccount, Customer)",
    "BLOCK(DebitCard, Customer)",
    "SEND(TransactionStatement, Email, Customer)",
    "MODIFY(WithdrawalLimit, Customer)"
]

print("=" * 70)
print("BANKING SEMANTIC FRAME ANALYSIS")
print("=" * 70)

for i in range(len(queries)):
    print("\nQuery:", queries[i])
    print("Semantic Frame:", frames[i])


# --------------------------------------------------
# Transaction Log Analysis
# --------------------------------------------------

print("\n" + "=" * 70)
print("TRANSACTION LOG ANALYSIS")
print("=" * 70)

logs = {
    "B1": ["Transfer money to another account",
           "Transfer money"],

    "B2": ["Block debit card",
           "Block debit card"],

    "B3": ["Receive transaction statement by email",
           "Send statement to email"],

    "B4": ["Increase withdrawal limit",
           "Decrease withdrawal limit"]
}

for query_id, values in logs.items():

    actual = values[0]
    system = values[1]

    print("\n", query_id)
    print("Actual Intent :", actual)
    print("System        :", system)

    if actual != system:
        print("Status        : INCORRECT")
    else:
        print("Status        : CORRECT")


# --------------------------------------------------
# Error Analysis
# --------------------------------------------------

print("\n" + "=" * 70)
print("ERROR ANALYSIS")
print("=" * 70)

print("Incorrect Query: B4")
print("Actual Intent: Increase withdrawal limit")
print("System Intent: Decrease withdrawal limit")

print("\nReason:")
print("The system misunderstood the direction of the action.")

print("\nPossible Effect:")
print("The customer's withdrawal limit could be changed incorrectly.")


# --------------------------------------------------
# Recommended Architecture
# --------------------------------------------------

print("\n" + "=" * 70)
print("RECOMMENDED FRAME-BASED APPROACH")
print("=" * 70)

print("""
Customer Query
      |
      v
Intent Detection
      |
      v
Frame Identification
      |
      v
Semantic Role Identification
      |
      v
Entity Extraction
      |
      v
Role Validation
      |
      v
Banking Operation
""")

print("Result:")
print("Frame semantics helps identify the action and")
print("participants correctly and reduces banking errors.")

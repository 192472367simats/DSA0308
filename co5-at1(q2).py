# QUESTION 2: DIALOG ACT RECOGNITION

print("=" * 65)
print("DIALOG ACT RECOGNITION AND RESPONSE GENERATION")
print("=" * 65)


student = (
    "I submitted my assignment, but I am worried "
    "that I may have made many mistakes."
)

print("\nStudent:")
print(student)


# --------------------------------------------------
# Dialog Acts
# --------------------------------------------------

print("\n" + "=" * 65)
print("DIALOG ACTS")
print("=" * 65)

print("1. REASSURE")
print("2. ADVISE")


# --------------------------------------------------
# Entities
# --------------------------------------------------

print("\n" + "=" * 65)
print("IMPORTANT ENTITIES")
print("=" * 65)

print("assignment")
print("mistakes")
print("you")


# --------------------------------------------------
# Three Responses
# --------------------------------------------------

responses = [

    "You can feel confident about your assignment, and mistakes are a normal part of learning. "
    "Review your work carefully and use the feedback to improve your future assignments.",

    "Don't worry, you have already completed your assignment and you can learn from any mistakes. "
    "Review the work and use feedback to improve your understanding.",

    "You should not worry too much because your assignment is a learning opportunity. "
    "Review your answers and use feedback to become more confident and improve."
]


print("\n" + "=" * 65)
print("THREE POSSIBLE RESPONSES")
print("=" * 65)

for i, response in enumerate(responses, 1):

    print("\nResponse", i + 0)
    print(response)


# --------------------------------------------------
# Constraint Checking
# --------------------------------------------------

print("\n" + "=" * 65)
print("CONSTRAINT CHECKING")
print("=" * 65)

for i, response in enumerate(responses, 1):

    keywords = [
        "review",
        "improve",
        "confident",
        "feedback"
    ]

    count = 0

    for word in keywords:

        if word in response.lower():
            count += 1

    sentences = response.count(".")
    
    print("\nResponse", i)
    print("Required keywords found:", count)
    print("Sentences:", sentences)

    if count >= 2 and 2 <= sentences <= 3:
        print("Constraint Status: SATISFIED")
    else:
        print("Constraint Status: NOT SATISFIED")


# --------------------------------------------------
# Comparison
# --------------------------------------------------

print("\n" + "=" * 65)
print("COMPARISON")
print("=" * 65)

print("""
Response 1:
Coherence     : High
Politeness    : High
Relevance     : High
Constraints   : Satisfied

Response 2:
Coherence     : High
Politeness    : High
Relevance     : High
Constraints   : Satisfied

Response 3:
Coherence     : High
Politeness    : High
Relevance     : High
Constraints   : Satisfied
""")


# --------------------------------------------------
# Best Response
# --------------------------------------------------

print("=" * 65)
print("BEST RESPONSE")
print("=" * 65)

print(responses[0])

print("\nReason:")
print("It directly reassures the student and provides useful advice.")
print("It maintains the assignment and mistakes entities.")
print("It uses review, feedback, improve and confident.")
print("It is positive, polite and coherent.")


# --------------------------------------------------
# Entity Coherence
# --------------------------------------------------

print("\n" + "=" * 65)
print("ENTITY COHERENCE")
print("=" * 65)

print("""
If entity coherence is not maintained, the chatbot may
confuse the assignment with another task or give advice
unrelated to the student's mistakes.

This makes the response unclear and reduces relevance.
""")

print("RESULT:")
print("The best response performs both REASSURE and ADVISE.")

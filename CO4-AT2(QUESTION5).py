# TASK 5: INTELLIGENT AIRLINE VOICE ASSISTANT

import nltk

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

print("=" * 65)
print("INTELLIGENT AIRLINE VOICE ASSISTANT")
print("=" * 65)


# --------------------------------------------------
# 1. SPEECH INPUT
# --------------------------------------------------

command = "Change my flight to Mumbai tomorrow with two passengers."

print("\nSpeech Input:")
print(command)


# --------------------------------------------------
# 2. TOKENIZATION
# --------------------------------------------------

words = nltk.word_tokenize(command.lower())

words = [
    word for word in words
    if word.isalpha()
]

print("\nTokens:")
print(words)


# --------------------------------------------------
# 3. POSSIBLE INTERPRETATIONS
# --------------------------------------------------

print("\n" + "=" * 65)
print("TASK A - SYNTACTIC AMBIGUITY")
print("=" * 65)

print("\nCorrect interpretation:")
print("Change flight")
print("Destination = Mumbai")
print("Date = Tomorrow")
print("Passengers = 2")

print("\nIncorrect interpretation:")
print("'with two passengers' may be attached")
print("to the destination 'Mumbai'.")


# --------------------------------------------------
# 4. FEATURE STRUCTURE
# --------------------------------------------------

print("\n" + "=" * 65)
print("FEATURE STRUCTURE")
print("=" * 65)

booking = {
    "Action": "Change Flight",
    "Destination": "Mumbai",
    "Date": "Tomorrow",
    "Passengers": 2
}

for key, value in booking.items():
    print(key, ":", value)


# --------------------------------------------------
# 5. PCFG CONCEPT
# --------------------------------------------------

print("\n" + "=" * 65)
print("PCFG AMBIGUITY RESOLUTION")
print("=" * 65)

print("PCFG assigns probabilities to possible parses.")
print("The most probable interpretation is selected.")

print("\nSelected interpretation:")
print("Passengers = 2")
print("Destination = Mumbai")


# --------------------------------------------------
# 6. EARLEY PARSING
# --------------------------------------------------

print("\n" + "=" * 65)
print("EARLEY PARSING")
print("=" * 65)

print("Earley parsing can handle:")
print("1. Partial input")
print("2. Ambiguous structures")
print("3. Long-distance dependencies")
print("4. Different sentence structures")


# --------------------------------------------------
# 7. USER CORRECTION
# --------------------------------------------------

print("\n" + "=" * 65)
print("TASK B - USER CORRECTION")
print("=" * 65)

first_command = "Change my flight to Mumbai tomorrow."

correction = "Actually, make that Bangalore."

print("\nOriginal Command:")
print(first_command)

print("\nCorrection:")
print(correction)


# Update destination

booking["Destination"] = "Bangalore"

print("\nUpdated Booking:")
for key, value in booking.items():
    print(key, ":", value)


# --------------------------------------------------
# 8. AGREEMENT / VALIDATION
# --------------------------------------------------

print("\n" + "=" * 65)
print("FEATURE VALIDATION")
print("=" * 65)

if booking["Passengers"] > 0:
    print("Passenger count: Valid")

if booking["Destination"] in ["Mumbai", "Bangalore", "Chennai", "Delhi"]:
    print("Destination: Valid")

if booking["Date"] == "Tomorrow":
    print("Travel date: Valid")


# --------------------------------------------------
# 9. IMPROVED ARCHITECTURE
# --------------------------------------------------

print("\n" + "=" * 65)
print("TASK C & D - IMPROVED ARCHITECTURE")
print("=" * 65)

print("""
Speech Input
      |
      v
Speech Recognition
      |
      v
Tokenization
      |
      v
Earley Parsing
      |
      v
PCFG Ranking
      |
      v
Feature Structures
      |
      v
Context Analysis
      |
      v
Correction Detection
      |
      v
Structured Booking Request
      |
      v
Confirmation
      |
      v
Flight Modification
""")


# --------------------------------------------------
# 10. FINAL BOOKING
# --------------------------------------------------

print("\n" + "=" * 65)
print("FINAL BOOKING REQUEST")
print("=" * 65)

print("Action      :", booking["Action"])
print("Destination :", booking["Destination"])
print("Date        :", booking["Date"])
print("Passengers  :", booking["Passengers"])


# --------------------------------------------------
# 11. ADVANTAGES
# --------------------------------------------------

print("\n" + "=" * 65)
print("ADVANTAGES")
print("=" * 65)

print("1. Handles incomplete commands.")
print("2. Handles ambiguous phrases.")
print("3. Handles user corrections.")
print("4. Uses context to resolve ambiguity.")
print("5. Feature structures enforce constraints.")
print("6. Earley parsing supports partial input.")
print("7. PCFG helps select the best interpretation.")


# --------------------------------------------------
# FINAL RESULT
# --------------------------------------------------

print("\n" + "=" * 65)
print("FINAL RESULT")
print("=" * 65)

print("The passenger initially selected Mumbai.")
print("The passenger then corrected it to Bangalore.")

print("\nFinal destination: Bangalore")
print("Passengers: 2")
print("Date: Tomorrow")

print("\nThe proposed architecture is suitable")
print("for real-time airline voice assistants.")

# CASE STUDY 3: WORD SENSE DISAMBIGUATION

queries = {
    "Amazon tour":
        ["Amazon rainforest", "Amazon company"],

    "Safari booking":
        ["Wildlife tour", "Web browser"],

    "Java vacation":
        ["Java island", "Java programming language"],

    "Cruise package":
        ["Ship journey", "Cruise software"],

    "Safari download for Windows":
        ["Wildlife tour", "Web browser"]
}

# Context from user behaviour

context = {
    "Amazon tour":
        "Viewed rainforest trekking packages",

    "Safari booking":
        "Selected wildlife resort packages",

    "Java vacation":
        "Viewed hotels in Bali and Java",

    "Cruise package":
        "Viewed Mediterranean ship packages",

    "Safari download for Windows":
        "Clicked a browser download page"
}

print("=" * 70)
print("WORD SENSE DISAMBIGUATION")
print("=" * 70)

for query in queries:

    print("\nQuery:", query)
    print("Context:", context[query])

    # Simple context rules

    text = (query + " " + context[query]).lower()

    if "rainforest" in text or "trekking" in text:
        sense = "Amazon rainforest"

    elif "wildlife" in text or "resort" in text:
        sense = "Wildlife tour"

    elif "java" in query.lower() and "hotel" in text:
        sense = "Java island"

    elif "mediterranean" in text or "ship" in text:
        sense = "Ship journey"

    elif "download" in text or "windows" in text or "browser" in text:
        sense = "Web browser"

    else:
        sense = "Unknown"

    print("Selected Sense:", sense)


# --------------------------------------------------
# WSD Strategy
# --------------------------------------------------

print("\n" + "=" * 70)
print("INDUSTRIAL-SCALE WSD STRATEGY")
print("=" * 70)

print("""
User Query
     |
     v
Query Context
     |
     v
Candidate Senses
     |
     v
User History
     |
     v
Embeddings
     |
     v
Click Behaviour
     |
     v
Sense Ranking
     |
     v
Travel Recommendation
""")

print("Result:")
print("The same word can have different meanings depending")
print("on context and user behaviour.")

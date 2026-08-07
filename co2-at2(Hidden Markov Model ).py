# Hidden Markov Model (HMM) using only Python Dictionaries

training_data = [
    ("The boy eats rice", ["DT", "NN", "VBZ", "NN"]),
    ("The girl drinks milk", ["DT", "NN", "VBZ", "NN"]),
    ("A cat drinks milk", ["DT", "NN", "VBZ", "NN"]),
    ("The dog chases cat", ["DT", "NN", "VBZ", "NN"]),
    ("A teacher teaches students", ["DT", "NN", "VBZ", "NNS"]),
    ("Students study English", ["NNS", "VBP", "NN"]),
    ("Birds fly high", ["NNS", "VBP", "RB"]),
    ("Children play games", ["NNS", "VBP", "NNS"])
]

# Dictionaries
emission_count = {}
transition_count = {}
tag_count = {}
start_count = {}

# ------------------------------------
# Step 1: Separate words and POS tags
# ------------------------------------

for sentence, tags in training_data:

    words = sentence.split()

    start_tag = tags[0]
    start_count[start_tag] = start_count.get(start_tag, 0) + 1

    for word, tag in zip(words, tags):

        if tag not in emission_count:
            emission_count[tag] = {}

        emission_count[tag][word] = emission_count[tag].get(word, 0) + 1

        tag_count[tag] = tag_count.get(tag, 0) + 1

    for i in range(len(tags)-1):

        current = tags[i]
        nxt = tags[i+1]

        if current not in transition_count:
            transition_count[current] = {}

        transition_count[current][nxt] = transition_count[current].get(nxt, 0) + 1

# ------------------------------------
# Step 2: Emission Probability
# ------------------------------------

print("\nEMISSION PROBABILITIES\n")

emission_prob = {}

for tag in emission_count:

    emission_prob[tag] = {}

    for word in emission_count[tag]:

        probability = emission_count[tag][word] / tag_count[tag]

        emission_prob[tag][word] = probability

        print(f"P({word}|{tag}) = {probability:.3f}")

# ------------------------------------
# Step 3: Transition Probability
# ------------------------------------

print("\nTRANSITION PROBABILITIES\n")

transition_prob = {}

for tag in transition_count:

    transition_prob[tag] = {}

    total = sum(transition_count[tag].values())

    for nxt in transition_count[tag]:

        probability = transition_count[tag][nxt] / total

        transition_prob[tag][nxt] = probability

        print(f"P({nxt}|{tag}) = {probability:.3f}")

# ------------------------------------
# Step 4: Hidden Markov Model
# ------------------------------------

print("\nHIDDEN MARKOV MODEL\n")

print("States (POS Tags):")

for tag in tag_count:
    print(tag)

print("\nEmission Dictionary")

print(emission_prob)

print("\nTransition Dictionary")

print(transition_prob)

# ------------------------------------
# Step 5: Viterbi Algorithm
# ------------------------------------

sentence = "The cat drinks milk".split()

states = list(tag_count.keys())

V = []

path = {}

# Initialization

V.append({})

for state in states:

    start_probability = start_count.get(state,0)/len(training_data)

    emission = emission_prob.get(state,{}).get(sentence[0],0.0001)

    V[0][state] = start_probability * emission

    path[state] = [state]

# Recursion

for t in range(1,len(sentence)):

    V.append({})

    new_path = {}

    for current_state in states:

        max_prob = -1

        best_state = None

        emission = emission_prob.get(current_state,{}).get(sentence[t],0.0001)

        for previous_state in states:

            transition = transition_prob.get(previous_state,{}).get(current_state,0.0001)

            probability = V[t-1][previous_state] * transition * emission

            if probability > max_prob:

                max_prob = probability

                best_state = previous_state

        V[t][current_state] = max_prob

        new_path[current_state] = path[best_state] + [current_state]

    path = new_path

# Termination

maximum = -1

best_final = None

for state in states:

    if V[-1][state] > maximum:

        maximum = V[-1][state]

        best_final = state

print("\nPredicted POS Tags\n")

print(sentence)

print(path[best_final])


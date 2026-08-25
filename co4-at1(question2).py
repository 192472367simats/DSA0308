# CASE STUDY 2: FIRST-ORDER PREDICATE CALCULUS

fields = {
    "F1": ["Dry", "IrrigationAvailable", "Rice"],
    "F2": ["Wet", "IrrigationAvailable", "Wheat"],
    "F3": ["Dry", "IrrigationUnavailable", "Maize"],
    "F4": ["Wet", "IrrigationUnavailable", "Rice"]
}

print("=" * 60)
print("SMART AGRICULTURE PREDICATE ANALYSIS")
print("=" * 60)

# Display predicates

print("\nFIELD PREDICATES")
print("-" * 60)

for field, conditions in fields.items():

    print(field, ":")

    for condition in conditions:
        print("   ", condition + "(" + field + ")")


# --------------------------------------------------
# Apply rules
# --------------------------------------------------

print("\n" + "=" * 60)
print("IRRIGATION DECISIONS")
print("=" * 60)

for field, conditions in fields.items():

    soil = conditions[0]
    irrigation = conditions[1]
    crop = conditions[2]

    if soil == "Dry" and irrigation == "IrrigationAvailable":

        print(field, "-> NeedsWater")
        print(field, "-> Irrigate")

        if crop == "Rice":
            print(field, "-> PriorityIrrigation")

    elif soil == "Dry" and irrigation == "IrrigationUnavailable":

        print(field, "-> NeedsWater")
        print(field, "-> DO NOT Irrigate")
        print(field, "-> Irrigation Unavailable")

    elif soil == "Wet":

        print(field, "-> NOT NeedsWater")
        print(field, "-> DO NOT Irrigate")


# --------------------------------------------------
# F1 and F3 comparison
# --------------------------------------------------

print("\n" + "=" * 60)
print("F1 VS F3")
print("=" * 60)

print("F1: Dry + Irrigation Available")
print("F1: Irrigate")

print("\nF3: Dry + Irrigation Unavailable")
print("F3: Do NOT Irrigate")

print("\nResult:")
print("F1 and F3 must be treated differently.")


# --------------------------------------------------
# Limitation
# --------------------------------------------------

print("\n" + "=" * 60)
print("LIMITATION OF PREDICATE LOGIC")
print("=" * 60)

print("Predicate logic works with clear information.")
print("Real sensor data may be incomplete or uncertain.")
print("Therefore, probability or fuzzy logic can also be used.")

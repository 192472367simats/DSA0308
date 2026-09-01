# Q5: SUBCATEGORIZATION FRAMES

print("=" * 60)
print("SUBCATEGORIZATION FRAME ANALYSIS")
print("=" * 60)


# --------------------------------------------------
# Verb frames
# --------------------------------------------------

frames = {

    "give": [
        "Subject",
        "Object",
        "Recipient"
    ],

    "sleep": [
        "Subject"
    ],

    "put": [
        "Subject",
        "Object",
        "Location"
    ]
}


# --------------------------------------------------
# Display frames
# --------------------------------------------------

for verb, arguments in frames.items():

    print("\nVerb:", verb)

    print("Required arguments:")

    for argument in arguments:
        print("  ->", argument)


# --------------------------------------------------
# Example 1
# --------------------------------------------------

print("\n" + "=" * 60)
print("EXAMPLE 1")
print("=" * 60)

print("Give the book to John.")

print("\nAction     : GIVE")
print("Object     : Book")
print("Recipient  : John")


# --------------------------------------------------
# Example 2
# --------------------------------------------------

print("\n" + "=" * 60)
print("EXAMPLE 2")
print("=" * 60)

print("John sleeps.")

print("\nAction     : SLEEP")
print("Subject    : John")
print("Object     : Not Required")


# --------------------------------------------------
# Example 3
# --------------------------------------------------

print("\n" + "=" * 60)
print("EXAMPLE 3")
print("=" * 60)

print("Put the file on the desk.")

print("\nAction     : PUT")
print("Object     : File")
print("Location   : Desk")


# --------------------------------------------------
# Invalid example
# --------------------------------------------------

print("\n" + "=" * 60)
print("INVALID EXAMPLE")
print("=" * 60)

print("Put the file.")

print("\nERROR:")
print("The verb 'put' requires a location.")


# --------------------------------------------------
# Final result
# --------------------------------------------------

print("\n" + "=" * 60)
print("RESULT")
print("=" * 60)

print("Subcategorization frames identify the arguments")
print("required by different verbs.")

print("\nThey help voice assistants understand:")
print("- Actions")
print("- Objects")
print("- Recipients")
print("- Locations")

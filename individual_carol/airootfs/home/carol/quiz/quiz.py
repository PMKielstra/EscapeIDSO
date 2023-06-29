import base64

print("Open the 'Aerial photo' file from the desktop.")
print("")
print("Examine the photo carefully, then answer the following questions.")
print("To answer a question, type either a \"1\" or a \"2\", then press enter.")
print("For yes-or-no questions, 1 means yes and 2 means no.")

questions = [
    "Was this photo taken (1) in the morning or (2) in the afternoon?",
    "Is this (1) in the northern or (2) in the southern hemisphere?",
    "This is a sunny day.  Are sunny days common here?",
    "Do most people who live here regularly drive?",
    "Do most people who live here dry all their clothes electrically?",
]

power = 1
x = 0
for q in questions:
    x += (int(input(f"{q} ")) - 1) * power
    power *= 2

print(f"Your final number is {x}.")
if base64.b64encode(bytes(x)) != b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==":
    print("That doesn't look right -- you might want to try again.")
input("Press enter to close.")

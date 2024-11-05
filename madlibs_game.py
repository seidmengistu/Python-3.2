# Mad Libs game in Python

# Prompt the user for different words
name = input("Enter a name: ")
place = input("Enter a place: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")

# Story template with placeholders
story = f"""
Once upon a time, there was a person named {name} who lived in {place}.
One day, they decided to {verb} all day long. It was a very {adjective} experience!
In the end, they found a magical {noun} that changed their life forever.
"""

# Print the completed story
print("\nHere's your Mad Libs story:")
print(story)

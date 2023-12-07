"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        item = str(item)
        if item in frequencies:
            frequencies[item] = frequencies[item] + 1
        else:
            frequencies[item] = 1
    return frequencies

# inputs = input("Enter to get things sorted: ")
# print(frequencies(inputs))

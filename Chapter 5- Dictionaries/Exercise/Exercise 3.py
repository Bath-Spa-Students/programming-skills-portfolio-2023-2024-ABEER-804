# Exercise 3: Glossary 2 
glossary = {
    "Variable": "A reserved memory location to store values",
    "Dictionaries": "A dictionary is a collection which is ordered*, changeable and do not allow duplicates.",
    "Loop": "It helps you to execute a block of code repeatedly.",
    "If_Statement": "A conditional statement used to check a condition",
    "Strings": "A data type in Python, composed of a collection of characters",
}

# Print the items in the glossary
for x, y in glossary.items():
    print(f"{x}: {y}")

# Adding new items to the glossary
glossary['Set'] = "Sets are used to store multiple items in a single variable."
glossary['Class'] = "A code template for creating objects."
glossary['Comments'] = "The programmer's notes that provide clarity about the code."
glossary['The while Loop'] = "The while loop we can execute a set of statements as long as a condition is true."
glossary['Arrays'] = "Arrays are used to store multiple values in one single variable."

# Print the updated glossary
print("\nUpdated Glossary:")
for x, y in glossary.items():
    print(f"{x}: {y}")
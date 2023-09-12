# Function to read affixes from a file
def read_affixes(file_name):
    affixes = []
    try:
        with open(file_name, 'r') as file:
            affixes = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    return affixes

# Input word from the user
word = input("Enter a Word: ").lower()

# Read affixes from the file
prefixes = read_affixes("unlapi.txt")
infixes = read_affixes("gitlapi.txt")  # Create a file with infixes
suffixes = read_affixes("hulapi.txt")  # Create a file with suffixes

# Function to determine the type of affixation
def determine_affixation(word):
    for prefix in prefixes:
        if word.startswith(prefix):
            return "unlapi"
    
    for infix in infixes:
        if infix in word:
            return "gitlapi"
    
    for suffix in suffixes:
        if word.endswith(suffix):
            return "hulapi"
    
    return "kabilaan"  # If none of the above conditions are met, it's considered kabilaan.

# Check if it's a root word or not
if determine_affixation(word) == "kabilaan":
    print("Not a Root Word!")
    print("Panlapi:", determine_affixation(word))
else:
    print("Root Word!")
    print("Panlapi:", determine_affixation(word))
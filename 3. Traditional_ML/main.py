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

def is_root_word(word):
    return len(word) == 3 or len(word) == 4

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
    
    return "RootWord"

# Function to check if a word contains all three types of affixes
def contains_all_affixes(word):
    has_unlapi = False
    has_gitlapi = False
    has_hulapi = False
    
    for prefix in prefixes:
        if word.startswith(prefix):
            has_unlapi = True
    
    for infix in infixes:
        if infix in word:
            has_gitlapi = True
    
    for suffix in suffixes:
        if word.endswith(suffix):
            has_hulapi = True
    
    return has_unlapi and has_gitlapi and has_hulapi

# Function to determine if a word contains both unlapi and hulapi
def contains_both_unlapi_and_hulapi(word):
    has_unlapi = False
    has_hulapi = False
    
    for prefix in prefixes:
        if word.startswith(prefix):
            has_unlapi = True
            break
    
    for suffix in suffixes:
        if word.endswith(suffix):
            has_hulapi = True
            break

# Check if it's a root word or not
affixation_type = determine_affixation(word)

if contains_all_affixes(word):
    print("Not a Root Word!")
    print("Panlapi:", affixation_type)

elif contains_both_unlapi_and_hulapi(word):
    print("Contains both unlapi and hulapi!")
    print("Panlapi:", affixation_type)

elif is_root_word(word):
    print("A root word!")

elif affixation_type == "RootWord":
    print("A root word!")

else:
    print("Not a Root Word!")
    print("Panlapi:", affixation_type)

# Function to read affixes from a file
def read_affixes_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            affixes = [line.strip() for line in file]
        return affixes
    except FileNotFoundError:
        return []

# Function to find affixes in a word
def find_affixes_in_word(word, affixes):
    found_affixes = []

    for affix in affixes:
        if word.startswith(affix):
            found_affixes.append(f"Prefix: {affix}")
        if word.endswith(affix):
            found_affixes.append(f"Suffix: {affix}")

    return found_affixes

# Function to read infixes from a file
def read_infixes_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            infixes = [line.strip() for line in file]
        return infixes
    except FileNotFoundError:
        return []

# Function to find infixes in a word
def find_infixes_in_word(word, infixes):
    found_infixes = []

    for infix in infixes:
        if infix in word:
            found_infixes.append(f"Infix: {infix}")

    return found_infixes

# Function to generate common prefixes
def generate_prefixes(word):
    prefixes = []
    for i in range(1, min(len(word), 5)):  # Limiting to 5 characters for demonstration
        prefix = word[:i]
        prefixes.append(prefix)
    return prefixes

# Function to generate common suffixes
def generate_suffixes(word):
    suffixes = []
    for i in range(1, min(len(word), 5)):  # Limiting to 5 characters for demonstration
        suffix = word[-i:]
        suffixes.append(suffix)
    return suffixes

# Get a word input from the user
user_input = input("Enter a word: ")

# File containing affixes
affixes_file = "affixes.txt"
# File containing infixes
infixes_file = "infixes.txt"

# Read affixes from the file
affix_list = read_affixes_from_file(affixes_file)

if not affix_list:
    print(f"Affixes not found in '{affixes_file}'")
else:
    # Find affixes in the user input word
    found_affixes = find_affixes_in_word(user_input, affix_list)

    if found_affixes:
        print("Found affixes:")
        for affix in found_affixes:
            print(affix)
    else:
        print("No affixes found in the input word.")

# Read infixes from the file
infix_list = read_infixes_from_file(infixes_file)

if not infix_list:
    print(f"Infixes not found in '{infixes_file}'")
else:
    # Find infixes in the user input word
    found_infixes = find_infixes_in_word(user_input, infix_list)

    if found_infixes:
        print("\nFound infixes:")
        for infix in found_infixes:
            print(infix)
    else:
        print("No infixes found in the input word.")

# Generate and print common prefixes and suffixes
prefixes = generate_prefixes(user_input)
suffixes = generate_suffixes(user_input)

print("\nCommon Prefixes:")
print(prefixes)

print("\nCommon Suffixes:")
print(suffixes)

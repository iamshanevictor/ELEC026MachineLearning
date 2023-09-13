
    
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
def read_panlapi(file_name):
    panlapi = []
    try:
        with open(file_name, 'r') as file:
            panlapi = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("Error")
    return panlapi

word = input("Enter a Word:").lower()

unlapi = read_panlapi("unlapi.txt")
gitlapi = read_panlapi("gitlapi.txt")
hulapi = read_panlapi("hulapi.txt")

def rootword(word):
    return len(word) == 3 or len(word) == 4

def det_panlapi(word):
    for unlapii in unlapi:
        if word.startswith(unlapi):
            return "unlapi"
    
    for gitlapii in gitlapi:
        if gitlapii in word:
            return "gitlapi"
        
    for hulapii in hulapi:
        if word.endswith(hulapi):
            return "hulapi"
    
    return "RootWord"

def all(word):
    has_unlapi = False
    has_gitlapi = False
    has_hulapi = False

    for unlapii in unlapi:
        if word.startswith(unlapi):
            has_unlapi = True

    for gitlapii in gitlapi:
        if gitlapii in word:
            has_gitlapi = True
        
    for hulapii in hulapi:
        if word.endswith(hulapi):
            has_hulapi = True
    
    return has_unlapi and has_gitlapi and has_hulapi

def contains_unlapi_hulapi(word):
    has_unlapi = False
    has_hulapi = False

    if unlapii in unlapi:
        if word.startswith(unlapi):
            has_hulapi = True
            break

    if hulapii in hulapi:
        if word.endswith(hulapi):
            has_hulapi = True
            break

    

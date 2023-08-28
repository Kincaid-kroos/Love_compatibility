def calculate_love_compatibility(name1,name2):
    combined_names = (name1 + name2).lower()
    letters = {}
    for letter in combined_names:
        letters[letter] = letters.get(letter, 0) +1
    compatibility = sum(letters.values())
    compatibility = min(compatibility,100)
    return compatibility
name1 = input("Enter boyfriends name: ")
name2 = input("Enter girlfriends name: ")
compatibility_score = calculate_love_compatibility(name1,name2)
print(compatibility_score)
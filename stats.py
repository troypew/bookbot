filepath = "books/frankenstein.txt"

character_count = {
    'a' : 0,
    'b' : 0,
    'c' : 0,
    'd' : 0,
    'e' : 0,
    'f' : 0,
    'g' : 0,
    'h' : 0,
    'i' : 0,
    'j' : 0,
    'k' : 0,
    'l' : 0,
    'm' : 0, 
    'n' : 0,
    'o' : 0,
    'p' : 0,
    'q' : 0,
    'r' : 0,
    's' : 0,
    't' : 0,
    'u' : 0,
    'v' : 0,
    'w' : 0,
    'x' : 0,
    'y' : 0,
    'z' : 0,
}


def total_word_count(filepath):
    with open(filepath) as f:
        filecontents = f.read()
        wordcount = 0
        for word in filecontents.split():
            wordcount += 1
        return wordcount
    
def character_count_calc(filepath):
    with open(filepath) as f:
        filecontents = f.read()
        for letters in filecontents:
            letter = letters.lower()
            if letter in character_count:
                character_count[letter] += 1
            else:
                character_count[letter] = 1
        return character_count

new_character_count = character_count_calc(filepath)

sorted_characters = []
#test_dict = character_count

def sort_on(sorted_characters):
         return sorted_characters["num"]

def sorted_chars(new_character_count):   
    sorted_characters = [] 
    #test_dict = character_count
    
    for char, num in character_count.items():
        num = character_count[char]
        if char.isalpha():
            sorted_characters.append({"char" : char, "num" : character_count[char]})
        else:
            pass
    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters

reformatted_character_count = sorted_chars(new_character_count)

# def sort_on():
#         return reformatted_character_count["num"]

#new_sorted_chars = reformatted_character_count.sort(reverse=True, key=sort_on)

def main(): 
    #print(f"Found {total_word_count(filepath)} total words")
    #print(character_count_calc(filepath))
    #print(sorted_chars(new_character_count))
    return (sorted_chars(new_character_count))

main()
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

#sorted_characters = []

def sorted_chars(character_count):   
    sorted_characters = [] 
    for char in character_count:
        if char.isalpha():
            sorted_characters = [{"char": char, "num": char[0]}]
        else:
            pass
    return sorted_characters.sort(reverse=True, char=sort_on)

    






def main(): 
    #print(f"Found {total_word_count(filepath)} total words")
    #print(character_count_calc(filepath))
    print(sorted_chars(character_count))

main()





#def sort_on(character_count):
#    return character_count[0]
#
#character_count.sort(key=sort_on)
#print(character_count)
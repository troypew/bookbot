filepath = "books/frankenstein.txt"
from stats import total_word_count
from stats import character_count_calc

def get_book_text(filepath):
    try:
        with open(filepath) as f:
            filecontents = f.read()
        return filecontents
    except Exception as e:
        print(e)




def main(): 
    #print(get_book_text(filepath))
    #print(f"Found {total_word_count(filepath)} total words")
    print(
        "============ BOOKBOT ============
        Analyzing book found at books/frankenstein.txt...
        ----------- Word Count ----------"
        )
    print(f"Found {character_count_calc} total words")
    for 


main()


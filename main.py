filepath = "books/frankenstein.txt"
from stats import total_word_count
from stats import sorted_chars
from stats import reformatted_character_count
from stats import new_character_count

# def get_book_text(filepath):
#     try:
#         with open(filepath) as f:
#             filecontents = f.read()
#         return filecontents
#     except Exception as e:
#         print(e)

reformatted_character_count = sorted_chars(new_character_count)


def main(): 
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {total_word_count(filepath)} total words")
    print("--------- Character Count -------")
    for entry in reformatted_character_count:
        character = entry["char"]
        if character.isalpha():
            print(f"{character}: {entry['num']}")
    print("============= END ===============")


main()
import sys
from stats import total_word_count
from stats import sorted_chars
from stats import reformatted_character_count
from stats import new_character_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

reformatted_character_count = sorted_chars(new_character_count)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {total_word_count(filepath)} total words")
    print("--------- Character Count -------")
    for entry in reformatted_character_count:
        character = entry["char"]
        if character.isalpha():
            print(f"{character}: {entry['num']}")
    print("============= END ===============")


main()
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
from stats import get_book_text, word_count, char_count, sorted_char_list
text = get_book_text(sys.argv[1])

num_words = word_count(text)
counts = char_count(text)

sorted_chars = sorted_char_list(counts)


print(f"============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print(f"----------- Word Count ----------")
print(f"Found {num_words} total words")
print(f"--------- Character Count -------")

for entry in sorted_chars:
    ch = entry["char"]
    n = entry["num"]
    print(f"{ch}: {n}")
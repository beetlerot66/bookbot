def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

def char_count(text):
    chars = {}
    for char in text:
        char = char.lower()
        if char in chars:
            chars[char] = chars[char] + 1
        else:
            chars[char] = 1
    return chars

def helper(entry):
    return entry["num"]

def sorted_char_list(counts):
    result = []
    for char, num_chars in counts.items():
        if not char.isalpha():
            continue
        result.append({"char": char, "num": num_chars})
    result.sort(reverse=True, key=helper)
    return result
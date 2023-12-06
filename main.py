def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_words = word_count(text)
    print(f"{number_words} words found in the document")
    letter_dict = letter_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(letter_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{number_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    count = len(words)
    return count

def letter_count(text):
    letters = {}
    for i in text:
        lowered = i.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    return letters

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]

main()
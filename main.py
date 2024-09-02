
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_characters(text):
    h = {}
    for i in text:
        lowercase_string = i.lower()
        for j in lowercase_string:
            if(j.isalpha()):
                h[j] = h.get(j, 0) + 1
    
    h = dict(sorted(h.items()))
    return h

def report(list):
    for i, j in list.items():
        print(f"The character '{i}' was found {j} times")
def get_num_words(text):

    words = text.split()
    return len(words)

def main():
    book_path = "./frankenstein.txt"
    text = get_book_text(book_path)
    get_num_words(text)
    print("--- Begin report of",book_path, "---")
    print(get_num_words(text), "words found in the document\n")
    report(count_characters(text))
    print("--- End report ---")
main()
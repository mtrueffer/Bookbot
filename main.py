def main():
    book_file = "books/frankenstein.txt"
    book_contents = None
    word_count = 0
    char_counts = {}
    char_list = []
    
    book_contents = getBook(book_file)

    word_count = wordCount(book_contents)

    char_counts = characterCount(book_contents)

    char_list = dict2dictlist(char_counts)
    char_list.sort(reverse=True, key=sortOn)
    
    print(f"--- Begin report of {book_file} ---")
    print(f"{word_count} words found in the document")
    print(" ")
    for i in range(0,len(char_list)):
        if char_list[i]["letter"].isalpha():
            print(f"The '{char_list[i]["letter"]}' character was found {char_list[i]["count"]} times")
    print("--- End report ---")

def getBook(book):
    with open(book) as f:
        return f.read()

def wordCount(text):
    words = text.split()
    return len(words)

def characterCount(text):
    text_chars = {}
    low_text = text.lower()
    for c in low_text:
        if c in text_chars:
            text_chars[c] += 1
        else:
            text_chars[c] = 1
    return text_chars

def dict2dictlist(dict):
    list = []
    for d in dict:
        tmp_dict = {}
        tmp_dict["letter"] = d
        tmp_dict["count"] = dict[d]
        list.append(tmp_dict)
    return list

def sortOn(dict):
    return dict["count"]

main()
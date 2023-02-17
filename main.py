import sys
import string

def count_letter(file):
    chars = list(string.ascii_lowercase)
    aux = [0 for x in range(26)]
    letters = dict(zip(chars,aux))
    file=file.lower()

    for i in file:
        try:
            letters[i] += 1
        except:
            pass

    return letters

def word_count(file):
    words = file.split()
    return len(words)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 main.py path/to/the/book")
        sys.exit()

    path = sys.argv[1]

    with open(path,'r') as f:
        file_content=f.read()


    count_letter(file_content)

    print(f"--- Begin Report of {path} ---")
    print(f"{word_count(file_content)} words find in the document\n\n")
    letters=count_letter(file_content)
    #keys= 
    for letter in letters.keys():
        print(f"The '{letter}' character was found {letters[letter]} times")

    print("--- End Report ---")



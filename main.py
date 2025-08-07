
#Funktion to grap a text and mak it to a string: gives string back
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
#main Funktion to give a count of words in a book
def main():
    booktxt = get_book_text("./books/frankenstein.txt")
    num_words = count_book_words(booktxt)
    txt = f"{num_words} words found in the document"
    print(txt)
    return 0
# funktion to count the words form the string
def count_book_words(booktext):
    nummber = len(booktext.split())
    return nummber

main()


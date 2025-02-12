print("deneme")
def add_book(library, title, author, year):
    library[title] = {"author": author, "year": year}

if remove_book(library, title):
    if title in library:
        del library[title]

def get_author(library, title):
    if title in library:
        return library[title]["author"]
    else:
        return "Kitapbulunamadi"

book_library = {}
add_book(book_library, "PythonCrashCourse", "EricMatthes", 2019)
add_book(book_library, "DeepLearning", "IanGoodfellow", 2016)
remove_book(book_library, "DeepLearning")
author = get_author(book_library, "PythonCrashCourse")
print("deneme")
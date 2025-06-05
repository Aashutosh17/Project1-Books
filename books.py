from fastapi import FastAPI, HTTPException, Body

app = FastAPI()

Books= [
    { "Title" : "Title One", "Author" : "Author One", "Category" : "Science"},
    { "Title" : "Title Two", "Author" : "Author Two", "Category" : "Math"},
    { "Title" : "Title Three", "Author" : "Author Two", "Category" : "Social"},
    { "Title" : "Title Two", "Author" : "Author Four", "Category" : "Math"},
    { "Title" : "Title Five", "Author" : "Author One", "Category" : "General Knowledge"}
]

# Route 1: Get all books
@app.get("/books")
async def read_all_books():
    return Books

# Route 2: Get a book by title
@app.get("/books/{book_title}/")
async def read_book(book_title: str):
    for book in Books:
        if book.get('Title').casefold() == book_title.casefold():
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Route 3: Get books by category using query parameter
@app.get("/books/by-category")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in Books:
        if book.get('Category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

#Get books by Author and Category
@app.get("/books/by-author/{author}")
async def read_author_category_query(author : str, category : str):
    books_to_return =[]
    for book in Books:
        if book.get('Author').casefold() == author.casefold() and \
            book.get('Category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


# Post request method Create a new book
@app.post("/books")
async def create_book(new_book =Body()):
      Books.append(new_book)

# Put request Method
@app.put("/books")
async def update_book(updated_book = Body()):
   for i in range(len(Books)):
       if Books[i].get("Title").casefold() == updated_book.get("Title").casefold():
           Books[i] = updated_book

# Delete request method
@app.delete("/book/{book_title}")
async def delete_book(book_title:str):
    for i in range(len(Books)):
        if Books[i].get("Title").casefold() == book_title.casefold():
            Books.pop(i)
            break


"""@app.delete("/book/{book_title}")
async def delete_all_books(book_title: str):
    for i in range(len(Books) - 1, -1, -1):  # loop backwards
        if Books[i].get("Title").casefold() == book_title.casefold():
            Books.pop(i)
    return {"message": f"All books titled '{book_title}' deleted."}"""

@app.get("/books/byauthor/{author}/")
async def fetch_All_Books(author : str):
    fetch_all_books =[]
    for book in Books:
        if book.get('Author').casefold() == author.casefold():
           fetch_all_books.append(book)

    return fetch_all_books
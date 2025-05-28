from fastapi import FastAPI, HTTPException

app = FastAPI()

Books = [
    { "Title" : "Title One", "Author" : "Author One", "Category" : "Science"},
    { "Title" : "Title Two", "Author" : "Author Two", "Category" : "Math"},
    { "Title" : "Title Three", "Author" : "Author Three", "Category" : "Social"},
    { "Title" : "Title Two", "Author" : "Author Four", "Category" : "Math"},
    { "Title" : "Title Five", "Author" : "Author Five", "Category" : "General Knowledge"}
]

@app.get("/books")
async  def read_all_books():
    return Books

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in Books:
        if book.get('Title').casefold() == book_title.casefold():
            return book

    raise HTTPException(status_code=404, detail="Book not found")



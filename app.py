from fastapi import Body,FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "year": 2001, "category": "horror"},
    {"title": "Title Two", "author": "Author Two", "year": 2002, "category": "math"},
    {"title": "Title Three", "author": "Author Three", "year": 2003, "category": "something"},
]

@app.get("/books")
async def first_api():
    return BOOKS

@app.get("/books/{dynamic_param}")
async def read_all_books(dynamic_param: str):
    return {'dynamic_param': dynamic_param}


@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
    return {"error": "Book not found"}


@app.get("/books/category/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book/")
async def create_book(new_book= Body()):
    BOOKS.append(new_book)
    return new_book

@app.put("/books/update_book/")
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title = str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
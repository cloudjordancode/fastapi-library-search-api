# exercises/library-search/app/routers/books.py
# L4 — Library Search endpoints

# TODO: Import APIRouter, Query, HTTPException from fastapi
from fastapi import APIRouter, Query, Path, HTTPException

# TODO: Import your schemas
from app.schemas.book import Book, SortField
from typing import Optional

router = APIRouter()

# Sample in-memory library — 10+ books across multiple genres
# TODO: Add at least 10 book dicts (id, title, author, genre, rating, year, available)
BOOKS: list[dict] = [
    {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "rating": 4.8,
        "year": 1949,
        "available": True
    },
        {
        "id": 2,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "rating": 4.9,
        "year": 1937,
        "available": True
    },
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic",
        "rating": 4.3,
        "year": 1925,
        "available": False
    },
    {
        "id": 4,
        "title": "Dune",
        "author": "Frank Herbert",
        "genre": "Science Fiction",
        "rating": 4.8,
        "year": 1965,
        "available": True
    },
    {
        "id": 5,
        "title": "Animal Farm",
        "author": "George Orwell",
        "genre": "Dystopian",
        "rating": 4.6,
        "year": 1945,
        "available": True
    },
    {
        "id": 6,
        "title": "The Shining",
        "author": "Stephen King",
        "genre": "Horror",
        "rating": 4.7,
        "year": 1977,
        "available": False
    },
    {
        "id": 7,
        "title": "The Fellowship of the Ring",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "rating": 4.9,
        "year": 1954,
        "available": True
    },
    {
        "id": 8,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "rating": 4.5,
        "year": 1813,
        "available": True
    },
    {
        "id": 9,
        "title": "The Martian",
        "author": "Andy Weir",
        "genre": "Science Fiction",
        "rating": 4.7,
        "year": 2011,
        "available": False
    },
    {
        "id": 10,
        "title": "It",
        "author": "Stephen King",
        "genre": "Horror",
        "rating": 4.5,
        "year": 1986,
        "available": True
    }
]

# TODO: Implement GET /books/{book_id} — return a single book or 404
# This is a PATH parameter because the book_id uniquely identifies the resource.

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int = Path(gt=0, description="THe ID of the book.")):
    """
    Returns a single book by ID.
    TODO: Find the book in BOOKS, raise 404 if not found.
    """
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail=f"Book {book_id} not found.")


# TODO: Implement GET /books?genre=fiction&min_rating=4.0&sort_by=title&limit=10
# All query parameters are optional (have defaults)
# Use Query() with ge/le constraints for min_rating
# Use Query() with ge=1, le=100 for limit

@router.get("/", response_model=list[Book])
def search_books(
    genre: Optional[str] = Query(None, description="Filter by genre"),
    min_rating: float = Query(0.0, ge=0.0, le=5.0, description="Minimum rating"),
    sort_by: SortField = Query(SortField.title, description="Sort field"),
    limit: int = Query(10, ge=1, le=100, description="Max results to return"),
):
    """
    Searches and filters books.

    TODO:
    1. Filter BOOKS by genre if provided (case-insensitive)
    2. Filter by min_rating
    3. Sort the results by sort_by field
    4. Return up to limit results
    """
    results = BOOKS.copy()

    if genre:
        results = [book for book in results if book["genre"].strip().lower() == genre.strip().lower()] 
    results = [book for book in results if min_rating <= book["rating"]]

    results.sort(key=lambda book: book[sort_by.value])
    results = results[:limit]
    return results 


# TODO: Implement GET /authors/{author_id}/books
# Return all books by a given author (use author_id as an index into a small
# hardcoded author list, or just treat it as a name lookup)

AUTHORS = {
    1: "George Orwell",
    2: "J.K. Rowling",
    3: "Stephen King"
}


@router.get("/authors/{author_id}/books", response_model=list[Book])
def get_books_by_author(
    author_id: int,
    sort_by: SortField = SortField.title
    ):

    """
    Returns all books by the specified author.

    TODO: Filter BOOKS where the author matches the author at author_id.
    You can keep a small list: AUTHORS = {1: "George Orwell", 2: ...}
    """

    author_name = AUTHORS.get(author_id)

    if not author_name:
        raise HTTPException(
            status_code=404, 
            detail="Author not found."
        )
    results = [book for book in BOOKS if book["author"] == author_name]

    results.sort(key=lambda book: book[sort_by.value])
    return results 





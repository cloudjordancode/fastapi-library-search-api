# exercises/library-search/app/schemas/book.py
# L4 — Library Search — Book schema and sort enum

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


# TODO: Define a SortField Enum with at least these values:
#   title, author, rating, year
# This restricts what values are accepted for the sort_by query parameter.
class SortField(str, Enum):
    title = "title"
    author = "author"
    rating = "rating"
    year = "year"
    


# TODO: Define a Book schema with fields:
#   id (int), title (str), author (str), genre (str),
#   rating (float, 0–5), year (int), available (bool)

class Book(BaseModel):
    """Represents a book in the library catalog."""
    id: int
    title: str
    author: str
    genre: str
    rating: float = Field(ge=0.0, le=5.0)
    year: int
    available: bool = False

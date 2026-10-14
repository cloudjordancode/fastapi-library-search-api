# exercises/library-search/app/main.py
# L4 — Library Search API
#
# Run with: uvicorn app.main:app --reload  (from library-search/ folder)

from fastapi import FastAPI
from app.routers import books

# TODO: Import the books router and include it

app = FastAPI(title="Library Search API")
app.include_router(
    books.router,
    prefix="/books",
    tags=["books"]
)

# TODO: Include the books router with prefix="/books" and tags=["books"]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine
from models import Base, Book, Reservation
from datetime import datetime, timedelta

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

# Expiry
def clear_expired(db):
    now = datetime.utcnow()
    expired = db.query(Reservation).filter(Reservation.expires_at < now).all()
    for r in expired:
        book = db.query(Book).filter(Book.id == r.book_id).first()
        if book:
            book.available_copies += 1
        db.delete(r)
    db.commit()

@app.get("/")
def root():
    return {"message": "API running"}

@app.post("/books/")
def add_book(title: str, author: str, copies: int):
    db = SessionLocal()
    book = Book(title=title, author=author,
                total_copies=copies, available_copies=copies)
    db.add(book)
    db.commit()
    db.refresh(book)
    db.close()
    return book

@app.get("/books/")
def get_books():
    db = SessionLocal()
    clear_expired(db)
    books = db.query(Book).all()
    db.close()
    return books

@app.post("/books/{book_id}/reserve")
def reserve(book_id: int, user_name: str):
    db = SessionLocal()
    clear_expired(db)

    book = db.query(Book).filter(Book.id == book_id).first()
    if not book or book.available_copies <= 0:
        raise HTTPException(status_code=400)

    book.available_copies -= 1

    r = Reservation(
        book_id=book_id,
        user_name=user_name,
        expires_at=datetime.utcnow() + timedelta(days=7)
    )

    db.add(r)
    db.commit()
    db.refresh(r)
    db.close()
    return r

@app.delete("/reservations/{rid}")
def cancel(rid: int):
    db = SessionLocal()
    r = db.query(Reservation).filter(Reservation.id == rid).first()

    if not r:
        raise HTTPException(status_code=404)

    book = db.query(Book).filter(Book.id == r.book_id).first()
    if book:
        book.available_copies += 1

    db.delete(r)
    db.commit()
    db.close()

    return {"message": "Cancelled"}
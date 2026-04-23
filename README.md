# Library Book Reservation System

## 📌 Description
This project is a backend system built using FastAPI and SQLite to manage book reservations.

## 🚀 Features
- Add books
- View all books
- Get book by ID
- Reserve books
- Cancel reservations
- Automatic expiry of reservations (7 days)

## 🛠 Technologies Used
- Python
- FastAPI
- SQLite
- SQLAlchemy

## ▶ How to Run

### Step 1:
Run setup script:
setupdev.bat

### Step 2:
Run application:
runapplication.bat

### Step 3:
Open browser:
http://localhost:9000/docs

## 📖 API Endpoints
- GET /books/
- GET /books/{id}
- POST /books/
- POST /books/{id}/reserve
- DELETE /reservations/{id}
## 📂 Project Structure

```
LibrarySystem/
│
├── backend/
│   ├── main.py                 # FastAPI application entry point
│   ├── database.py             # Database connection setup
│   ├── models.py               # SQLAlchemy models
│   ├── alembic/                # Database migration folder
│   ├── alembic.ini             # Alembic configuration
│   ├── library.db              # SQLite database file
│   ├── openapi.json            # API specification
│   ├── test_main.py            # Backend test cases
│   ├── runapplication.bat      # Script to run backend
│   ├── setupdev.bat            # Setup environment script
│   └── __pycache__/            # Python cache files
│
├── env/                        # Python virtual environment (NOT pushed to GitHub)
│
├── library_sdk/               # Auto-generated TypeScript SDK (OpenAPI)
│   ├── api/
│   ├── models/
│   ├── runtime/
│   └── index.ts
│
├── frontend/ (if exists)
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js / webpack config
│
├── node_modules/              # Node dependencies (NOT pushed to GitHub)
├── package.json               # Node project config (if SDK/frontend used)
├── package-lock.json
│
└── README.md                  # Project documentation
```

## 👩‍💻 Author
Monisha E MSc Data Science Student

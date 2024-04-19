import os

#  URI we use to talk to postgres
db_URI = os.getenv("DATABASE_URL", "postgresql://localhost:5432/conservation_db")
# Secret for JWT
SECRET = os.getenv("SECRET", "duckmariotinalego")

if db_URI.startswith("postgres://"):
    db_URI = db_URI.replace("postgres://", "postgresql://", 1)

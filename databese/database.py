from sqlmodel import SQLModel, Field, create_engine

DB_FILE = 'db.sqlite3'
engine = create_engine(f"sqlite:///{DB_FILE}", echo=True)
SQLModel.metadata.create_all(engine)
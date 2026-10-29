# not database independent yet
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///mydatabase.db", echo=True)

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE IF NOT EXISTS people (name TEXT, age INTEGER)"))
    conn.execute(text("INSERT INTO people (name, age) VALUES (:name, :age)"),
                 {"name": "Mihir", "age": 25})
    conn.commit()

    result = conn.execute(text("SELECT * FROM people"))
    for row in result:
        print(row)

from sqlalchemy.orm import Session

with Session(engine) as session:
    session.execute(text("insert into people values (:name, :age)"), {"name":"Vraj", "age":30})
    session.commit()
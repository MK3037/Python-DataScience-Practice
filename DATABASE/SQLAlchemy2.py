from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine

engine = create_engine("sqlite:///mydatabase.db", echo=True)
meta = MetaData()

people = Table(
    "people",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("age", Integer),
)
# Create the table in the database
meta.create_all(engine)

with engine.connect() as conn:

  # --- 1. Insert a single row ---
  stmt = people.insert().values(name="Mihir", age=25)
  conn.execute(stmt)
  conn.commit()

  # --- 2. Bulk insert multiple rows using a list of dictionaries ---
  stmt_bulk = people.insert()
  conn.execute(stmt_bulk, [{"name": "Jenil", "age": 30}, {"name": "Vraj", "age": 28}])
  conn.commit()

  # --- 3. DELETE a record ---
  stmt_delete = people.delete().where(people.c.name == "Vraj")
  conn.execute(stmt_delete)
  conn.commit()

  # --- 4. Update a record ---
  stmt_update = people.update().where(people.c.name=="Jenil").values(age="29")
  conn.execute(stmt_update)
  conn.commit()

  # --- 5. Select and print remaining records ---
  print("\n--- Records after deletion ---")
  result = conn.execute(people.select())
  for row in result:
    print(row)
# MetaData holds blueprints (Structure, not data)
#Session holds data changes (Inserts, updates, deletions)
from sqlalchemy import Column, Integer, MetaData, String, Float, Table, create_engine,ForeignKey, select,func

engine = create_engine("sqlite:///Foreign.db", echo=True)
meta = MetaData()

people = Table(
    "people",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("age", Integer),
)

things = Table(
    "things",
    meta,
    Column("id", Integer, primary_key=True),
    Column("description", String),
    Column('value', Float),
    Column('owner', Integer, ForeignKey("people.id")),
)

meta.create_all(engine)
conn=engine.connect()

insert_people = people.insert().values([
    {'name': 'Mike', 'age': 30},
    {'name': 'Bob', 'age': 35},
    {'name': 'Anna', 'age': 38},
    {'name': 'John', 'age': 50},
    {'name': 'Clara', 'age': 42}
])

insert_things = things.insert().values([
    {'owner': 2, 'description': 'Laptop', 'value': 800.50},
    {'owner': 2, 'description': 'Mouse', 'value': 50},
    {'owner': 2, 'description': 'Keyboard', 'value': 100},
    {'owner': 3, 'description': 'Book', 'value': 30},
    {'owner': 4, 'description': 'Bootle', 'value': 10.50},
    {'owner': 5, 'description': 'Speakers', 'value': 80},
])

conn.execute(insert_people)
conn.commit()
conn.execute(insert_things)
conn.commit()

join_statement = people.join(things, people.c.id == things.c.owner)
select_statement = select(people.c.name, things.c.description).select_from(join_statement)
result = conn.execute(select_statement)
for row in result.fetchall():
    print(row)

group_by = things.select().with_only_columns(things.c.owner, func.sum(things.c.value)).group_by(things.c.owner).having(func.sum(things.c.value)>50)
result=conn.execute(group_by)
for row in result.fetchall():
    print(row)
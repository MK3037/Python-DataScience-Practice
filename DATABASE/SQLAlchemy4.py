from sqlalchemy import Integer,String,Float,Column, create_engine, ForeignKey,func
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship

engine = create_engine("sqlite:///Foreign.db", echo=True)

class Base(DeclarativeBase):
    pass

class Person(Base):
    __tablename__='people'
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    age=Column(Integer)

    things=relationship('Thing',back_populates='person')

class Thing(Base):
    __tablename__='things'
    id=Column(Integer,primary_key=True)
    description=Column(String,nullable=False)
    value=Column(Float)
    owner=Column(Integer,ForeignKey('people.id'))

    person=relationship('Person', back_populates='things')

Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()

new_person=Person(name='Nobody', age=100)
session.add(new_person)
session.flush()

new_thing=Thing(description='Camera', value=500, owner=new_person.id)
session.add(new_thing)

session.commit()

print([t.description for t in new_person.things])

result=session.query(Person).filter(Person.age>40).all()
print([p.name for p in result])

result=session.query(Thing).filter(Thing.value<50).delete()
session.commit()
result=session.query(Thing).filter(Thing.value>50).all()
print([t.description for t in result])

result=session.query(Person.name, Thing.description).join(Thing).all()
print(result)

result=session.query(Thing.owner, func.sum(Thing.value)).group_by(Thing.owner).all()
print(result)

session.close




# Modern SQLAlchemy 2.0 Shortcut
# In SQLAlchemy 2.0, you can even skip sessionmaker for quick scripts and instantiate Session directly by passing the engine:

# Python
# from sqlalchemy.orm import Session

# # You can pass the engine straight to Session()
# with Session(engine) as session:
#   person = session.get(Person, 1)
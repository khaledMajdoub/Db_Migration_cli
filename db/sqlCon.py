from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate


engine = create_engine('sqlite:///db_dummy_test_sqlite', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name='Ridha', age=30)
session.add(new_user)
session.commit()

user_query = session.query(User).filter_by(name='Ridha').first()
print(user_query.name, user_query.age)

headers = ["ID", "Name", "Age"]
data = [(user_query.id, user_query.name, user_query.age)]

print(tabulate(data, headers=headers, tablefmt="grid"))

session.close()

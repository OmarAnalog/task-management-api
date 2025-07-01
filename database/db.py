from sqlmodel import SQLModel,create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine('sqlite:///database.db',echo=True)

def create_tables():
    SQLModel.metadata.create_all(engine)


def getsession():
    with sessionmaker(engine)() as session:
        yield session
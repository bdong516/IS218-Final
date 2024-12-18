from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Define a simple User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

# Database setup
engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)

# Session setup
Session = sessionmaker(bind=engine)
session = Session()

# Example seed data
def seed_users():
    if not session.query(User).first():
        user1 = User(name="John Doe", email="john@example.com")
        user2 = User(name="Jane Doe", email="jane@example.com")
        session.add_all([user1, user2])
        session.commit()
        print("Users seeded!")

if __name__ == "__main__":
    seed_users()

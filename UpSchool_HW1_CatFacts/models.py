from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class CatFact(Base):
    __tablename__ = 'cat_facts'

    id = Column(String, primary_key=True)
    text = Column(String)
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    type = Column(String)

    def __repr__(self):
        return f"<CatFact(id='{self.id}', text='{self.text[:30]}...', type='{self.type}')>"


engine = create_engine('sqlite:///cat_facts.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

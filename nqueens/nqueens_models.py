from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class QueenMoveNode(Base):
    __tablename__ = 'queen_move_nodes'

    id = Column(Integer, primary_key=True)
    move_number = Column(Integer, nullable=False)
    board = Column(String, nullable=False)  

    def __repr__(self):
        return f"<QueenMoveNode(id={self.id}, move_number={self.move_number}, board='{self.board}')>"

engine = create_engine('sqlite:///nqueens_moves.db', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

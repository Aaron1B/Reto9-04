from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class KnightMoveNode(Base):
    __tablename__ = 'knight_move_nodes'

    id = Column(Integer, primary_key=True)
    from_x = Column(Integer, nullable=False)
    from_y = Column(Integer, nullable=False)
    move_number = Column(Integer, nullable=False)
    to_x = Column(Integer, nullable=True)
    to_y = Column(Integer, nullable=True)
    possibilities = Column(Integer, nullable=False)
    next_node_id = Column(Integer, nullable=True)

    def __repr__(self):
        return f"<KnightMoveNode(id={self.id}, from=({self.from_x},{self.from_y}), move_number={self.move_number}, possibilities={self.possibilities})>"

# Configuración de la base de datos SQLite
engine = create_engine('sqlite:///knight_moves.db')

# Crear la base de datos y las tablas
Base.metadata.create_all(engine)

# Crear la sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

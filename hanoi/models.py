from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class HanoiMoveNode(Base):
    __tablename__ = 'hanoi_move_nodes'

    id = Column(Integer, primary_key=True)
    from_peg = Column(String, nullable=False)
    to_peg = Column(String, nullable=False)
    move_number = Column(Integer, nullable=False)
    next_node_id = Column(Integer, nullable=True)

    def __repr__(self):
        return f"<HanoiMoveNode(id={self.id}, from_peg='{self.from_peg}', to_peg='{self.to_peg}', move_number={self.move_number})>"

# Configuración de la base de datos SQLite (puedes usar otra base de datos si lo prefieres)
engine = create_engine('sqlite:///hanoi_moves.db')

# Crear la base de datos y las tablas
Base.metadata.create_all(engine)

# Crear la sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

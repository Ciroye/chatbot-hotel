from sqlalchemy import Column, Integer, String

import db


class Room(db.Base):
    __tablename__ = 'Room'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __repr__(self):
        return f'Room({self.name}, {self.capacity})'

    def __str__(self):
        return self.name

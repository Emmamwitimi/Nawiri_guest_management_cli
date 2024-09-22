from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

engine = create_engine('sqlite:///migrations_test.db')

Base = declarative_base()

class Guest(Base):
    __tablename__ = 'guests'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)


class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    number = Column(String, nullable=False)
    type = Column(String, nullable=False)
    available = Column(Integer, default=1)


class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    guest_id = Column(Integer, ForeignKey('guests.id'))
    room_id = Column(Integer, ForeignKey('rooms.id'))
    check_in = Column(DateTime, nullable=False)
    check_out = Column(DateTime, nullable=False)
    guest = relationship("Guest")
    room = relationship("Room")
# Create the engine and tables
engine = create_engine('sqlite:///nawiri.db')
Base.metadata.create_all(engine)
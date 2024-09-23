import click
import random
from faker import Faker  
from models import Guest, Booking, Room
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime,timedelta

engine = create_engine('sqlite:///nawiri.db')
Session = sessionmaker(bind=engine)

fake = Faker()

@click.group()
def cli():
    """Nawiri Guest Management CLI"""
    pass

@cli.command()
def add_guest():
    """Add a new guest."""
    name = click.prompt('Guest name')
    email = click.prompt('Guest email')
    phone = click.prompt('Guest phone')
    session = Session()
    new_guest = Guest(name=name, email=email, phone=phone)
    session.add(new_guest)
    session.commit()
    click.echo(f"Added guest {name}.")
    session.close()

@cli.command()
def view_guests():
    """View all guests."""
    session = Session()
    guests = session.query(Guest).all()
    for guest in guests:
        click.echo(f"{guest.id}: {guest.name}, {guest.email}")
    

@cli.command()
def add_room():
    """Add a new room."""
    number = click.prompt('Room number')
    room_type = click.prompt('Room type')
    session = Session()
    new_room = Room(number=number, type=room_type)
    session.add(new_room)
    session.commit()
    click.echo(f"Added room {number}.")
    session.close()

@cli.command()
def view_rooms():
    """View all rooms."""
    session = Session()
    rooms = session.query(Room).all()
    for room in rooms:
        status = "Available" if room.available else "Occupied"
        click.echo(f"Room {room.number}: {room.type} - {status}")
    session.close()

@cli.command()
def make_booking():
    """Create a new booking."""
    session = Session()
    guest_id = click.prompt("Guest ID", type=int)
    room_id = click.prompt("Room ID", type=int)

    # Error handling for check-in date
    while True:
        check_in = click.prompt('Check-in date (DD/MM/YY)')
        try:
            check_in_date = datetime.strptime(check_in, '%d/%m/%y')
            break
        except ValueError:
            click.echo("Invalid date format! Please use DD/MM/YY (e.g., 12/10/24).")

    # Error handling for check-out date
    while True:
        check_out = click.prompt('Check-out date (DD/MM/YY)')
        try:
            check_out_date = datetime.strptime(check_out, '%d/%m/%y')
            break
        except ValueError:
            click.echo("Invalid date format! Please use DD/MM/YY (e.g., 12/10/24).")

    room = session.query(Room).get(room_id)
    if room.available == 1:
        new_booking = Booking(
            guest_id=guest_id,
            room_id=room_id,
            check_in=check_in_date,
            check_out=check_out_date
        )
        room.available = 0
        session.add(new_booking)
        session.commit()
        click.echo(f"Booking successful for Guest ID: {guest_id}, Room ID: {room_id}.")
    else:
        click.echo("Room is not available.")

    session.close()

@cli.command()
def seed_data():
    """Seed the database with a custom number of guests, rooms, and bookings."""
    session = Session()

    # Prompt for the number of records
    num_guests = click.prompt("How many guests do you want to seed?", type=int, default=10)
    num_rooms = click.prompt("How many rooms do you want to seed?", type=int, default=20)
    num_bookings = click.prompt("How many bookings do you want to seed?", type=int, default=5)

    # Seed guests
    guests = []
    for _ in range(num_guests):
        guest = Guest(
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number()
        )
        guests.append(guest)

    # Seed rooms
    rooms = []
    room_types = ["Single", "Double", "Suite", "Deluxe"]
    for i in range(num_rooms):
        room = Room(
            number=f"{100 + i}",  # Room numbers 100, 101, ..., 100+num_rooms
            type=random.choice(room_types)
        )
        rooms.append(room)

    # Add seeded guests and rooms to the session
    session.add_all(guests)
    session.add_all(rooms)
    session.commit()

    # Seed bookings with random dates, guest and room associations
    bookings = []
    guest_ids = [guest.id for guest in session.query(Guest).all()]
    room_ids = [room.id for room in session.query(Room).filter_by(available=1).all()]

    for _ in range(num_bookings):
        guest_id = random.choice(guest_ids)
        room_id = random.choice(room_ids)

        # Random check-in and check-out dates
        check_in_date = datetime.now() + timedelta(days=random.randint(1, 30))
        check_out_date = check_in_date + timedelta(days=random.randint(1, 5))

        booking = Booking(
            guest_id=guest_id,
            room_id=room_id,
            check_in=check_in_date,
            check_out=check_out_date
        )
        bookings.append(booking)

        # Mark room as booked
        room = session.query(Room).get(room_id)
        room.available = 0

    # Add bookings to the session
    session.add_all(bookings)
    session.commit()

    click.echo(f"Seeded {num_guests} guests, {num_rooms} rooms, and {num_bookings} bookings.")
    session.close()


if __name__ == '__main__':
    cli()

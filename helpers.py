import click
from models import Guest, Booking, Room
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///nawiri.db')
Session = sessionmaker(bind=engine)

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

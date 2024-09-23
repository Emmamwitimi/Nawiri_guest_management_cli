# Nawiri Guest Management CLI

## Overview

Nawiri Guest Management CLI is a command-line interface application built to manage guest information for a hotel or guest house. It uses Python, SQLAlchemy for database interaction, and Click for building command-line tools. The project supports features like adding new guests and viewing guest lists.

## Features

- Add new guest information (name, email, phone number).
- View all guest information in the database.

## Project Structure

Nawiri_guest_management_cli/ │ ├── nawiri/ │ ├── init.py │ ├── models.py # SQLAlchemy models for Guest, Booking, and Room. │ ├── cli.py # Main CLI logic using Click. │ ├── helpers.py # Functions to add and view guests. │ ├── migrations/ # Alembic migration files │ └── env.py │ ├── alembic.ini # Alembic configuration file. └── README.md # Project documentation.


## Getting Started

### Prerequisites

To run this project, you need the following tools installed on your local machine:

- Python 3.8+
- Virtualenv or `venv` for Python environment management
- SQLite (or any SQLAlchemy-supported database)
- Alembic for database migrations

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Nawiri_guest_management_cli.git
   cd Nawiri_guest_management_cli

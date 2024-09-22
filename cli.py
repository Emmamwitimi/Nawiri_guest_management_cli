from helpers import add_guest, view_guests, add_room, view_rooms, make_booking, seed_data

def main():
    while True:
        menu()
        choice = input("> ")

        if choice == "0":
            add_guest()
        elif choice == "1":
            view_guests()
        elif choice == "2":
            add_room()
        elif choice == "3":
            view_rooms()
        elif choice == "4":
            make_booking()
        elif choice == "5":
            seed_data()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def menu():
    print("\nPlease select an option:")
    print("0. Add a guest")
    print("1. View all guests")
    print("2. Add a room")
    print("3. View all rooms")
    print("4. Make a booking")
    print("5. Seed the database with sample data")
    print("6. Exit")

if __name__ == "__main__":
    main()

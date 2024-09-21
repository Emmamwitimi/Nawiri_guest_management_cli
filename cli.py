from helpers import (
    add_guest,
    view_guests
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            add_guest()
        elif choice == "1":
            view_guests()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. add a guest")
    print("1. view all the guests")


if __name__ == "__main__":
    main()
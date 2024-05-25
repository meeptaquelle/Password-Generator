import random
import string


def simple_password_generator(observers):
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    notify_observers(observers, password)
    return password, observers


def strong_password_generator(observers):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(12))
    notify_observers(observers, password)
    return password, observers


def numeric_password_generator(observers):
    password = ''.join(random.choices(string.digits, k=8))
    notify_observers(observers, password)
    return password, observers


def alphabetic_password_generator(observers):
    password = ''.join(random.choices(string.ascii_letters, k=8))
    notify_observers(observers, password)
    return password, observers

def create_generator(strategy):
    strategies = {
        "1": simple_password_generator,
        "2": strong_password_generator,
        "3": numeric_password_generator,
        "4": alphabetic_password_generator
    }
    return strategies.get(strategy)

def notify_observers(observers, password):
    for observer in observers:
        observer(password)

def print_observer(password):
    print(f"New password generated: {password}")


def main():
    observers = [print_observer]

    print("Password Generator")
    print("==================")

    while True:
        print("\nMenu:")
        print("1. Generate Simple Password")
        print("2. Generate Strong Password")
        print("3. Generate Numeric Password")
        print("4. Generate Alphabetic Password")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice in ["1", "2", "3", "4"]:
            password_func = create_generator(choice)
            password, observers = password_func(observers)
        elif choice == "5":
            print("Exiting program")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

from colors import (
    RESET,
    GREEN,
    YELLOW,
    BLUE,
    MAGENTA,
    CYAN,
    BOLD
)

from inventory import (
    add_resource,
    list_resources,
    search_resources,
    filter_by_category
)

from lending import borrow_resource, return_resource

from reports import generate_report

from data import fellows


def get_positive_integer(prompt):
    while True:
        value = input(prompt)

        try:
            value = int(value)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if value <= 0:
            print("Please enter a number greater than 0.")
            continue

        return value


def display_resources(resources):
    if not resources:
        print("No resources found.")
        return

    for resource in resources:
        print(
            f"{resource['id']} | "
            f"{resource['name']} | "
            f"{resource['category']} | "
            f"Total: {resource['total']} | "
            f"Available: {resource['available']}"
        )


def handle_add_resource():
    print("\n--- Add Resource ---")

    resource_id = input("Resource ID: ")
    name = input("Resource name: ")
    category = input("Category: ")
    total = get_positive_integer("Total units: ")

    success, message = add_resource(
        resource_id,
        name,
        category,
        total
    )

    print(message)


def handle_list_resources():
    print("\n--- Resources ---")
    display_resources(list_resources())


def handle_search():
    print("\n--- Search Resources ---")

    name = input("Enter name to search: ")

    results = search_resources(name)

    display_resources(results)


def handle_filter():
    print("\n--- Filter Resources ---")

    category = input("Enter category: ")

    results = filter_by_category(category)

    display_resources(results)


def handle_borrow():
    print("\n--- Borrow Resource ---")

    fellow_id = input("Fellow ID: ")
    resource_id = input("Resource ID: ")
    quantity = get_positive_integer("Quantity: ")

    success, message = borrow_resource(
        fellow_id,
        resource_id,
        quantity
    )

    print(message)


def handle_return():
    print("\n--- Return Resource ---")

    fellow_id = input("Fellow ID: ")
    resource_id = input("Resource ID: ")
    quantity = get_positive_integer("Quantity: ")

    success, message = return_resource(
        fellow_id,
        resource_id,
        quantity
    )

    print(message)


def handle_report():
    print("\n--- Report ---")

    report = generate_report()

    print(f"Total units: {report['total_units']}")
    print(f"Available units: {report['available_units']}")
    print(f"Currently borrowed: {report['borrowed_units']}")

    print("\nLow stock:")
    if report["low_stock"]:
        for resource in report["low_stock"]:
            print(
                f"- {resource['name']}: "
                f"{resource['available']} available"
            )
    else:
        print("None")

    print("\nMost borrowed:")
    for item in report["most_borrowed"]:
        resource = item["resource"]
        borrowed = item["borrowed"]

        print(
            f"- {resource['name']}: "
            f"{borrowed} currently borrowed"
        )


def show_menu():
    print()
    print(BOLD + CYAN + "========================================" + RESET)
    print(BOLD + CYAN + " LEARN2EARN EQUIPMENT LENDING" + RESET)
    print(BOLD + CYAN + "========================================" + RESET)

    print(BLUE + "1." + RESET + " Add resource")
    print(BLUE + "2." + RESET + " List resources")
    print(BLUE + "3." + RESET + " Search resources")
    print(BLUE + "4." + RESET + " Filter by category")
    print(BLUE + "5." + RESET + " Borrow resource")
    print(BLUE + "6." + RESET + " Return resource")
    print(BLUE + "7." + RESET + " View report")
    print(YELLOW + "8." + RESET + " Exit")


def main():
    while True:
        show_menu()

        choice = input(BOLD + BLUE + "Choose an option: " + RESET)

        if choice == "1":
            handle_add_resource()

        elif choice == "2":
            handle_list_resources()

        elif choice == "3":
            handle_search()

        elif choice == "4":
            handle_filter()

        elif choice == "5":
            handle_borrow()

        elif choice == "6":
            handle_return()

        elif choice == "7":
            handle_report()

        elif choice == "8":
            print(BOLD + CYAN + "Goodbye." + RESET)
            break

        else:
            print("Invalid opion. Please choose 1-8.")


if __name__ == "__main__":
    main()
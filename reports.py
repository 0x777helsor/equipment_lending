from data import resources, borrow_records


def get_borrowed_quantity(resource_id):
    total = 0

    for record in borrow_records:
        if record["resource_id"] == resource_id:
            total += record["quantity"]

    return total


def get_total_units():
    total = 0

    for resource in resources:
        total += resource["total"]

    return total


def get_available_units():
    total = 0

    for resource in resources:
        total += resource["available"]

    return total


def get_low_stock_resources():
    low_stock = []

    for resource in resources:
        if resource["available"] < 3:
            low_stock.append(resource)

    return low_stock


def get_most_borrowed_resources():
    borrowed_amounts = []

    for resource in resources:
        borrowed = get_borrowed_quantity(resource["id"])

        borrowed_amounts.append({
            "resource": resource,
            "borrowed": borrowed
        })

    highest = 0

    for item in borrowed_amounts:
        if item["borrowed"] > highest:
            highest = item["borrowed"]

    most_borrowed = []

    for item in borrowed_amounts:
        if item["borrowed"] == highest:
            most_borrowed.append(item)

    return most_borrowed


def generate_report():
    total_units = get_total_units()
    available_units = get_available_units()
    borrowed_units = total_units - available_units

    return {
        "total_units": total_units,
        "available_units": available_units,
        "borrowed_units": borrowed_units,
        "low_stock": get_low_stock_resources(),
        "most_borrowed": get_most_borrowed_resources()
    }
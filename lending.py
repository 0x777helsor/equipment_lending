from colors import (
    RESET,
    GREEN,
    RED,
    BOLD,
    BLUE,
    YELLOW
)

from data import fellows, borrow_records
from inventory import find_resource


def borrow_resource(fellow_id, resource_id, quantity):
    if fellow_id not in fellows:
        return False, (BOLD + RED + "Fellow ID not found." + RESET)

    resource = find_resource(resource_id)

    if resource is None:
        return False, (BOLD + RED + "Resource ID not found." + RESET)

    if not isinstance(quantity, int) or isinstance(quantity, bool):
        return False, (BOLD + BLUE + "Quantity must be a positive integer." + RESET)

    if quantity <= 0:
        return False, (BOLD + BLUE + "Quantity must be a positive integer." + RESET)

    if quantity > resource["available"]:
        return False, (BOLD + RED + "Not enough stock available." + RESET)

    resource["available"] -= quantity

    for record in borrow_records:
        if (
            record["fellow_id"] == fellow_id
            and record["resource_id"] == resource_id
        ):
            record["quantity"] += quantity
            break
    else:
        borrow_records.append({
            "fellow_id": fellow_id,
            "resource_id": resource_id,
            "quantity": quantity
        })
    
    return True, (BOLD + GREEN + "Borrowing successful." + RESET)

def return_resource(fellow_id, resource_id, quantity):
    if fellow_id not in fellows:
        return False, (BOLD + RED + "Fellow ID not found." + RESET)

    resource = find_resource(resource_id)

    if resource is None:
        return False, (BOLD + RED + "Resource ID not found." + RESET)

    if not isinstance(quantity, int) or isinstance(quantity, bool):
        return False, (BOLD + BLUE + "Quantity must be a positive integer." + RESET)

    if quantity <= 0:
        return False, (BOLD + BLUE + "Quantity must be a positive integer." + RESET)

    for record in borrow_records:
        if (
            record["fellow_id"] == fellow_id
            and record["resource_id"] == resource_id
        ):
            if quantity > record["quantity"]:
                return False, "Return quantity exceeds current loan." 

            record["quantity"] -= quantity
            resource["available"] += quantity

            if record["quantity"] == 0:
                borrow_records.remove(record)

            return True, (BOLD + GREEN + "Return successful." + RESET)

    return False,  "Fellow does not currently have this resource on loan."
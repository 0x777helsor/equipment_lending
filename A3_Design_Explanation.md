# A3 --- Design and Implementation Explanation

## Project Structure

The project is divided into five Python files:

``` text
equipment_lending/
├── main.py
├── inventory.py
├── lending.py
├── reports.py
└── data.py
```

Each file has a specific responsibility.

  -----------------------------------------------------------------------
  File                                Responsibility
  ----------------------------------- -----------------------------------
  `data.py`                           Stores resources, fellows, and
                                      borrowing records

  `inventory.py`                      Handles adding, listing, searching,
                                      and filtering resources

  `lending.py`                        Handles borrowing and returning
                                      equipment

  `reports.py`                        Calculates inventory and borrowing
                                      reports

  `main.py`                           Handles the CLI menu, user input,
                                      validation, and display
  -----------------------------------------------------------------------

## Functions

The application is divided into meaningful functions rather than placing
all logic in one large function.

Examples include:

-   `find_resource()` --- finds a resource using its unique ID.
-   `add_resource()` --- adds a new resource and prevents duplicate
    resource IDs.
-   `search_resources()` --- searches resource names without case
    sensitivity.
-   `filter_by_category()` --- filters resources by category.
-   `borrow_resource()` --- validates and records a borrowing operation.
-   `return_resource()` --- validates and processes equipment returns.
-   `get_borrowed_quantity()` --- calculates how many units of a
    resource are currently on loan.
-   `generate_report()` --- combines the report calculations.
-   `get_positive_integer()` --- validates quantity input from the CLI.

This separation gives each function a focused responsibility and makes
the program easier to understand, test, and maintain.

## Inventory Representation

The inventory is represented as a **list of dictionaries** in `data.py`.

Example:

``` python
{
    "id": "R001",
    "name": "Laptop",
    "category": "Electronics",
    "total": 10,
    "available": 10
}
```

Each dictionary represents one resource.

The `total` value represents the total number of units owned by
Learn2Earn. The `available` value represents the number of units that
are currently available to borrow.

The number currently borrowed can therefore be calculated as:

``` text
currently borrowed = total - available
```

## Fellow Loan Representation

Current loans are represented using a **list of dictionaries** called
`borrow_records`.

Example:

``` python
{
    "fellow_id": "F001",
    "resource_id": "R001",
    "quantity": 2
}
```

This means that fellow `F001` currently has 2 units of resource `R001`
on loan.

If the same fellow borrows more units of the same resource, the existing
quantity is increased. If the quantity reaches zero after a return, the
borrowing record is removed.

## Validation and State Consistency

The application validates an operation before changing the inventory.

For example, if a fellow requests more equipment than is available, the
operation is rejected:

``` text
Not enough stock available.
```

The inventory is not reduced.

Similarly, if a fellow attempts to return more equipment than they
currently have on loan, the operation is rejected:

``` text
Return quantity exceeds current loan.
```

The borrowing record and inventory remain unchanged.

This protects the core inventory invariant:

``` text
total = available + currently borrowed
```

The application also validates quantity input through
`get_positive_integer()`, preventing zero, negative numbers, and
non-numeric values from being accepted as quantities.

## Menu and Program Flow

`main.py` contains a looping command-line menu.

The program continues displaying the menu until the user selects the
Exit option.

The menu provides operations for:

1.  Adding a resource
2.  Listing resources
3.  Searching resources
4.  Filtering by category
5.  Borrowing a resource
6.  Returning a resource
7.  Viewing the report
8.  Exiting

This keeps the application interactive while maintaining the separation
between user interaction and business logic.

## Design Limitation

A limitation of the current design is that it tracks **quantities rather
than individual physical equipment assets**.

For example, if Learn2Earn owns five laptops, the system knows that five
laptops exist, but it does not distinguish individual physical devices
by serial number.

Therefore, the system cannot determine which exact physical laptop was
issued to a fellow.

A future asset-tracking version could assign a unique identifier or
serial number to every physical item.

## A3 Summary

The design uses simple Python data structures and separate modules to
implement the required equipment lending functionality. The separation
of inventory, lending, reporting, data, and user-interface
responsibilities keeps the application understandable while maintaining
the required validation and inventory consistency.

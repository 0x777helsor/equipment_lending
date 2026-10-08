# A2 --- Demonstration and Test Evidence

## Program Execution

The application was run locally using:

``` bash
python3 main.py
```

The required demonstration was performed using the Learn2Earn Equipment
Lending CLI.

## 1. F001 borrows 2 laptops

``` text
--- Borrow Resource ---
Fellow ID: F001
Resource ID: R001
Quantity: 2
Borrowing successful.
```

The laptop availability was reduced from 10 to 8.

## 2. F002 borrows 3 keyboards

``` text
--- Borrow Resource ---
Fellow ID: F002
Resource ID: R002
Quantity: 3
Borrowing successful.
```

The keyboard availability was reduced from 5 to 2.

## 3. F001 returns 1 laptop

``` text
--- Return Resource ---
Fellow ID: F001
Resource ID: R001
Quantity: 1
Return successful.
```

The laptop availability became 9.

## 4. F003 requests 4 headsets

``` text
--- Borrow Resource ---
Fellow ID: F003
Resource ID: R003
Quantity: 4
Not enough stock available.
```

The request was rejected because only 3 headsets were available.

## 5. F002 attempts to return 4 keyboards

``` text
--- Return Resource ---
Fellow ID: F002
Resource ID: R002
Quantity: 4
Return quantity exceeds current loan.
```

The return was rejected because F002 had only 3 keyboards on loan.

## 6. Case-insensitive search

The search was performed using:

``` text
Enter name to search: LAPtop
```

The program found:

``` text
R001 | Laptop | Electronics | Total: 10 | Available: 9
```

This demonstrates that the resource search is case-insensitive.

## 7. Inventory report

The report produced:

``` text
--- Report ---
Total units: 18
Available units: 14
Currently borrowed: 4

Low stock:
- Keyboard: 2 available

Most borrowed:
- Keyboard: 3 currently borrowed
```

The report therefore confirms:

-   Total units: **18**
-   Available units: **14**
-   Currently borrowed: **4**
-   Low-stock resource: **Keyboard --- 2 available**
-   Most borrowed resource: **Keyboard --- 3 currently borrowed**

## Additional Invalid-Input Test

An invalid quantity of `0` was entered:

``` text
Quantity: 0
Please enter a number greater than 0.
```

The program rejected the invalid quantity and requested another value.

## A2 Conclusion

The demonstration confirms that the application:

-   Processes valid borrowing and return operations.
-   Rejects borrowing when stock is insufficient.
-   Rejects returns exceeding a fellow's current loan.
-   Performs case-insensitive resource searches.
-   Generates the required inventory report.
-   Validates invalid quantity input.

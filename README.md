# Python Practice Projects

This repository contains several Python practice files covering basic
programming concepts, loops, user input, classes, and turtle graphics.

## Files

### `Bank_account.py`

A practice exercise about **encapsulation and classes**. It defines a
`BankAccount` class with methods for displaying account information,
getting and setting a balance, depositing, withdrawing, and transferring
money.

**Note:** This file appears to contain indentation or syntax issues in
some sections, so it may need debugging before it runs successfully.

### `guessing_game_pratice.py`

A number-guessing game. The program chooses a random number between 1
and 1,000, and the player has up to 10 attempts to guess it. It gives
hints to guess higher or lower.

### `guessing_game_pratice(1).py`

A second copy of the number-guessing game practice file. It appears to
contain the same code as `guessing_game_pratice.py`.

### `loops_2.py`

A practice file for `for` loops and `while` loops. It includes a list of
rainbow colours and a loop that prints numbers after adding 2.

**Note:** The `while` loop may not finish because the index stops
increasing when the condition becomes false.


### `Mini Supermarket Management System.ipynb`

A Jupyter Notebook for practising Python lists and building the foundations of a mini supermarket management system. It includes product names, prices, and stock; adding and removing products; updating and sorting prices; list slicing and copying; creating a customer cart and receipt text; and working with nested lists to calculate stock totals across branches. It also begins a simple supermarket report and menu.

**Note:** This notebook appears to be a practice exercise rather than a finished application. Some cells may need debugging or completing. For example, the cart-total loop uses `price` rather than the current cart price, and the final menu is only a basic starting point.

### `turtle_task.py`

Uses Python's `turtle` graphics to draw a square on an aqua-coloured
background.

### `star.py`

Uses Python's `turtle` graphics to draw three coloured stars on a black
background.

## Requirements

-   Python 3
-   Jupyter Notebook or JupyterLab to open `Mini Supermarket Management System.ipynb`
-   The `turtle` module for `turtle_task.py` and `star.py` (usually
    included with standard Python installations)

No extra packages are needed for the guessing game, loops, or bank
account practice files.

## How to Run

1.  Install Python 3 if it is not already installed.

2.  Open a terminal or command prompt in the folder containing these
    files.

3.  Run a file using:

    ``` bash
    python filename.py
    ```

    For example:

    ``` bash
    python guessing_game_pratice.py
    ```

4.  For the turtle files, make sure your environment supports opening a
    graphics window.

## Topics Practised

-   Classes and objects
-   Encapsulation, getters, and setters
-   Basic bank-account operations
-   Random numbers and user input
-   `for` and `while` loops
-   Lists and conditional statements
-   Turtle graphics, loops, and shapes
-   List operations, sorting, slicing, copying, nested lists, shopping carts, and supermarket stock reports

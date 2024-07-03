# Restaurant Management System

This project is a comprehensive restaurant management system designed to handle various aspects of running a restaurant, including menu management, warehouse management, user management, and order processing. The system is divided into several modules, each responsible for a specific part of the restaurant operations.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
   - [Menu Management](#menu-management)
   - [Warehouse Management](#warehouse-management)
   - [User Management](#user-management)
   - [Waiters Management](#waiters-management)
3. [Files](#files)

## Installation

To run this project, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

1. Clone this repository:
    ```sh
    git clone https://github.com/yourusername/restaurant-management-system.git
    ```
2. Navigate to the project directory:
    ```sh
    cd restaurant-management-system
    ```
3. Install the required dependencies (if any).

## Usage

### Menu Management

The menu management module allows you to add, remove, and view dishes and their ingredients.

#### Adding a New Dish
Run the `new_dish()` function to add a new dish to the menu.

#### Removing a Dish
Run the `remove_dish()` function to remove a dish from the menu.

### Warehouse Management

The warehouse management module allows you to manage the inventory of products.

#### Adding a New Product
Run the `new_product()` function to add a new product to the warehouse.

#### Dropping a Product
Run the `drop_product()` function to remove a product from the warehouse.

#### Viewing the Warehouse Inventory
Run the `kitchen_warehouse()` or `accountant_warehouse()` functions to view the current inventory.

### User Management

The user management module allows you to manage user accounts and their roles.

#### Adding a New User
Run the `new_user()` function to add a new user.

#### Editing a User
Run the `edit_user()` function to edit an existing user's details.

#### Deleting a User
Run the `delete_user()` function to remove a user.

### Waiters Management

The waiters management module handles the order process and checks the warehouse for ingredient availability.

#### Processing an Order
Run the `waiter()` function to process an order, check for ingredient availability, and record income.

## Files

- `menu.csv`: Stores the menu items.
- `dish_ingredients.csv`: Stores the ingredients for each dish.
- `warehouse.csv`: Stores the warehouse inventory.
- `incomes.csv`: Stores the recorded incomes.
- `writer.csv`: Stores the user details.



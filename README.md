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



# Burger Bar Krikina Management System

## Overview

Welcome to the Burger Bar Krikina Management System repository! This system is designed to manage various aspects of a restaurant, including user management, order processing, inventory management, and menu management. The system is implemented in Python and uses CSV files for data storage. This README provides an overview of the system's functionality, installation instructions, and usage guidelines.

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
   - [User Management](#user-management)
   - [Order Processing](#order-processing)
   - [Inventory Management](#inventory-management)
   - [Menu Management](#menu-management)
4. [Functions](#functions)
5. [Contributing](#contributing)
6. [License](#license)

## Installation

To run the Burger Bar Krikina Management System, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/burger-bar-krikina.git
   cd burger-bar-krikina


Create CSV files:
Create the following CSV files in the root directory if they do not exist:

menu.csv
dish_ingredients.csv
warehouse.csv
incomes.csv
writer.csv
The structure of these files is defined in the code.

Usage
User Management
Adding a User: Users can be added by providing a username, password, and role (admin or customer).
Deleting a User: Users can be removed from the system based on their username.
Viewing Users: All users can be viewed along with their details.
Order Processing
Creating an Order: Orders can be created by specifying the user and the dishes they want to order.
Viewing Orders: All orders can be viewed along with their details, including the user and the total cost.
Updating Order Status: Orders can have their status updated (e.g., from pending to completed).
Inventory Management
Viewing Inventory: The current inventory of ingredients can be viewed.
Adding Inventory: New ingredients can be added to the inventory with their quantities.
Updating Inventory: Existing inventory quantities can be updated based on usage or restocking.
Menu Management
Viewing Menu: The current menu can be viewed with all available dishes.
Adding a Dish: New dishes can be added to the menu by specifying their ingredients and prices.
Deleting a Dish: Dishes can be removed from the menu based on their name.
Functions
User Management Functions
add_user(username, password, role): Adds a new user to the system.
delete_user(username): Deletes a user from the system.
view_users(): Displays all users in the system.
Order Processing Functions
create_order(user, dishes): Creates a new order for a user.
view_orders(): Displays all orders in the system.
update_order_status(order_id, status): Updates the status of an order.
Inventory Management Functions
view_inventory(): Displays the current inventory.
add_inventory(ingredient, quantity): Adds a new ingredient to the inventory.
update_inventory(ingredient, quantity): Updates the quantity of an existing ingredient in the inventory.
Menu Management Functions
view_menu(): Displays the current menu.
add_dish(dish_name, ingredients, price): Adds a new dish to the menu.
delete_dish(dish_name): Removes a dish from the menu.
Contributing
Contributions are welcome! Please open an issue or submit a pull request with your changes. Make sure to follow the project's code style and add tests for any new features or bug fixes.
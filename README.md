# restaurant_app


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
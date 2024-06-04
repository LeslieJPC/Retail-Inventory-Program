# Retail Inventory Program

## Overview
The **Retail Inventory Program** is a Python application that manages retail items, displaying details such as item name, description, units in inventory, and price. This simple program helps in keeping track of inventory items and their attributes.

## Features
- Creation of `RetailItem` objects to represent individual retail items.
- Display of item details including name, description, units in inventory, and price.
- Easy-to-understand output format for quick reference.

## Code Structure
The application consists of a single Python script that defines a `RetailItem` class and a `main` function to instantiate and display retail items.

### Class: RetailItem
The `RetailItem` class is used to create objects that store details about each retail item.

#### Attributes
- `item`: The name or identifier of the item.
- `description`: A brief description of the item.
- `units_in_inventory`: The number of units available in inventory.
- `price`: The price of the item.

#### Methods
- `__init__(self, item, description, units_in_inventory, price)`: The constructor method initializes the attributes with the provided values.

### Function: main
The `main` function is the entry point of the application.

#### Functionality
- Creates three `RetailItem` objects with predefined data.
- Prints a table header for the inventory list.
- Displays the details of each `RetailItem` object in a formatted manner.

## Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/RetailInventoryProgram.git
    ```
2. Navigate to the project directory:
    ```sh
    cd RetailInventoryProgram
    ```

### Usage
1. Run the Python script:
    ```sh
    python retail_inventory.py
    ```
2. The output will display the details of the retail items in a formatted table.

## Example Output
```
Retail Items Available
Item            Description         Units_In_Inventory        Price
Item #1         Jacket                     12                          59.95
Item #2         Designer Jeans     40                          34.95
Item #3         Shirt                      20                          24.95
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Author
- Leslie

Feel free to reach out for any questions or contributions. Happy coding!

---

### Note
This application is a sample project intended for learning and demonstration purposes. It may require further enhancements and testing for production use.

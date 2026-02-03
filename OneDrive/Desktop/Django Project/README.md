# LuxeStore - Django E-commerce Project

## Project Overview
LuxeStore is a fully functional e-commerce web application built with **Django**. It is designed to simulate a real-world online shopping experience with a premium, responsive user interface.

## How It Works (Architecture)

The project follows the standard **Django MVT (Model-View-Template)** pattern, split into 4 distinct applications:

### 1. The Shop App (`shop/`)
*   **Purpose**: Manages the product catalog and display.
*   **Data Models**:
    *   `Category`: Groups products (e.g., Watches, Bags).
    *   `Product`: Stores item details (Name, Price, Image, Description).
*   **Flow**:
    *   User visits `/` -> `views.product_list` fetches products -> Renders `list.html`.
    *   User clicks a product -> `views.product_detail` fetches specific item -> Renders `detail.html`.

### 2. The Cart App (`cart/`)
*   **Purpose**: Manages the temporary shopping cart.
*   **Mechanism**:
    *   It uses **Django Sessions** (`request.session`) to store selected items. This means the cart data is saved in the browser's session cookie, not the database.
    *   Users can add items, update quantities, or remove items without needing to log in.
*   **Key File**: `cart/cart.py` contains the logic to add, remove, and calculate totals.

### 3. The Orders App (`orders/`)
*   **Purpose**: Handles the checkout process and permanent record keeping.
*   **Data Models**:
    *   `Order`: Stores customer info (Name, Address, Email).
    *   `OrderItem`: Links products to an order with the price at the time of purchase.
*   **Flow**:
    *   User clicks "Checkout" -> Enters details in `OrderCreateForm`.
    *   On submit -> Data is saved to `db.sqlite3` -> Cart is cleared -> Success message shown.

### 4. The Accounts App (`accounts/`)
*   **Purpose**: Manages User Authentication.
*   **Features**:
    *   Uses Django's built-in `User` model.
    *   Allows users to **Register** and **Login**.
    *   The header updates dynamically to show "Hello, [Username]" when logged in.

---

## Setup & Run Instructions

1.  **Environment Setup**:
    ```powershell
    # Activate virtual environment
    .\venv\Scripts\activate
    ```

2.  **Run the Server**:
    ```powershell
    python manage.py runserver
    ```

3.  **Access the Site**:
    *   **Storefront**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    *   **Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) (User: `admin`, Pass: `admin123`)

## Key Technologies
*   **Backend**: Django 5.x / 6.x
*   **Database**: SQLite (Default)
*   **Frontend**: HTML5, Vanilla CSS3 (Custom "Outfit" font styling)
*   **Images**: Pillow (for handling product uploads)

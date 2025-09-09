# Fashion Ecommerce API

## Overview

This project is a full-featured e-commerce backend built with Python and the Django framework. It provides a complete server-side rendered application for managing products, categories, user accounts, and a multi-functional shopping cart.

## Features

- **Django**: Core web framework for routing, database management (ORM), and template rendering.
- **Django Authentication**: Handles user registration, login, logout, and session management.
- **SQLite3**: Default relational database for development, providing persistent storage for all application data.
- **Django Templates**: Server-side rendering engine used to build the dynamic user interface.

## Getting Started

### Installation

Follow these steps to set up the project locally.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/FavourDarasimi/Clothing-Ecommerce-Website.git
    cd Clothing-Ecommerce-Website
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000`.

### Environment Variables

Create a `.env` file in the project root and add the following variables. The project uses default values from `FashionConfig/settings.py` for development.

- `SECRET_KEY`: Django's secret key for cryptographic signing.
  - Example: `SECRET_KEY='your-super-secret-key-here'`
- `DEBUG`: Toggles Django's debug mode. Set to `False` in production.
  - Example: `DEBUG=True`
- `DATABASE_URL`: Connection string for a production database like PostgreSQL.
  - Example: `DATABASE_URL='postgres://user:password@host:port/dbname'`

## API Documentation

This is a server-side rendered application. The following endpoints handle form data and render HTML templates, not JSON payloads.

### Base URL

`http://127.0.0.1:8000/`

### Endpoints

#### Authentication

---

#### **POST** `/accounts/signup/`

Registers a new user.

**Request (Form Data)**:

```
{
  "username": "newuser",
  "first_name": "John",
  "last_name": "Doe",
  "age": 30,
  "email": "john.doe@example.com",
  "password": "securepassword123",
  "password2": "securepassword123"
}
```

**Response**:

- **On Success**: `302 Found` - Redirects to the login page (`/accounts/login/`).
- **On Failure**: `200 OK` - Re-renders the signup page with validation errors.

---

#### **POST** `/accounts/login/`

Logs in an existing user.

**Request (Form Data)**:

```
{
  "username": "newuser",
  "password": "securepassword123"
}
```

**Response**:

- **On Success**: `302 Found` - Redirects to the home page (`/`).
- **On Failure**: `200 OK` - Re-renders the login page with an error message.

---

#### **GET** `/accounts/logout/`

Logs out the currently authenticated user.

**Request**:

- No payload required.

**Response**:

- `302 Found` - Redirects to the home page (`/`).

---

#### Products & Categories

---

#### **GET** `/`

Displays the home page with new products.

**Request**:

- No payload required.

**Response**:

- `200 OK` - Renders `home.html` with a list of products where `new=True`.

---

#### **GET** `/category/`

Displays all available product categories.

**Request**:

- No payload required.

**Response**:

- `200 OK` - Renders `category.html` with a list of all active categories.

---

#### **GET** `/products/<int:pk>`

Displays all products belonging to a specific category.

**Request**:

- `pk`: The ID of the `Category`.

**Response**:

- `200 OK` - Renders `product_view.html` with products filtered by the category ID.

---

#### **GET** `/details/<int:pk>`

Displays the detailed view for a single product.

**Request**:

- `pk`: The ID of the `Product`.

**Response**:

- `200 OK` - Renders `product_detail.html` with the specified product's details and comments.

---

#### **POST** `/search_products`

Searches for products by name.

**Request (Form Data)**:

```
{
  "searched": "Shirt"
}
```

**Response**:

- `200 OK` - Renders `search_result.html` with a list of products whose names contain the search term.

---

#### Comments

---

#### **POST** `/details/comment/<int:pk>`

Adds a comment to a product. Requires user to be authenticated.

**Request**:

- `pk`: The ID of the `Product` being commented on.
- **Form Data**:
  ```
  {
    "comment": "This is a great product!"
  }
  ```

**Response**:

- `302 Found` - Redirects back to the product detail page (`/details/<int:pk>`).

---

#### Shopping Cart

---

#### **GET** `/mycart/`

Displays the contents of the user's shopping cart. Requires user to be authenticated.

**Request**:

- No payload required.

**Response**:

- `200 OK` - Renders `cartview.html` with all items in the current user's cart, along with total quantity and cost.

---

#### **GET** `/add/<int:pk>`

Adds a product to the user's cart. Requires user to be authenticated.

**Request**:

- `pk`: The ID of the `Product` to add.

**Response**:

- `302 Found` - Redirects to the cart view page (`/mycart/`).

---

#### **GET** `/add/quantity/<int:pk>`

Increments the quantity of an item in the cart.

**Request**:

- `pk`: The ID of the `CartItem`.

**Response**:

- `302 Found` - Redirects to the cart view page (`/mycart/`).

---

#### **GET** `/subtract/quantity/<int:pk>`

Decrements the quantity of an item in the cart. If quantity becomes zero, the item is removed.

**Request**:

- `pk`: The ID of the `CartItem`.

**Response**:

- `302 Found` - Redirects to the cart view page (`/mycart/`).

---

#### **GET** `/remove/<int:pk>`

Removes an item completely from the cart.

**Request**:

- `pk`: The ID of the `CartItem`.

**Response**:

- `302 Found` - Redirects to the cart view page (`/mycart/`).

---

### **Errors**

- **403 Forbidden**: Occurs when an unauthenticated user tries to access a protected route (e.g., adding an item to the cart).
- **404 Not Found**: Occurs when requesting a resource that does not exist (e.g., a product with an invalid ID).
- **Form Validation Errors**: Returned with a `200 OK` status, re-rendering the form page with specific error messages displayed to the user (e.g., incorrect password during login).

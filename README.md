
#  E-Commerce REST API Backend

A fully-featured Django REST Framework e-commerce backend with JWT authentication, cart management, order processing, and wishlist functionality.

## 📋 Project Overview

This is a production-ready e-commerce platform backend built with Django REST Framework. It demonstrates solid backend engineering principles including:
- Multi-app architecture with separation of concerns
- RESTful API design patterns
- JWT-based authentication with token management
- Complex business logic (cart → order workflow)
- Proper database relationships and constraints
- Permission-based access control

**Status**: ✅ Fully Functional MVP

---

## 🎯 Key Features

### ✅ Authentication & User Management
- **JWT Authentication**: Secure token-based auth with automatic refresh
- **Custom User Model**: Extended Django User with phone number and email
- **Token Blacklist**: Logout functionality via token blacklist
- **Registration & Login**: Full user lifecycle management

### ✅ Product Catalog
- Complete CRUD operations for products
- Stock management and availability tracking
- Category-based organization
- Product filtering and search capabilities
- Admin-only product management

### ✅ Shopping Cart
- User-specific cart persistence across sessions
- Add/update/remove items with quantity management
- Automatic stock validation
- Real-time cart total calculations
- One-to-one relationship per user

### ✅ Order Management
- Complete order lifecycle (pending → delivered)
- Order creation from cart with automatic cart clearing
- Order history per user
- Order item tracking with historical pricing
- Address association with orders
- Total amount calculation

### ✅ Wishlist
- Save favorite products for later
- Persistent wishlist per user
- Add/remove wishlist items
- View all wishlist products

### ✅ Address Management
- Multiple addresses per user
- Default address selection
- Comprehensive address fields (street, city, postal code, etc.)
- Full CRUD operations

### ✅ Permission & Security
- Role-based access control (authenticated users, admin)
- User isolation (users can only access their own data)
- Password hashing and validation
- CSRF protection
- Secure token management with rotation

---

## 🏗️ Architecture

### Database Schema

# E-Commerce REST API Backend

A production-ready Django REST Framework e-commerce platform backend implementing professional enterprise patterns for authentication, cart management, order processing, and inventory control.

## 🎯 Project Overview

This is a fully-featured e-commerce REST API built with industry best practices:
- **Multi-app Django architecture** with clean separation of concerns
- **JWT authentication** with secure token rotation and refresh mechanisms
- **Complex business logic** handling cart → order → fulfillment workflows
- **Transaction-safe operations** with PostgreSQL and proper constraint management
- **Role-based access control** (RBAC) for public, authenticated, and admin users
- **Production-ready** with environment-based configuration and comprehensive API design

**Status**: ✅ Fully Functional MVP | Ready for Production Deployment

---

## 🏗️ Architecture

### Core Features

**Authentication & Security**
- JWT token-based authentication with 15-minute access token lifetime
- Automatic token refresh mechanism with rotation
- Token blacklist system for secure logout
- Password hashing, email validation, and phone number support
- Role-based permission classes (Authenticated, Admin-only, Public Read)

**Product Catalog & Inventory**
- Complete CRUD operations for products with admin-only write access
- Real-time stock tracking with availability validation
- Category-based product organization and filtering
- Pagination and search capabilities

**Shopping Cart System**
- User-specific, persistent cart (one-to-one relationship)
- Add/update/remove cart items with quantity management
- Automatic stock validation on cart operations
- Real-time cart total calculations using database aggregations
- Cart clears automatically upon successful order creation

**Order Management**
- 6-stage order lifecycle: pending → confirmed → processing → in_transit → out_for_delivery → delivered
- Order creation from cart with historical pricing snapshot
- Complete order history per user with status tracking
- Order-level total calculation from items (handles decimal precision)
- Address association for shipping information

**Additional Features**
- Wishlist system for saving favorite products
- Multiple address management per user with default address selection
- Comprehensive address fields (street, city, postal code, country, etc.)

### Database Schema

```
CustomUser (extends Django User)
├── phone_number
├── email

Cart (one-to-one per user)
├── CartItem (many) → Product
└── total_amount (calculated)

Order (per user)
├── OrderItem (many) → Product (with historical pricing)
├── Address (shipping)
├── status (choice field)
└── total_amount (calculated from items)

Product
├── Category
├── stock (inventory)
├── price (decimal with validation)
├── created_at / updated_at

Wishlist (many-to-many through)
├── User
└── Product

Address (multiple per user)
├── user
└── is_default
```

### Application Structure

```
onlineshop/
├── onlineshop/           Django project settings & URL routing
│   ├── settings.py       Configuration with environment variables
│   ├── urls.py           API route definitions
│   └── wsgi.py           Production WSGI application
├── User/                 Custom user model & related views
├── Authentication/       JWT login, registration, logout
├── Product/              Product catalog, filtering
├── Cart/                 Cart creation & retrieval
├── CartItem/             Individual cart item operations
├── Order/                Order creation & history
├── Address/              Shipping address management
├── Wishlist/             Product wishlist functionality
├── Category/             Product categorization
├── requirements.txt      Python dependencies
└── manage.py             Django CLI utility
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- PostgreSQL 12+
- pip / virtual environment

### Installation

```bash
# 1. Clone repository
git clone https://github.com/taranom667/shop.git
cd shop/onlineshop

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
cp .env.example .env
# Edit .env with your configuration:
# SECRET_KEY=your-secret-key
# DEBUG=False (for production)
# DB_ENGINE=django.db.backends.postgresql
# DB_NAME=shopdatabase
# DB_USER=postgres
# DB_PASSWORD=your-password
# DB_HOST=localhost
# DB_PORT=5432

# 5. Apply migrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. Run development server
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

---

## 📡 API Endpoints

### Authentication
- `POST /api/auth/register/` — Create new user account
- `POST /api/auth/login/` — Obtain access & refresh tokens (SimpleJWT)
- `POST /api/auth/refresh/` — Refresh access token
- `POST /api/auth/logout/` — Blacklist refresh token

### Products
- `GET /api/products/` — List all products (paginated, filterable)
- `GET /api/products/{id}/` — Product details
- `POST /api/products/` — Create product (admin only)
- `PUT /api/products/{id}/` — Update product (admin only)
- `DELETE /api/products/{id}/` — Delete product (admin only)

### Cart
- `GET /api/cart/` — Retrieve user's cart
- `POST /api/cart/` — Create cart for user
- `POST /api/cart-items/` — Add item to cart
- `PUT /api/cart-items/{id}/` — Update cart item quantity
- `DELETE /api/cart-items/{id}/` — Remove from cart

### Orders
- `POST /api/orders/` — Create order from cart (auto-clears cart)
- `GET /api/orders/` — View user's order history
- `GET /api/orders/{id}/` — Order details with items

### Addresses
- `GET /api/addresses/` — List user's addresses
- `POST /api/addresses/` — Create new address
- `PUT /api/addresses/{id}/` — Update address
- `DELETE /api/addresses/{id}/` — Delete address

### Wishlist
- `GET /api/wishlist/` — View wishlist items
- `POST /api/wishlist/` — Add product to wishlist
- `DELETE /api/wishlist/{id}/` — Remove from wishlist

---

## 🔐 Security Features

✅ **JWT Authentication** — Stateless, token-based auth with SimpleJWT  
✅ **Token Rotation** — Refresh tokens automatically rotate with blacklisting  
✅ **Password Validation** — Django's built-in validators (complexity, common passwords)  
✅ **CSRF Protection** — Django middleware enabled  
✅ **User Isolation** — Users can only access their own data (enforced via permission classes)  
✅ **Admin Authorization** — Product management restricted to admin users  
✅ **Decimal Precision** — Money fields use DecimalField (not floats)  

---

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test User Authentication

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

---

## 📦 Dependencies

- **Django 6.0.6** — Web framework
- **Django REST Framework 3.17.1** — REST API toolkit
- **djangorestframework-simplejwt 5.5.1** — JWT authentication
- **psycopg2-binary 2.9.12** — PostgreSQL adapter
- **python-dotenv 1.2.3** — Environment variable management
- **django-filter 26.1** — Query filtering

---

## 🌱 Environment Variables

Create `.env` file in project root:

```
SECRET_KEY=your-django-secret-key-here
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

DB_ENGINE=django.db.backends.postgresql
DB_NAME=shopdatabase
DB_USER=postgres
DB_PASSWORD=secure-password
DB_HOST=localhost
DB_PORT=5432
```

---

## 📈 Deployment

### Production Checklist
- [ ] Set `DEBUG=False`
- [ ] Use strong `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up PostgreSQL (not SQLite)
- [ ] Use environment variables for all secrets
- [ ] Run `collectstatic` for static files
- [ ] Enable HTTPS
- [ ] Set `CSRF_TRUSTED_ORIGINS`
- [ ] Configure CORS if frontend is separate
- [ ] Use gunicorn + nginx for production

### Heroku Deployment

```bash
heroku create your-app-name
heroku addons:create heroku-postgresql:standard-0
heroku config:set SECRET_KEY="your-secret-key"
git push heroku main
heroku run python manage.py migrate
```

---

## 🎓 Learning Resources

- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [SimpleJWT Documentation](https://django-rest-framework-simplejwt.readthedocs.io/)
- [Django Security Guide](https://docs.djangoproject.com/en/6.0/topics/security/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---

## 📝 License

MIT License — Feel free to use this project as a reference or starting point.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

## ✨ Author

Built by **taranom667** as a demonstration of professional e-commerce backend development.
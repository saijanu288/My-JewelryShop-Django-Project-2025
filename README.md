🛍️ Jewelry Shop - Django E-commerce Website
A comprehensive web-based application designed to manage and streamline the operations of a jewelry shop. The system includes features for inventory management, order processing, customer management, and sales tracking. Developed using Django, the project provides an intuitive interface for both customers and shop staff, enabling efficient management of daily operations.



🚀 Live Demo
Coming Soon! (You can deploy on Render, Railway, or Heroku.)


✨ Features
🔐 User Authentication (Login, Logout, Registration, Password Reset)



🛍️ Shopping Cart & Checkout System


🛒 Product Browsing by Categories


📦 Order Management


📝 Blog, Contact Page, About Page


🛠️ Admin Dashboard (Manage Products, Orders, Customers)


📬 Email System (Password Reset / Notifications)


📸 Screenshots
<details> <summary>Click to view Screenshots</summary>
Home Page


Product Page


Product Details


Cart Page


Checkout Page


Profile Dashboard


... (more images)

</details>
🛠️ Prerequisites
Python 3.x

pip (Python package manager)

virtualenv (recommended)

⚙️ Installation
bash
Copy
Edit

# Clone the repository
git clone https://github.com/saijanu288/My-JewelryShop-Django-Project-2025.git
cd My-JewelryShop-Django-Project-2025

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver
Then open: http://127.0.0.1:8000/

📁 Project Structure
csharp
Copy
Edit
jewelry_shop/
│
├── store/                    # Main app (models, views, templates)
├── media/                    # User uploaded files
├── static/                   # CSS, JS, Images
├── templates/                # Base templates
└── manage.py                 # Django management script
🧰 Technology Stack
Backend: Django 5.0, Python 3.x

Database: SQLite (dev), PostgreSQL (production ready)

Frontend: HTML5, CSS3, Bootstrap 4, JavaScript

Payment Integration: Razorpay (Coming Soon)

🛒 Key Django Apps Used
django-crispy-forms

django-widget-tweaks

django-environ

Pillow

🔐 Environment Setup
Create a .env file:

env
Copy
Edit
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
🛠️ Development
bash
Copy
Edit
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
python manage.py test

# Check code quality
flake8 .
🛫 Deployment
Heroku Deployment (example)
bash
Copy
Edit
heroku create your-app-name
git push heroku main
heroku run python manage.py migrate
(DigitalOcean deployment guide coming soon!)

📝 Todo
 Payment Gateway Integration

 Wish List Feature

 Product Reviews and Ratings

 Search Functionality

 Product Recommendations

📜 License
This project is licensed under the MIT License.

🤝 Support
For queries or support:
📧 Email: your-email@example.com
🐞 Raise an Issue

<p align="center"> Made with ❤️ by <b>N.Janani</b> </p>
✨ Happy Coding!

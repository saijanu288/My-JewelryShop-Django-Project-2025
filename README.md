# Jewelry Shop - Django E-commerce Website 🛍️

A comprehensive web-based application designed to manage and streamline the operations of a jewelry shop. The system includes features for inventory management, order processing, customer management, and sales tracking. Developed using Django, the project provides an intuitive interface for both customers and shop staff, enabling efficient management of the shop's daily operations.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Django](https://img.shields.io/badge/django-5.0-green.svg)
## Live Demo

Check out the live demo of the Jewelry Shop platform:

![Live Demo](https://github.com/engrmumtazali0112/Jewelry-Shop---Django-E-commerce/blob/main/IMG_9022-ezgif.com-video-to-gif-converter.gif)

## ✨ Features

- 🔐 User Authentication System
  - Registration, Login, Logout
  - Password Reset
  - Profile Management
  - Address Management

- 🛍️ Shopping Features
  - Product Categories
  - Product Details
  - Shopping Cart
  - Order Management
  - Checkout Process

- 📝 Content Management
  - Blog System
  - Contact Form
  - About Page
  - Dynamic Category Navigation

- 💼 Admin Features
  - Product Management
  - Order Tracking
  - User Management
  - Content Management

## 📸 Screenshots
<details>
![Image](https://github.com/user-attachments/assets/79a486cc-3d81-4347-a929-04d566c069a0)
![Image](https://github.com/user-attachments/assets/74e59924-f153-4955-9abb-d597b7e6244e)
![Image](https://github.com/user-attachments/assets/e0387bc7-0e11-4f87-8859-f12516f57278)
![Image](https://github.com/user-attachments/assets/87598ac4-2e74-406d-9049-51baf91f9d27)
![Image](https://github.com/user-attachments/assets/4b633a5e-d68d-4cb0-bfa3-0672c239c6ca)
![Image](https://github.com/user-attachments/assets/3fc7f8e4-0f1c-4b22-8225-d502be831388)
![Image](https://github.com/user-attachments/assets/44ba45a2-1962-424b-8f27-ff075f83d727)
![Image](https://github.com/user-attachments/assets/607d78a8-086d-4648-91c9-ee9c572b0c3e)
![Image](https://github.com/user-attachments/assets/966286d7-418e-4e4f-9143-c3a84b861172)
![Image](https://github.com/user-attachments/assets/5889393f-960d-47dd-8da6-3adb4b9ee327)
![Image](https://github.com/user-attachments/assets/54665097-99dd-4e85-98c4-6b950bf2e8ca)
![Image](https://github.com/user-attachments/assets/9d225030-cbb4-4f01-9a08-ac7423960b4b)
![Image](https://github.com/user-attachments/assets/922c2157-f14c-48bc-835d-e883d857d699)
![Image](https://github.com/user-attachments/assets/ec9e531d-355a-4b0e-8f1a-9e0aff340660)
![Image](https://github.com/user-attachments/assets/c3b0ddad-938e-4f64-8a5b-905534286f31)
![Image](https://github.com/user-attachments/assets/d8ced9a2-92ac-4952-b032-1a5ef07dcca7)
</details>

### Prerequisites

- Python 3.x
- pip (Python package manager)
- virtualenv (recommended)

### Installation

1. Clone the repository
```bash
[git clone https://github.com/yourusername/Jewelry-Shop.git](https://github.com/engrmumtazali0112/Jewelry-Shop---Django-E-commerce.git)
cd Jewelry-Shop
```

2. Create and activate virtual environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
# Copy example environment file
cp .env.example .env
# Edit .env with your settings
```

5. Run migrations
```bash
python manage.py migrate
```

6. Create superuser
```bash
python manage.py createsuperuser
```

7. Start development server
```bash
python manage.py runserver
```

8. Visit http://127.0.0.1:8000/ in your browser

## 📁 Project Structure

```
jewelry_shop/
│
├── store/                      # Main app directory
│   ├── migrations/            # Database migrations
│   ├── static/                # Static files
│   │   ├── css/
│   │   ├── js/
│   │   ├── img/
│   │   └── vendor/
│   ├── templates/             # HTML templates
│   │   ├── account/          # Account-related templates
│   │   └── store/            # Store-related templates
│   ├── models.py             # Database models
│   ├── views.py              # View logic
│   ├── urls.py               # URL configurations
│   └── forms.py              # Form definitions
│
├── templates/                  # Base templates
├── media/                     # User-uploaded files
├── static/                    # Static files
└── manage.py                  # Django management script
```

## 🔧 Technology Stack

- **Backend**
  - Django 5.0
  - Python 3.x
  - SQLite (development)
  - PostgreSQL (production)

- **Frontend**
  - HTML5
  - CSS3
  - JavaScript
  - Bootstrap 4
  - Font Awesome

- **Payment Integration**
  - [Payment Gateway] (Coming Soon)

## 📝 Dependencies

```txt
Django>=5.0.0
Pillow>=10.0.0
django-crispy-forms>=2.1
django-environ>=0.11.2
django-widget-tweaks>=1.5.0
```

## 🛠️ Configuration

Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-specific-password
```

## 👥 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

For support, email [your-email@example.com](mailto:your-email@example.com) or create an issue in the GitHub repository.

## 🙏 Acknowledgments

- Bootstrap Templates
- Django Documentation
- Font Awesome Icons
- All Contributors

## 📸 Screenshots

[Coming Soon]

## 🚀 Deployment

Detailed deployment instructions for various platforms:

### Heroku
```bash
# Install Heroku CLI
heroku create your-app-name
git push heroku main
heroku run python manage.py migrate
```

### DigitalOcean
[Deployment Guide Coming Soon]

## ⚙️ Development

To set up the development environment:

1. Ensure all dependencies are installed
```bash
pip install -r requirements-dev.txt
```

2. Run tests
```bash
python manage.py test
```

3. Check code style
```bash
flake8 .
```

## 📝 Todo

- [ ] Add payment gateway integration
- [ ] Implement wish list functionality
- [ ] Add product reviews and ratings
- [ ] Implement search functionality
- [ ] Add product recommendations

## 🔄 Version History

* 0.1
    * Initial Release
    * Basic e-commerce functionality

## 📊 Status

Project is: _in progress_

# 📌 Follow Us

📜 License
This repository is licensed under the MIT License.
</p>

<p align="center">Made with ❤️ by N.Janani</p>

**Happy coding!** ✨
# My-Django-Jewelry-Shop-project
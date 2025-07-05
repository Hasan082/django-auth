# Django Authentication System

A simple Django project that implements user authentication including registration, login, logout, password reset, and user profile management.

## 🔧 Project Structure

```

├── authuser/               # Main project folder
│   ├── settings.py         # Django settings
│   ├── urls.py             # Project URLs
│   └── static/css/styles.css  # Custom CSS
├── templates/base.html     # Base template
├── userprofile/            # App handling user authentication
│   ├── models.py           # User-related models
│   ├── forms.py            # Registration/Login forms
│   ├── views.py            # View functions
│   ├── urls.py             # App URLs
│   ├── signals.py          # User signals (e.g. profile creation)
│   └── templates/accounts/ # Auth templates (login, register, etc.)
├── manage.py
├── requirements.txt
└── README.md

````

---

## 🚀 Features

- ✅ User Registration
- ✅ User Login & Logout
- ✅ Password Reset (via email)
- ✅ Profile Page
- ✅ CSRF Protection
- ✅ Template-based frontend
- ✅ Signals for profile creation

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/django-authuser.git
cd django-authuser
````

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 📁 Important Templates

| Template                       | Description               |
| ------------------------------ | ------------------------- |
| `login.html`                   | User login form           |
| `register.html`                | Registration form         |
| `profile.html`                 | User profile              |
| `password_reset.html`          | Request password reset    |
| `password_reset_confirm.html`  | Reset confirmation        |
| `password_reset_done.html`     | Reset email sent          |
| `password_reset_complete.html` | Password reset successful |
| `base.html`                    | Base layout               |

---

## 📬 Email Backend (for Password Reset)

In `settings.py`, add the following for development:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

For production, configure SMTP properly.

---

## 🛠 To Do

* Add user profile update
* Add social authentication (Google, Facebook)
* Add tests for authentication flow

---

## 📝 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Md Hasanuzzaman
[Your GitHub Profile](https://github.com/hasan082)


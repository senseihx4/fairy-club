# 🧚 Fairy Club

## 🌐 Live Demo
👉 **[https://fairy-club-production.up.railway.app](https://fairy-club-production.up.railway.app)**

A fully-featured full-stack web application built with **Django**. Fairy Club is a community membership platform where users can register, manage their profiles, book memberships, share podcasts, and interact through a global mail/messaging system — with nearly every feature fully functional.

---

## ✨ Features

- 🔐 **Authentication** — Signup, Login, Logout, Change Password
- 👤 **Profile Management** — Edit profile details, upload profile picture
- 🏷️ **Membership Booking** — Book and manage club memberships
- 📬 **Global Mail** — Community-wide messaging visible to all members
- 💬 **Replies** — Reply to global mail threads
- 🎙️ **Podcast Upload** — Upload and share podcasts with the community
- ⚙️ **Fully functional UI** — Almost every button and feature works end-to-end

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Backend | Django |
| Frontend | HTML, CSS, JavaScript |
| Database | Django ORM (SQLite) |
| Auth | Django Authentication System |
| File Uploads | Django Media Files |

---

## 📁 Project Structure

```
fairy-club/
└── fairy_club/
    ├── manage.py
    ├── fairy_club/         # Project settings & root URLs
    ├── accounts/           # Auth — login, signup, password change
    ├── profiles/           # Profile editing & picture upload
    ├── membership/         # Membership booking logic
    ├── globalmail/         # Global mail & reply system
    ├── podcasts/           # Podcast upload & listing
    ├── templates/          # HTML templates
    └── static/             # CSS, JS, images
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# Clone the repo
git clone https://github.com/senseihx4/fairy-club.git
cd fairy-club/fairy_club

# Create & activate virtual environment
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows

# Install dependencies
pip install django pillow

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

Then visit `http://127.0.0.1:8000` in your browser.

---

## 📸 Key Flows

**User Journey:**
```
Register → Login → Book Membership → Edit Profile
       → View Global Mail → Reply to Mail
       → Upload Podcast → Change Password
```

---

## 🔮 Planned Improvements

- [x] Remove virtual environment from repo
- [x] Add `requirements.txt`
- [x] Deploy to Railway
- [ ] Email notifications for new global mail
- [ ] Podcast audio player in the browser
- [ ] REST API endpoints for mobile app support

---

## 👨‍💻 Author

**Kartik Sharma** — [GitHub](https://github.com/senseihx4) · [LinkedIn](https://www.linkedin.com/in/kartik-sharma-023a85322/)

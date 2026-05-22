# 🧚 Fairy Club

## 🌐 Live Demo
👉 [https://fairy-club-1.onrender.com](https://fairy-club-1.onrender.com)

A fully-featured full-stack web application built with **Django**. Fairy Club is a community membership platform where users can register, manage their profiles, book memberships, share podcasts, and interact through a global mail/messaging system — with nearly every feature fully functional.

---

## Features

- **Authentication** — Register, login, logout, profile management
- **Memberships** — Book and manage membership plans via Stripe
- **Podcasts** — Share and listen to community podcasts
- **Global Mail** — Send and receive messages within the platform
- **Real-time** — WebSocket support via Django Channels & Daphne
- **Media uploads** — Profile pictures and podcast files via Pillow
 
---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6, Django Channels |
| Server | Daphne (ASGI), Gunicorn |
| Database | PostgreSQL (psycopg2) |
| Payments | Stripe |
| Email | Resend |
| Static files | WhiteNoise |
| Deployment | Render |

---

## Local Setup

```bash
# Clone the repo
git clone https://github.com/senseihx4/fairy-club.git
cd fairy-club

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env  # fill in your values

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
```

---

## Environment Variables

Create a `.env` file with the following:

```
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=your_database_url
STRIPE_SECRET_KEY=your_stripe_key
STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
SENDINBLUE_API_KEY=your_sendinblue_key
```

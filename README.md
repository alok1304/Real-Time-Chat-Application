# 💬 Real-Time Chat App

A real-time chat application using **Django**, **Django Channels**, **Redis (Upstash)**, and **WebSockets** with features like:

- 🗨️ Room-based instant messaging
- 👤 User authentication (signup, login, logout)
- ✍️ Typing indicators
- 🖼️ Image sharing via Base64
- 🌐 Message translation with LibreTranslate API
- 🚀 Deployed on Railway with Daphne + Redis

---

## 🔧 Tech Stack

- **Backend:** Django, Channels, Redis (Upstash), Daphne
- **Frontend:** HTML, CSS, JavaScript
- **WebSocket:** Real-time updates via Django Channels
- **API:** LibreTranslate for message translation

---

## 🚀 Run Locally

```bash
git clone https://github.com/alok1304/Real-Time-Chat-Application.git
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Set your .env:
```
REDIS_URL=rediss://:password@your-db.upstash.io:port

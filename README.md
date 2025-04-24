
# 🧠 AIrenaX - Smart Stadium Experience

AIrenaX is an AI-powered smart stadium management system built with **React + Vite (TypeScript)**, **Node.js (Express)**, **MySQL**, and **Streamlit**. It enhances the fan experience through real-time navigation, crowd detection, virtual queueing and intelligent food recommendations.

---

## 🚀 Features

### 🎟 Seat Navigation with Crowd Awareness
- Interactive 2D stadium map
- Recommends best gate with lowest crowd levels
- Routes users from gate to specific seat, restrooms, or food areas

### 📦 Virtual Queuing System
- View and join queues remotely
- Real-time queue updates via WebSocket
- Notifications when it’s your turn

### 🍽 Smart Recommendations
- ML-powered food suggestions using LightFM
- Personalized to user preferences and order history
- Displays venue images and order count dynamically

### 📍 Venue Overview
- List of all food/merchandise venues
- Displays logo, location, opening hours, and crowd percentage

---

## 🛠 Tech Stack

- **Frontend**: React + Vite (TypeScript), Tailwind CSS
- **Backend**: Node.js (Express + TypeScript)
- **Database**: MySQL + Workbench
- **ML Model**: LightFM (Python)
- **Navigation UI**: Streamlit + OpenCV + Matplotlib
- **Communication**: REST APIs + WebSocket

---

## 🧪 How to Run

### 1. Backend
```bash
cd server
npm install
npm run dev
```

### 2. Frontend
```bash
cd client
npm install
npm run dev
```

### 3. Smart Navigation (Streamlit)
```bash
cd streamlit
streamlit run AIrenaX_CrowdAware_Navigation.py
```
---

## 👩‍💻 Developed By

- Dema Alrahal (AIrenaX Team Lead)
-Amjad alluqmani
-shouq alquraifah
-Fatimah alzahrani
- Built as part of the **AI League Finals 2025**

---



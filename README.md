# CoreStatus: System Resource Monitor Dashboard

> A real-time cybersecurity-adjacent web dashboard that monitors CPU, RAM, Disk, and Network stats on your local machine, built with Python (Flask) and a terminal aesthetic frontend.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=flat-square&logo=flask)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange?style=flat-square)

---

> [!WARNING]
> **Work In Progress --> Backend Not Yet Implemented**
>
> The frontend dashboard UI is complete, but the Python backend (`app.py`) is still being built out. Live data updates are **not functional yet**, and the dashboard currently shows placeholder/static values only.
>
> The backend (Flask + psutil) will be added in a future update to wire up real system metrics.



---

## 📸 Features

- **Terminal/hacker aesthetic** --> scanlines, neon glows, monospace fonts
- **Live CPU usage** --> total % + per-core breakdown with animated bars
- **RAM monitoring** --> used/total/available in GB with ring gauge
- **Disk usage** --> root partition used vs. free storage
- **Network I/O** --> cumulative bytes sent and received
- **System uptime** --> how long your machine has been running
- **Auto-refresh** every 2 seconds --> no manual reload needed

---

## 🚀 Getting Started

> **Note:** The backend isn't wired up yet. For now, you can open `templates/index.html` directly in your browser to preview the UI; it will display the dashboard with placeholder values.

Once the Python backend is complete, the setup will be:

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/sysmon.git
cd sysmon
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

### 5. Open in your browser

```
http://localhost:5000
```

---

## 🗂️ Project Structure

```
sysmon/
├── templates/
│   └── index.html      # Frontend dashboard (HTML + CSS + JS) ✅ Done
├── app.py              # Flask backend — 🚧 coming soon
├── requirements.txt    # Python dependencies — 🚧 coming soon
└── README.md
```

---

## 🛠️ Tech Stack

| Layer     | Tech                              |
|-----------|-----------------------------------|
| Backend   | Python, Flask                     |
| Metrics   | psutil                            |
| Frontend  | Vanilla HTML/CSS/JS               |
| Fonts     | Share Tech Mono, Rajdhani         |

---

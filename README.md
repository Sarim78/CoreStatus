# CoreStatus: System Resource Monitor Dashboard
> A real-time cybersecurity-adjacent web dashboard that monitors CPU, RAM, Disk, and Network stats on your local machine, built with Python (Flask) and a terminal aesthetic frontend.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=flat-square&logo=flask)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

---

## 📸 Features
- **Terminal/hacker aesthetic** --> scanlines, neon glows, monospace fonts
- **Live CPU usage** --> total % + per-core breakdown with animated bars
- **RAM monitoring** --> used/total/available in GB with ring gauge
- **Disk usage** --> root partition used vs. free storage
- **Network I/O** --> cumulative bytes sent and received
- **System uptime** --> how long your machine has been running
- **Auto-refresh** every 2 seconds --> no manual reload needed

> **Note:** All stats are displayed on a local web dashboard in your browser at `http://localhost:5000`. No data is sent to any external server; everything runs entirely on your own machine.

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/Sarim78/CoreStatus.git
cd CoreStatus
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
CoreStatus/
├── static/
│   └── style.css       # Stylesheet
├── templates/
│   └── index.html      # Frontend dashboard (HTML + CSS + JS)
├── app.py              # Flask backend + psutil metrics
├── requirements.txt    # Python dependencies
└── README.md
```

---

## 🔌 API Endpoint

**`GET /api/stats`** — returns all current system metrics as JSON.

> **Note:** No JSON file is needed. Flask generates this response live from your machine's stats every time the frontend calls this endpoint. You can preview it directly at `http://localhost:5000/api/stats` while the app is running. All stats are also displayed visually on the dashboard at `http://localhost:5000` in your browser.
```json
{
  "cpu": { "total": 14.2, "per_core": [10.0, 18.4, 12.1, 16.0], "count": 4 },
  "ram": { "percent": 62.5, "used_gb": 10.0, "total_gb": 16.0, "available_gb": 6.0 },
  "disk": { "percent": 55.3, "used_gb": 275.0, "total_gb": 500.0, "free_gb": 225.0 },
  "network": { "bytes_sent_mb": 1024.5, "bytes_recv_mb": 3210.2 },
  "system": { "uptime": "1 day, 4:32:10", "timestamp": "14:22:05" }
}
```

*(Values above are examples, your actual machine's real-time stats will appear here)*

---

## 🛠️ Tech Stack
| Layer     | Tech                        |
|-----------|-----------------------------|
| Backend   | Python, Flask               |
| Metrics   | psutil                      |
| Frontend  | Vanilla HTML/CSS/JS         |
| Fonts     | Share Tech Mono, Rajdhani   |

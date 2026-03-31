from flask import Flask, jsonify, render_template
import psutil
import datetime

app = Flask(__name__)

# Returns CPU usage as total percentage and per-core breakdown
def get_cpu_stats():
    return {
        "total": psutil.cpu_percent(interval=1),
        "per_core": psutil.cpu_percent(interval=1, percpu=True),
        "count": psutil.cpu_count()
    }

# Returns RAM usage including used, total, and available in GB
def get_ram_stats():
    ram = psutil.virtual_memory()

    return {
        "percent": ram.percent,
        "used_gb": round(ram.used / (1024 ** 3), 1),
        "total_gb": round(ram.total / (1024 ** 3), 1),
        "available_gb": round(ram.available / (1024 ** 3), 1)
    }

# Returns disk usage for root partition including used, free, and total in GB
def get_disk_stats():
    disk = psutil.disk_usage('/')

    return {
        "percent": disk.percent,
        "used_gb": round(disk.used / (1024 ** 3), 1),
        "total_gb": round(disk.total / (1024 ** 3), 1),
        "free_gb": round(disk.free / (1024 ** 3), 1)
    }

# Returns network I/O including total bytes sent and received in MB
def get_network_stats():
    net = psutil.net_io_counters()

    return {
        "bytes_sent_mb": round(net.bytes_sent / (1024 ** 2), 1),
        "bytes_recv_mb": round(net.bytes_recv / (1024 ** 2), 1)
    }

# Returns system uptime and current timestamp
def get_system_stats():
    boot_time = psutil.boot_time()
    
    uptime_seconds = datetime.datetime.now().timestamp() - boot_time
    uptime = str(datetime.timedelta(seconds=int(uptime_seconds)))
    return {
        "uptime": uptime,
        "timestamp": datetime.datetime.now().strftime("%H:%M:%S")
    }

# Bundles all stat functions into one dictionary to send to the frontend
def get_all_stats():
    return {
        "cpu": get_cpu_stats(),
        "ram": get_ram_stats(),
        "disk": get_disk_stats(),
        "network": get_network_stats(),
        "system": get_system_stats()
    }

# Route that serves the main dashboard HTML page
@app.route("/")
def index():
    return render_template("index.html")

# API route that returns all system stats as JSON (called every 2s by the frontend)
@app.route("/api/stats")
def stats():
    return jsonify(get_all_stats())

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify, render_template
import psutil
import datetime

app = Flask(__name__)

# Returns CPU usage as total percentage and per-core breakdown
def get_cpu_stats():
    
    pass

# Returns RAM usage including used, total, and available in GB
def get_ram_stats():

    pass

# Returns disk usage for root partition including used, free, and total in GB
def get_disk_stats():

    pass

# Returns network I/O including total bytes sent and received in MB
def get_network_stats():

    pass

# Returns system uptime and current timestamp
def get_system_stats():

    pass

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
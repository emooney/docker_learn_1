from flask import Flask, render_template
import psutil
import platform
import os

app = Flask(__name__)

def get_system_info():
    # CPU Information
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    
    # Memory Information
    memory = psutil.virtual_memory()
    memory_total = f"{memory.total / (1024 ** 3):.2f} GB"
    memory_used = f"{memory.used / (1024 ** 3):.2f} GB"
    memory_percent = memory.percent
    
    # Disk Information
    disk = psutil.disk_usage('/')
    disk_total = f"{disk.total / (1024 ** 3):.2f} GB"
    disk_used = f"{disk.used / (1024 ** 3):.2f} GB"
    disk_percent = disk.percent
    
    return {
        'cpu_percent': cpu_percent,
        'cpu_count': cpu_count,
        'memory_total': memory_total,
        'memory_used': memory_used,
        'memory_percent': memory_percent,
        'disk_total': disk_total,
        'disk_used': disk_used,
        'disk_percent': disk_percent,
        'platform': platform.platform(),
        'hostname': platform.node()
    }

@app.route('/')
def index():
    system_info = get_system_info()
    return render_template('index.html', info=system_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/env python3

import os
import shutil
import json
from pathlib import Path
from datetime import datetime
import platform
import random

script_dir = Path(__file__).resolve().parent

config_path = script_dir / "config.json"

width = shutil.get_terminal_size((80, 20)).columns
flower_count = max(1, width // 2)

with config_path.open("r", encoding="utf-8") as f:
    config = json.load(f)


translations = {
    "en": {
        "title": "New Terminal",
        "system_info": "System Information",
        "date": "Date",
        "time": "Time",
        "system": "System",
        "kernel": "Kernel",
        "directory": "Directory",
        "uptime": "Uptime",
        "disk": "Disk",
        "free": "Free",
        "total": "Total"
    },
    "es": {
        "title": "Nueva Terminal",
        "system_info": "Información del sistema",
        "date": "Fecha",
        "time": "Hora",
        "system": "Sistema",
        "kernel": "Núcleo",
        "directory": "Directorio",
        "uptime": "Tiempo de actividad",
        "disk": "Disco",
        "free": "Libre",
        "total": "Total"

    }
}

language = config.get("language", "en")
if language == "es":
    file_path = Path(__file__).resolve().parent / "quotes_es.txt"
if language == "en":
    file_path = Path(__file__).resolve().parent / "quotes_en.txt"

with file_path.open(encoding="utf-8") as f:
    quotes = [line.strip() for line in f if line.strip()]

t = translations.get(language, translations["en"])

show_date = config.get("date", "yes").lower() == "yes"
show_time = config.get("time", "yes").lower() == "yes"
show_system = config.get("system", "yes").lower() == "yes"
show_kernel = config.get("kernel", "yes").lower() == "yes"
show_directory = config.get("directory", "yes").lower() == "yes"
show_uptime = config.get("uptime", "yes").lower() == "yes"
show_disk_usage = config.get("disk_usage", "yes").lower() == "yes"
show_title = config.get("title", "yes").lower() == "yes"
show_quotes = config.get("quotes", "yes").lower() == "yes"

if show_title:
    print(f"{'🌸' * flower_count}\n{t['title']:^{width}}\n{'🌸' * flower_count}\n")
if show_quotes:
    print(quotes[random.randint(0, len(quotes) - 1)])
    print()
if show_date or show_time or show_system or show_kernel or show_directory or show_uptime or show_disk_usage:
    print(f"🖥️ {t['system_info']}:")
if show_date:
    print(f"    📅 {t['date']}: {datetime.now().strftime('%d/%m/%Y ')}")
if show_time:
    print(f"    🕙 {t['time']}: {datetime.now().strftime('%H:%M:%S')}")
if show_system:
    print(f"    💻 {t['system']}: {platform.system()} {platform.release()}")
if show_kernel:
    print(f"    🐧 {t['kernel']}: {platform.version().split()[0]}")
if show_directory:
    print(f"    📂 {t['directory']}: {os.getcwd()}")
if show_uptime:
    try:
        uptime = os.popen("uptime -p").read().strip()
        print(f"    ⏳ {t['uptime']}: {uptime}")
    except:
        pass
if show_disk_usage:
    use = shutil.disk_usage("/")
    print(f"\n    💾 {t['disk']}:")
    print(f"          {t['free']}: {use.free // (1024**3)} GB")
    print(f"          {t['total']}: {use.total // (1024**3)} GB")

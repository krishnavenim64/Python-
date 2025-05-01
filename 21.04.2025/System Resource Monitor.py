Import psutil



Print(f”CPU Usage: {psutil.cpu_percent()}%”)

Print(f”Memory Usage: {psutil.virtual_memory().percent}%”)

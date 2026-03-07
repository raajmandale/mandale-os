from datetime import datetime
def log(message):
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {message}")

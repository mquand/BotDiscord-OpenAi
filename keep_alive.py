from flask import Flask
import threading
import os

app = Flask('')

@app.route('/')
def home():
    return "Bot đang chạy trên Render!"

def run():
    port = int(os.environ.get("PORT", 10000))  # Render sẽ set PORT tự động
    app.run(host='0.0.0.0', port=port)         # Quan trọng: host phải là 0.0.0.0

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

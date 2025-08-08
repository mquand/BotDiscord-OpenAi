from flask import Flask
import threading
import os

app = Flask('')

@app.route('/')
def home():
    return "Bot đang chạy trên Render!"

def run():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

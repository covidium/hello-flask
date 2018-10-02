
import os
from flask import Flask
app = Flask(__name__)

host_ip = '0.0.0.0'

@app.route("/")
def hello():
    return "Hi all! I'm Ad and Leo"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
app.run(host=host_ip, port=port)

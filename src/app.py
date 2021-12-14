import datetime
import platform
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def challenge1():
    return {
      "timestamp": datetime.datetime.now(),
      "hostname": platform.node(),
      "engine": platform.python_version(),
      "visitor ip": request.remote_addr
    }

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

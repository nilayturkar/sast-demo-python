import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/run')
def run_command():
    cmd = request.args.get("cmd")
    os.system(cmd)  # ⚠️ Vulnerable: Command Injection
    return "Command executed: " + cmd

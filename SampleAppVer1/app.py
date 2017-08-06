from flask import Flask, render_template, request
import socket
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html', hostname=socket.gethostname())


if __name__ == "__main__":
    app.run('0.0.0.0')

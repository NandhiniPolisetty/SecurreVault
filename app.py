
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>SecureVault</title>
        <style>
            body {
                background: #0f172a;
                color: white;
                text-align: center;
                font-family: Arial;
                padding: 100px 20px;
            }
            h1 { color: #38bdf8; }
        </style>
    </head>
    <body>
        <h1>SecureVault</h1>
        <h2>Smart Document Access Control System</h2>
        <p>Secure Every Document. Control Every Access.</p>
        <p>Welcome to SecureVault!</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()

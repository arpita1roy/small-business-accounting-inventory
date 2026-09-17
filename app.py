from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Small Business Accounting & Inventory Management System</h1>
    <p>Application is under development.</p>
    <p>Inventory and accounting modules coming soon.</p>
    """


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template


app = Flask(__name__)


# @app.route("/")
# def home():
#     return render_template("index.html")

@app.route("/")
def get_short_essays_screen():
    return render_template("short_essays.html")


@app.route("/mcq")
def get_mcq_screen():
    return render_template("mcq_3.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8004)
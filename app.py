from flask import Flask, request, render_template
from translation import convert_to_ottoman, convert_to_turkish

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def translate():
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        direction = request.form["direction"]

        if direction == "to_ottoman":
            result = " ".join([convert_to_ottoman(word) for word in text.split()])
        else:
            result = " ".join([convert_to_turkish(word) for word in text.split()])
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

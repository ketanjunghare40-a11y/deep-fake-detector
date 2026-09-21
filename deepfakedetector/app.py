from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "/tmp"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    confidence = None
    image = None

    if request.method == "POST":

        file = request.files["image"]

        if file:

            path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

            file.save(path)

            # Demo result (not real AI)
            prediction = "Real Image"
            confidence = "95"

            image = path

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        image=image
    )


if __name__ == "__main__":
    app.run()
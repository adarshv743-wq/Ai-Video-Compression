from flask import Flask, render_template, request
import os
import uuid

from video_processor import process_video


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route("/process", methods=["POST"])
def process():

    if "video" not in request.files:

        return render_template(
            "index.html",
            error="Please select a video."
        )

    video = request.files["video"]

    if video.filename == "":

        return render_template(
            "index.html",
            error="No video selected."
        )

    extension = os.path.splitext(
        video.filename
    )[1]

    filename = str(uuid.uuid4()) + extension

    input_path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    video.save(input_path)

    try:

        result = process_video(
            input_path,
            OUTPUT_FOLDER
        )

        return render_template(
            "index.html",
            result=result
        )

    except Exception as e:

        return render_template(
            "index.html",
            error=str(e)
        )


if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )
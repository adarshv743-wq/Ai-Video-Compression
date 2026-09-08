import cv2
import os
import numpy as np


def calculate_psnr(original, processed):

    original = original.astype(np.float32)
    processed = processed.astype(np.float32)

    mse = np.mean(
        (original - processed) ** 2
    )

    if mse == 0:
        return 100.0

    psnr = 10 * np.log10(
        (255 ** 2) / mse
    )

    return float(psnr)


def compress_frame(frame):

    # Encode frame as JPEG with low quality
    encode_param = [
        int(cv2.IMWRITE_JPEG_QUALITY),
        35
    ]

    success, encoded = cv2.imencode(
        ".jpg",
        frame,
        encode_param
    )

    if not success:
        return frame

    compressed = cv2.imdecode(
        encoded,
        cv2.IMREAD_COLOR
    )

    return compressed


def enhance_frame(frame):

    # Lightweight AI-inspired filtering stage.
    # Can later be replaced by a CNN/DnCNN model.

    denoised = cv2.fastNlMeansDenoisingColored(
        frame,
        None,
        5,
        5,
        7,
        21
    )

    # Sharpening
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    enhanced = cv2.filter2D(
        denoised,
        -1,
        kernel
    )

    return enhanced


def process_video(
    input_path,
    output_folder
):

    cap = cv2.VideoCapture(
        input_path
    )

    if not cap.isOpened():

        raise Exception(
            "Unable to open video."
        )

    fps = cap.get(
        cv2.CAP_PROP_FPS
    )

    width = int(
        cap.get(
            cv2.CAP_PROP_FRAME_WIDTH
        )
    )

    height = int(
        cap.get(
            cv2.CAP_PROP_FRAME_HEIGHT
        )
    )

    total_frames = int(
        cap.get(
            cv2.CAP_PROP_FRAME_COUNT
        )
    )

    output_name = (
        "enhanced_video_"
        + os.path.basename(input_path)
    )

    output_path = os.path.join(
        output_folder,
        output_name
    )

    fourcc = cv2.VideoWriter_fourcc(
        *"mp4v"
    )

    writer = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width, height)
    )

    total_psnr = 0

    processed_frames = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # Simulate compression
        compressed = compress_frame(
            frame
        )

        # AI/DL-style enhancement
        enhanced = enhance_frame(
            compressed
        )

        # Quality measurement
        psnr = calculate_psnr(
            frame,
            enhanced
        )

        total_psnr += psnr

        processed_frames += 1

        writer.write(
            enhanced
        )

        # Limit processing for demonstration
        # Remove this limit for full video processing.
        if processed_frames >= 300:
            break

    cap.release()
    writer.release()

    if processed_frames == 0:

        raise Exception(
            "No video frames found."
        )

    average_psnr = (
        total_psnr /
        processed_frames
    )

    return {

        "output_video":
            output_path,

        "frames":
            processed_frames,

        "fps":
            round(fps, 2),

        "resolution":
            f"{width} x {height}",

        "psnr":
            round(average_psnr, 2)
    }
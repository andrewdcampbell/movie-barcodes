# USAGE: python barcode.py -video VIDEO [-u]

import os
import time
import argparse
import cv2
import numpy as np

OUT_WIDTH = 2560
OUT_HEIGHT = 1280

# In compressed mode, each frame is resized into a 1xSAMPLE_HEIGHT vector.
# SAMPLE_HEIGHT should be at most the input height and at least 1 (which
# is equivalent to uniform mode). Smaller values yield smoother results.
SAMPLE_HEIGHT = 8

def generate_barcode():
    cap = cv2.VideoCapture(VIDEO)
    TOTAL_FRAMES = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # sample at most 8*OUT_WIDTH frames
    NTH_FRAME = max(1, int(TOTAL_FRAMES / OUT_WIDTH / 8))
    print("Sampling every {} frame(s); {} total frames"
        .format(NTH_FRAME, TOTAL_FRAMES))

    counter, avg_cols = 0, []
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        if counter % NTH_FRAME == 0:
            if not UNIFORM_COLS:
                avg_cols.append(cv2.resize(frame, (1, SAMPLE_HEIGHT)))
            else:
                avg_cols.append(np.array([[np.mean(frame, axis=(0, 1))]]))
            print("{}%".format(np.round(counter/TOTAL_FRAMES * 100, 2)), 
                end="\r", flush=True)
        counter += 1

    cap.release()
    concatenated = np.concatenate(avg_cols, axis=1)
    print("Resizing {} frames to {}".format(concatenated.shape[1], OUT_WIDTH))
    barcode = cv2.resize(concatenated, (OUT_WIDTH, OUT_HEIGHT))
    cv2.imwrite(OUT_NAME, barcode)

if __name__ == "__main__":
    start_time = time.time()
    ap = argparse.ArgumentParser()
    ap.add_argument("-video", help="Path to video file", required=True)
    ap.add_argument("-u", help="Use uniform color columns", action='store_true')
    args = vars(ap.parse_args())
    VIDEO, UNIFORM_COLS = args["video"], args["u"]
    OUT_NAME = os.path.splitext(os.path.basename(VIDEO))[0] + "_barcode.jpg"

    generate_barcode()

    elapsed_time = time.time() - start_time
    print("Time elapsed: {}"
        .format(time.strftime("%H:%M:%S", time.gmtime(elapsed_time))))

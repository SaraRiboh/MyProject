import cv2
from ultralytics import YOLO
import time

def detect_objects_in_video(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    model_path = "last.pt"
    print("Loading model...")
    start_time = time.time()
    model = YOLO(model_path)
    load_time = time.time() - start_time
    print(f"Model loaded in {load_time:.2f} seconds.")

    threshold = 0.2
    frame_count_with_objects = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video.")
            break

        results = model(frame)[0]

        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result

            if score > threshold:
                frame_count_with_objects += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return frame_count_with_objects

# קריאה לפונקציה והדפסת מספר הפריימים עם אובייקטים
frame_count_with_objects = detect_objects_in_video("D:\\Users\\שרי\\Desktop\\r\\WIN_20240526_13_55_34_Pro.mp4")
print(f"Number of frames with objects: {frame_count_with_objects}")
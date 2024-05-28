import cv2
from ultralytics import YOLO
import time



def record_video(output_file, cap):
    # מקבלים את רזולוציית הוידאו מהקאפ
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # אתחול אובייקט עבור ההקלטה
    out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'XVID'), 20.0, (frame_width, frame_height))

    # קריאה ראשונה מהמצלמה
    ret, frame = cap.read()

    # בדיקה שהפריים נקראו תקין
    if not ret:
        print("Error: Could not read frame from camera.")
        return

    while True:
        # כתיבת הפריים לקובץ הוידאו
        out.write(frame)

        # קריאת הפריים הבאים מהמצלמה
        ret, frame = cap.read()

        # בדיקה שהפריים נקראו תקין
        if not ret:
            print("Error: Could not read frame from camera.")
            break

        # תהליך עיבוד הפריים כאן אם נדרש

        # הצגת הפריים בחלון
        cv2.imshow('Recording', frame)

        # בדיקה אם המשתמש לחץ על מקש 'q' לסיום ההקלטה
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # סיום ושחרור משאבים
    out.release()
    cv2.destroyAllWindows()

# פתיחת המצלמה
cap = cv2.VideoCapture(0)

# בדיקה שהמצלמה נפתחה תקין
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    # התחלת הקלטת הוידאו
    record_video("output.MOV", cap)

    # שחרור משאבים
    cap.release()

#record_video("output.MOV", cap)

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
            return frame_count_with_objects

    cap.release()
    cv2.destroyAllWindows()



# קריאה לפונקציה והדפסת מספר הפריימים עם אובייקטים
frame_count_with_objects= detect_objects_in_video("D:\\Users\\שרי\\Desktop\\a\\WIN_20240528_19_01_22_Pro.mp4")

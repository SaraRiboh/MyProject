
from packeg import *
from feels import *


counter = 0


# חישוב תכונות
features = extract_feature('D:\\Users\\שרי\\Desktop\\FullProjectSARI\\20240415-173029.wav', mfcc=True, chroma=True, mel=True)
# חיזוי רגש
predicted_emotion = model.predict(features)
# פירוש התוצאה
emotion_label = predicted_emotion[0]
print(f"Predicted emotion: {emotion_label}")



    # פונקציה לקליטת שמע והצגתו
def listen_and_print(person,i,choice):

    # יצירת מזהה דיבור
    recognizer = sr.Recognizer()

    while True:
        # קבלת קלט שמע
        with sr.Microphone() as source:
            audio = recognizer.listen(source)


        # ניסיון זיהוי דיבור
        try:
            text = recognizer.recognize_google(audio)
            print(f"אמרת: {text}")
            if choice==1:
              if not text == person[i]:
                print("תגיד את האמת בבקשה!")
                user_response = text  # תשובת המשתמש הנכונה תכנס לתוך הקלט הזה
              else:
                print("אמת")
                pyautogui.press('q')
                break


            elif choice==2:
                if  text == person[i]:
                    print("תגיד שקר בבקשה!")
                    user_response = text  # תשובת המשתמש הנכונה תכנס לתוך הקלט הזה
                else:
                    print("נהדר")
                    pyautogui.press('q')
                    break

        except sr.UnknownValueError:
            print("לא זיהיתי את מה שאמרת")
        except sr.RequestError:
            print("שגיאה בעת התחברות לשירות זיהוי הדיבור")





# פונקציה להצגת מצלמה
def show_camera():
    # יצירת אובייקט לכידת וידאו
    cap = cv2.VideoCapture(0)
    # לולאה אינסופית עד לחיצה על q
    while True:
        # קריאת פריים
        ret, frame = cap.read()
        # נצטרך לטעון את המודל שאימנו YOLO
        #   כל פעם בזמן אמת המצלמה לוכדת פריימים כל שניה - נרצה לשלוח למודל פריים -
        # והמודל מחזיר לי אם נגע או לא (יחזיר באינדקסים)
        # אם המודל החזיר נגע ששזה נגיד האינדקס 0 אז נעשה לו ספירה מונה ++
        # שומרים בתוך משתנה את מספר הנגיעות למדדים בסוף
        # את המשתנה הזה נחזיר את מספר הנגיעות לפונקציה   fun_truth_check()

        # הצגת הפריים
        cv2.imshow('מצלמה', frame)

        # קבלת קלט מהמשתמש
        key = cv2.waitKey(1) & 0xFF

        # יציאה מהלולאה בעת לחיצה על q
        if key == ord('q'):
            break
        #return מספר נגיעות

    # שחרור משאבי המצלמה
    cap.release()
    cv2.destroyAllWindows()








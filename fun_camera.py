
from packeg import *







    # פונקציה לקליטת שמע והצגתו
def listen_and_print():


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


        except sr.UnknownValueError:
            print("לא זיהיתי את מה שאמרת")
        except sr.RequestError:
            print("שגיאה בעת התחברות לשירות זיהוי הדיבור")







listen_and_print()






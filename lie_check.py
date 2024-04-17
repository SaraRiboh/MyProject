
from packeg import *
from fun_camera import *


#בדיקה על 3 שאלות השקר



person = ["David","Levy","Jerusalem"]

def fun_lie_check(choice):

    Blood_Pressure = random.randint(160, 179)
    Pulse_Pressure = random.randint(190, 200)

    for i in range(3):

        engine = pyttsx3.init()

        question = input("בוחן יקר אנא הכנס שאלה לשאול את הנבחן")

        engine.say(question)
        engine.runAndWait()

        print("עכשיו תפתח מצלמה ועל הנבחן לענות תשובה")

        # יצירת תהליך נפרד עבור קליטת שמע
        thread = threading.Thread(target = listen_and_print, args=(person, i))
        thread.start()
        # הפעלת פונקציית המצלמה
        #num = show_camera()# שחוזר מספר נגיעות מהYOLO

        show_camera()

        # המתנה לסיום תהליך קליטת השמע
        thread.join()




from real_test import *
from packeg import *
from fun_camera import *





#בדיקה על שאלת השקרq
sentence = "my name is Sarah"
numLie=0
def fun_lie_check(choice1):

    Blood_Pressure2 = random.randint(160, 179)
    Pulse_Pressure2 = random.randint(190, 200)



    engine = pyttsx3.init()



    print("עכשיו תפתח מצלמה ועל הנבחן לענות שקר על השאלה")

    # יצירת תהליך נפרד עבור קליטת שמע
    audio_queue = queue.Queue()
    thread = threading.Thread(target = listen_and_print, args=(sentence,choice1, audio_queue))
    thread.start()
    # הפעלת פונקציית המצלמה
    #numLie = show_camera()# שחוזר מספר נגיעות מהYOLO

    show_camera()
    # המתנה לסיום תהליך קליטת השמע
    thread.join()

    audio1 = audio_queue.get()
    raw_audio = audio1.get_raw_data()
    audio2 = bytes(raw_audio)
    with wave.open('output_audio.wav', 'wb') as audio_file:
         audio_file.setnchannels(1)
         audio_file.setsampwidth(2)
         audio_file.setframerate(44100)
         audio_file.writeframes(audio2)
    # חישוב תכונות
    features = extract_feature('output_audio.wav', mfcc=True, chroma=True, mel=True)
    # חיזוי רגש
    predicted_emotion = model.predict(features)
    # פירוש התוצאה
    emotion_label = predicted_emotion[0]

    print("השלב השלישי הוא הבחינה האמיתית")
    read_file_to_array(f'D:\\Users\\שרי\\Desktop\\FullProjectSARI\\percents.txt')
    choice3 = 3
    fun_real_test(choice3)

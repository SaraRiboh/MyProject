
from real_test import *
from packeg import *
from fun_camera import *






#בדיקה על שאלת השקרq
sentence = "my name is Sarah"
numLie=0
sum2=0
def fun_lie_check(choice1,sum):

    Blood_Pressure2 = random.randint(160, 179)
    Pulse_Pressure2 = random.randint(190, 200)

    question = input("בוחן יקר אנא הכנס שאלה לשאול את הנבחן,אם אינך חפץ לשאול הקש A")

    while (question != 'A'):
        engine = pyttsx3.init()
        engine.say(question)
        print("עכשיו תפתח מצלמה ועל הנבחן לענות שקר על השאלה")
        engine.runAndWait()

        # יצירת תהליך נפרד עבור קליטת שמע
        audio_queue = queue.Queue()
        thread = threading.Thread(target=listen_and_print, args=(sentence, choice, audio_queue))
        thread.start()
        # הפעלת פונקציית המצלמה
        # numTruth = show_camera()# שחוזר מספר נגיעות מהYOLO
        show_camera()

        # המתנה לסיום
        thread.join()

        if not text == sentence:
            mone = mone + 1

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
        emotion_label2 = predicted_emotion[0]
        print(emotion_label2)
        if text == sentence:
            Truth_touch_arr.append(numTruth)
            if emotion_label2 == observed_emotions[1]:
                Truth_feels_arr[1] = int(Truth_feels_arr[1]) + 1
            else:
                Truth_feels_arr[0] = int(Truth_feels_arr[0]) + 1
        else:
            lie_touch_arr.append(numTruth)
            if emotion_label2 == observed_emotions[1]:
                lie_feels_arr[1] = int(lie_feels_arr[1]) + 1
            else:
                lie_feels_arr[0] = int(lie_feels_arr[0]) + 1

    for i in range(mone):
        sum2 += lie_touch_arr[i]
    sum2 /= mone
    if (lie_feels_arr[0] > lie_feels_arr[1]):
        lie_emotion = lie_feels_arr[0]
    else:
        lie_emotion = lie_feels_arr[1]


    print("השלב השלישי הוא הבחינה האמיתית")
    read_file_to_array(f'D:\\Users\\שרי\\Desktop\\FullProjectSARI\\percents.txt')
    choice3 = 3
    fun_real_test(choice3,emotion_label2,sum)

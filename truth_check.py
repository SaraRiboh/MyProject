
from packeg import *
from fun_camera import *
from  lie_check import  *




#בדיקה על  שאלת האמת


sentence =["my name is Sarah","20","Brown","Israel","Jerusalem"]
numTruth=0
mone=0
sum=0
Truth_feels_arr=[0,0]
lie_feels_arr=[0,0]
Truth_touch_arr=[]
lie_touch_arr=[]

def fun_truth_check(choice):

    Blood_Pressure1 = random.randint(140, 159)
    Pulse_Pressure1 = random.randint(170, 189)
    print("השלב הראשון הוא בדיקת האמת")

    question = input("בוחן יקר אנא הכנס שאלה לשאול את הנבחן,אם אינך חפץ לשאול הקש A")

    while (question != 'A' and i<5):
       i=i+1
       if  text == sentence[i]:
           mone=mone+1
           Truth_touch_arr.append(numTruth)
           if emotion_label1 == observed_emotions[1]:
               Truth_feels_arr[1] = int(Truth_feels_arr[1]) + 1
           else:
               Truth_feels_arr[0] = int(Truth_feels_arr[0]) + 1




       else:
           lie_touch_arr.append(numTruth)
           if emotion_label1 == observed_emotions[1]:
                lie_feels_arr[1] = int(lie_feels_arr[1]) + 1
           else:
                lie_feels_arr[0] = int(lie_feels_arr[0]) + 1




    for i in range(mone):
        sum+=Truth_touch_arr[i]
    sum/=mone
    if(Truth_feels_arr[0]>Truth_feels_arr[1]):
       true_emotion=Truth_feels_arr[0]
    else:
        true_emotion = Truth_feels_arr[1]
























from random import random
from feelsModel import observed_emotions
import random


Blood_Pressure1_Low=160
Blood_Pressure1_High=179
Pulse_Pressure1_Low=190
Pulse_Pressure1_High=200
Blood_Pressure1_arr=[]
Pulse_Pressure1_arr=[]
Blood_Pressure2_arr=[]
Pulse_Pressure2_arr=[]
lie_feels_arr=[0,0]
Truth_touch_arr=[]
res=[]
percents=[]
moneT=0
moneF=0
len=4
sum=0
a=0
b=0
c=0

def fun_a1():
    global sum,moneT, a, c, b


    a = 1
    moneT += 1
    Blood_Pressure1 = random.randint(140, 159)
    Pulse_Pressure1 = random.randint(170, 189)
    Blood_Pressure1_arr.append(Blood_Pressure1)
    Pulse_Pressure1_arr.append(Pulse_Pressure1)

def fun_a0():
    a = 0
    global moneF
    moneF += 1
    Blood_Pressure2 = random.randint(160, 179)
    Pulse_Pressure2 = random.randint(190, 200)
    Blood_Pressure2_arr.append(Blood_Pressure2)
    Pulse_Pressure2_arr.append(Pulse_Pressure2)

def fun_b1():
    b = 1
    moneF += 1
    Blood_Pressure2 = random.randint(160, 179)
    Pulse_Pressure2 = random.randint(190, 200)
    Blood_Pressure2_arr.append(Blood_Pressure2)
    Pulse_Pressure2_arr.append(Pulse_Pressure2)

def fun_b0():
    b = 0
    moneT += 1
    Blood_Pressure1 = random.randint(140, 159)
    Pulse_Pressure1 = random.randint(170, 189)
    Blood_Pressure1_arr.append(Blood_Pressure1)
    Pulse_Pressure1_arr.append(Pulse_Pressure1)

def fun_c():
    c = 1
    Blood()
    Pulse()


def check_touches_in_face(frame_count_with_objects):
   s= true_data()
   res.append((frame_count_with_objects>s))

#בדיקת רגש בקול
def checkSentiment(emotion_label,lie_emotion):
    res.append((emotion_label == lie_emotion))

def Blood():
    blood_Pressure3 = random.randint(140, 179)
    res.append((blood_Pressure3>Blood_Pressure1_Low and blood_Pressure3<=Blood_Pressure1_High))

def Pulse():
    Pulse_Pressure2 = random.randint(170, 200)
    res.append((Pulse_Pressure2>Pulse_Pressure1_Low and Pulse_Pressure2<=Pulse_Pressure1_High))

def true_data():
    for i in range(moneT):
        sum += Truth_touch_arr[i]
    sum /= moneT
    return sum

def false_data():
    if (lie_feels_arr[0] > lie_feels_arr[1]):
        lie_emotion = observed_emotions[0]
    else:
        lie_emotion = observed_emotions[1]
    return lie_emotion



def read_file_to_array(filename,arr:list):
  with open(filename, 'r') as file:
    for line in file:
      arr.append(line.rstrip())



def fun_result():
    result = 0
    for i in range(len):
        result += int(percents[i]) * int(res[i])
    return result
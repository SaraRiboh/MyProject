from random import random

from feelsModel import observed_emotions
from real_test import *


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
sum=0
a=0
b=0
c=0

def fun_a1():
    global sum,moneT, moneF, a, c, b


    a = 1
    moneT += 1
    Blood_Pressure1 = random.randint(140, 159)
    Pulse_Pressure1 = random.randint(170, 189)
    Blood_Pressure1_arr.append(Blood_Pressure1)
    Pulse_Pressure1_arr.append(Pulse_Pressure1)

def fun_a0():
    a = 0
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


def check_touches_in_face(sum):
    res.append((num>sum))

#בדיקת רגש בקול
def checkSentiment(emotion_label1):
    res.append((emotion_label == emotion_label))

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


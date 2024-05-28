

from packeg import *




len=4

def read_file_to_array(filename):
  with open(filename, 'r') as file:
    for line in file:
      percents.append(line.rstrip())








        result=0
        for i in range(len):
            result+=int(percents[i])*int(res[i])
        str_p = str(result)
        print("הנבחן שיקר בוודאות של "+str_p+"%")
        question = input("בוחן יקר אנא הכנס שאלה לשאול את הנבחן,אם אינך חפץ לשאול הקש A")


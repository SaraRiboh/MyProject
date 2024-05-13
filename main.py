

from truth_check import *


def main():
    while True:
        print("תפריט פעולות")
        print("הקש 1 להתחלת הבחינה")
        print("הקש 2 להסבר על האפליקציה")
        print("הקש 3 ליציאה")


        try:  # במקרה והמשתמש הזין קלט לא חוקי כמו רווח
            choice = int(input())
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue  # ask for input again

        if choice > 4 or choice < 1:
            print('Please select a valid choice')
        if choice == 1:
            fun_truth_check(choice)
        if choice == 3:
            exit()



main()









from truth_check import *
from  lie_check import  *

def main():
    while True:
        print("תפריט פעולות")
        print("הקש 1 כדי לעבור למבחן הסטטיסטיקה של 3 שאלות האמת")
        print("הקש 2 כדי לעבור למבחן של 3 שאלות השקר")
        print("הקש 3 להציג את הסטטיסטיקות ")
        print("הקש 4 לתחילת הבחינה")
        print("הקש 5 לצאת מהתפריט")


        try:  # במקרה והמשתמש הזין קלט לא חוקי כמו רווח
            choice = int(input())
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue  # ask for input again

        if choice > 4 or choice < 1:
            print('Please select a valid choice')
        if choice == 1:
            fun_truth_check(choice)
        if choice == 2:
             fun_lie_check(choice)
        # if choice == 3:
        #     show()
        # if choice == 4:
        #     start()
        if choice == 5:
            exit()



main()







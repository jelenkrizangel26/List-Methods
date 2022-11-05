#Write a python program that do the following:

#- display the initial content of the array
#- display a menu of options
#- allow user to select item in the menu (check if valid)
#- perform the selected option (you may prompt additional info to user when need)
#- display the resulting values of the array


#Note: 
#- The program has an array variable containing 10 random numbers
#- You may add other options and features
#- Your program should be uploaded to github before 1:30pm
#- Record a demo presenting your program
#- Send the demo directly to my messenger

import sys

list1 = [10, 40, 20, 60, 30, 50, 70, 80, 100, 200]
border = ("\33[35m*************************************************************\33[0m\n")

def intro():
    print("\n Good day, Welcome to List Manipulation!")
    print("\n So here's our list for today.\n")

def list():
    print("Array:",list1)
    print(border)

def menu():
    list2 = ["1 -> Add an element" ,"2 -> Reverse the list", "3 -> Find the smallest element" ,"4 -> Sum of the elements" ,"5 -> Arrange in ascending order" ,"6 -> Arrange in descending order"]
    print("Instructions: Pick number from 1 to 6 to tell what you want. \n Menu:")
    print(list2[0])
    print(list2[1])
    print(list2[2])
    print(list2[3])
    print(list2[4])
    print(list2[5])

def start():

    while True:
        print(border)
        pick = input("What do you want to do ? \n>>")
        if pick == '1':
            print(border)
            string = "\n\t              \33[3m\33[1m\33[35m Starting!\33[0m" 
            print(string)
            number = input("Enter the element you want to add: ")
            list1.append(number)
            print("\n Here's your result:")
            print("Array:",list1)

            again()

        elif pick == '2':
            print(border)
            string = "\n\t              \33[3m\33[1m\33[35m Starting!\33[0m" 
            print(string)
            print("\n Here's your result:")
            list1.reverse()
            print("Array:",list1)

            again()

        elif pick == '3':
            string = "\n\t              \33[3m\33[1m\33[35m Innitializing...\33[0m" 
            print(string)
            print("\n Here's your result:")
            smallest = min(list1)
            print(smallest)

            again()

        elif pick == '4':
            string = "\n\t              \33[3m\33[1m\33[35m Innitializing...\33[0m" 
            print(string)
            total = sum(list1)
            print("Here's the sum of all of the elements")
            print(total)

            again()

        elif pick == '5':
            string = "\n\t              \33[3m\33[1m\33[35m Innitializing...\33[0m" 
            print(string)
            list1.sort()
            print("\n Here's your new array:")
            print("Array:",list1)

            again()

        elif pick == '6':
            string = "\n\t              \33[3m\33[1m\33[35m Innitializing...\33[0m" 
            print(string)
            list1.sort(reverse=True)
            print("\n Here's your new array:")
            print(list1)

            again()

def main():
    intro()
    list()
    menu()
    start()

def again():
    answer = input("\nTry again y/n. \n>> ")
    if answer.lower() == "y":
        return main()
    elif answer.lower() == "n":
        print("\t          \33[3m\33[35mThanks for playing! ")
        sys.exit("\n")
    else: 
        print("\t\33[35m\33[1m        Sorry your input must be a y or n!\33[0m")
        return again()
        
main()

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

def intro():
    print("Good day, Welcome to List Manipulation!")
    print("So here's our list for today.\n")

def list():
    border = ("\33[35m******************************************\33[0m\n")
    list1 = [10, 40, 20, 60, 30, 50, 70, 80, 100, 200]
    print(border)
    print(list1)
    print(border)

def menu():
    list2 = ["1 -> Add an element" ,"2 -> Insert an element", "3 -> Modify an element" ,"4 -> Delete an element" ,"5 -> Arrange in ascending order" ,"6 -> Arrange in descending order"]
    print(list2[0])
    print(list2[1])
    print(list2[2])
    print(list2[3])
    print(list2[4])
    print(list2[5])
    
    


intro()
list()
menu()
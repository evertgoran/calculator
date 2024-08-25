#importing that which is needed
from tkinter import *
import ast

#create a new instance of the main window of the application
root = Tk()

#set up and initialize the index for the Entry widget
i = 0

#A function which displays in the Entry widget the pressed numbers
def get_number(num):
    global i
    display.insert(i, num)
    i = i + 1


#A function which displays in the Entry widget the pressed operators
def get_operator(operator):
    global i
    display.insert(i, operator)
    i = i + len(operator)



#A function which removes everything in the Entry widget
def all_clear():
    global i
    display.delete(0, END)
    i = 0

#A function which calculates whatever mathematical expression entered in the Entry widget and which uses the ast-module
# to parse and calculate
def calculate():
    try:
        entire_string = display.get()
        node = ast.parse(entire_string, mode="eval")
        result = eval(compile(node, '<string>','eval'))
        all_clear()
        display.insert(0, result)
    except Exception:
        display.insert(0, "Error")

#A function which removes the last index in the Entry widget
def undo():
    global i
    if i >= 1:
        i = (i - 1)
        display.delete(i)



#Determines the font size as well as make the Entry widgets height bigger
font_size = ('Arial', 40)

#Creates the Entry widget and stores it
display = Entry(root, width=13, font=font_size)

#Positions the Entry widget according to the stated below
display.grid(row=1, columnspan=24)

#A list of the total numbers, except 0, to be used in the for loop below
numbers = [1,2,3,4,5,6,7,8,9]

#A counter for the for loop to loop through so that all the numbers gets their turn to be added to a button
counter = 0

#A for loop which creates the buttons (except for 0) in a 3x3 layout
#For each iteration of the loop above their will be 3 iterations, so in total 9 iterations
for x in range(3):
    for y in range(3):
        #Each iteration, the unique number is stored into this variable which below is used to give each button a unique
        #number
        button_text = numbers[counter]
        #Each iteration, a button is created with the features and characteristics below
        button = Button(root, width=8, height=8, text=button_text, command=lambda text=button_text: get_number(text))
        #Each iteration, the button created above is positioned onto the window using the grid layout
        button.grid(row=x+2, column=y)
        # Each iteration, the counter is updated so that no previous number is put on a new button
        counter +=1

#Creating the button 0 with the characteristics below
button = Button(root, width=8, height=8, text="0", command=lambda: get_number(0))

#Positioning the button created above onto the main window using the grid layout
button.grid(row=5, column=1)

#Creating the button "C" with the characteristics below and positioning it on the main window using a grid layout
Button(root, width=8, height=8, text="C", command=lambda: all_clear()).grid(row=4, column=5)

#Creating the button "=" with the characteristics below and positioning it on the main window using a grid layout
Button(root, width=8, height=8, text="=", command=calculate).grid(row=5, column=2)

#Creating the button "Delete" with the characteristics below and positioning it on the main window using a grid layout
Button(root, width=8, height=8, text="Delete", command=undo).grid(row=5, column=0)

#Creating a list of possible operations
operations = ["+", "-", "", "/", "3.14", "%", "*", "**2"]

#Another counter to be used in the for loop below which ensures that each button gets the correct text
count = 0

#A for loop for the operator buttons in a 4x3 layout
#For each of the 4 iterations (rows), 3 columns will be created
for x in range(4):
    for y in range(3):
        #If count is less than operations (less than 😎 then a button will be created for each iteration
        if count < len(operations):
            button = Button(root, width=8, height=8, text=operations[count], command=lambda text=operations[count]: get_operator(text))

            #The count is updated to ensure that each button gets the correct text
            count += 1

            #Each button of each iteration gets positioned on the main window in grid layout
            #By 'x+2' and 'y+3' we ensure that these buttons do not sit in the same place as the "number" buttons
            button.grid(row=x+2, column=y+3)



#The main loop which ensures that the window does not automatically close at the end of program
root.mainloop()
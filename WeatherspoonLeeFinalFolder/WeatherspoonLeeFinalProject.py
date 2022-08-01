from cProfile import label
from sqlite3 import Row
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
root = Tk()
#Never figure out how to remove this without losing Ico File access in program
iconic = "C:/Users/wowza/Documents/Ivy Tech/SDEV140/Wk  (8)/Assignment docs/WeatherspoonLeeFinalFolder/Media/faviconFinal.ico"
root.iconbitmap(iconic)
#These set the toppings
TOPPINGS = ["Pepperoni","Sausage","Extra cheese","Peppers","Mushrooms","Onion","Tomato"]#list of toppings
checkYes = []#Which toppings are checked
checkofToppings = []#Here I am creating the list that will be parallel to toppings to filter out unchecked toppings
crustDiam = [("small","small"),("medium","medium"),("large","large")]
def totalCost(topAmount, pickDel, pieSize):
    topCost = float(topAmount * 1)
    if pickDel == "Delivery":#There is a cost for delivery
        delCost = 6.50
    else:#Nothing for pickup
        delCost = 0.0
    if pieSize == "large":#7 for a large
        pieCost = 7.0
    elif pieSize == "medium":#5 for a medium
        pieCost = 5.0
    else:#3 for a small
        pieCost = 3.0
    absTotal = round(topCost + delCost + pieCost, 2)
    return f"The Total Cost is {absTotal}!"
#This will write the items in the cart to a txt file called receipt
def receiptWriteTop():#Writing checked toppings to receipt
    print("Start receptWriteTop")#Notes that the function is running
    # PizzaService = PickOrDeliver()
    checkSet = {}#gets each topping into a list with an on or off value indicating selection
    for topping, markCheck in zip(TOPPINGS, checkofToppings):
        checkSet[topping]=markCheck.get()
        print("Running if statement")
        if checkSet[topping] == 1:# If the topping is marked as yes then the program labels it in the window
            checkYes.append(topping)
            #Trying to at least print the selected topping values here in the first window
            print("Try label")
            selectedTop = Label(root,text=topping)#Testing label remove after fstring text is created
            print("After Label")
        else:
            print("Not selected")
def cartWind():
    win1button['state']='disabled'
    receiptWriteTop()
    print("pizzaCart")
    pizzaCart = Toplevel()
    pizzaCart.iconbitmap(iconic)
    PizzaService = PickOrDeliver()
    pizzaSizing = pizzaSize()
    topCount = len(checkYes)
    sumTotal = totalCost(topCount, PizzaService,pizzaSizing)
    servType = Label(pizzaCart, text=PizzaService).grid(row=0, column=0)
    sizeType = Label(pizzaCart, text=pizzaSizing).grid(row=1, column=0)
    print("Going into the for loop")
    y=0
    for topping in checkYes:# Prints label
        y+=1
        topped = Label(pizzaCart, text=topping).grid(row=0,column=y)
        print("During the for loop")
    print("After Going into the forloop")
    tagPrice = Label(pizzaCart, text=sumTotal).grid(row=3, column=0)
    button_quit = Button(pizzaCart, text="EXIT PROGRAM", command=root.quit).grid()
def PickOrDeliver():
    choice = PoD.get()
    if choice == 1:
        print("inside 1st bit of if statement")
        HereGo = "Pickup"#label(pizzaCart,text="Pickup").grid()
    elif choice == 2:
        print("inside 2nd bit of if statement")
        HereGo = "Delivery"#label(pizzaCart,text="Delivery").grid()
    else:
        HereGo = "Error in radiobutton"
        #print("ERROR IN RADIOBUTTON")
        
    return HereGo #messagebox.showinfo('Pizza Service: ', f'you selected {HereGo}.')
def pizzaSize():
    choice = Diam.get()
    if choice == 1:
        print("inside 1st bit of if statement")
        pizzaDiameter = "Small"#label(pizzaCart,text="Pickup").grid()
    elif choice == 2:
        print("inside 2nd bit of if statement")
        pizzaDiameter = "Medium"#label(pizzaCart,text="Delivery").grid()
    elif choice == 3:
        print("Inside of 3rd statement")
        pizzaDiameter = "Large"
    else:
        pizzaDiameter = "Error in radiobutton"
        #print("ERROR IN RADIOBUTTON")
    return pizzaDiameter

#fishers.jpg
#Pickup or Delivery
PoD = IntVar()
PoD.set(2)
#Image attributes
imageOfPizza = Image.open("C:/Users/wowza/Documents/Ivy Tech/SDEV140/Wk  (8)/Assignment docs/WeatherspoonLeeFinalFolder/Media/fishers.jpg")
photo = ImageTk.PhotoImage(imageOfPizza)
imgLable = Label(root, image=photo).grid(row=0, column=1)#Displays pizza image
#End image stuff
Radiobutton(root, text="Pickup", variable=PoD, value=1, command=PickOrDeliver).grid()
Radiobutton(root, text="Delivery", variable=PoD, value=2, command=PickOrDeliver).grid()
#Size for pizza
Diam = IntVar()
Diam.set(3)
#uses a for loop to create a check list of toppings
Radiobutton(root, text="Small", variable=Diam, value=1,command=pizzaSize).grid()
Radiobutton(root, text="Medium", variable=Diam, value=2,command=pizzaSize).grid()
Radiobutton(root, text="Large", variable=Diam, value=3,command=pizzaSize).grid()
for topName in TOPPINGS: #uses a for loop to create a check list of toppings
    pizzaTop = IntVar()
    toppingNames = Checkbutton(root, text= topName, variable=pizzaTop) 
    toppingNames.deselect()
    toppingNames.grid()
    checkofToppings.append(pizzaTop)



#Open window 1(the Cart)
win1button= Button(root, text="View Cart",  command= cartWind, pady=5).grid()#Opens the cart to view all currentlyselected Items
button_quit = Button(root, text="EXIT PROGRAM", command=root.quit).grid()#Exit Button
    



root.mainloop()
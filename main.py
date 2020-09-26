#Trần Bá Khoa - 43.01.104.081
from tkinter import *
def calculate(event):
 v=int(tx.get());
 value1 = v * 2 * 3.14
 value2 = v * v * 3.14
 print(value1)
 print(value2)
 updateDisplay1(value1);
 updateDisplay2(value2);
	
def updateDisplay1(myString):
	displayVariable1.set(myString)

def updateDisplay2(myString):
	displayVariable2.set(myString)

root=Tk()
root.geometry("800x400")
root.title("Chu Vi - Diện Tích Hình Tròn")
root.grid()

lb=Label(root, text="Nhập bán kính", font=("TimeNewRoman",20))
lb.pack()
tx= Entry(root, width=30, font=("TimeNewRoman",20))
tx.pack()

button_1 = Button(root, text="Tính toán", font=("TimeNewRoman",30,"bold"), bg="cyan", fg="red") 
button_1.bind("<Button-1>", calculate)
button_1.pack()

lb=Label(root, text="Chu vi", font=("TimeNewRoman",20))
lb.pack()

displayVariable1 = StringVar()
displayLabel1 = Label(root, textvariable=displayVariable1, font=("TimeNewRoman",20))
displayLabel1.pack()

lb=Label(root, text="Diện tích", font=("TimeNewRoman",20))
lb.pack()

displayVariable2 = StringVar()
displayLabel2 = Label(root, textvariable=displayVariable2, font=("TimeNewRoman",20))
displayLabel2.pack()

root.mainloop()
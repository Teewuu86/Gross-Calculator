from tkinter import *

root = Tk()
root.title("Gross Calculator")



def HourlyRate():
    hourly = float(empWage.get())
    return hourly

def NormalHours():
    hrs = float(empHours.get())
    if hrs <= 40:
        return hrs
    else:
        return 40

def OverTime():
    OT = 0
    hrsOver =  float(empHours.get()) - 40
    if hrsOver >0:
        OT += hrsOver
        return OT
    else:
        return 0
    
def OverTimeWage():
    otWage = float(empWage.get()) * 1.5
    if OverTime() > 0:
        return otWage
    else:
        return 0
    
def calculate ():
    Name = "Employee: " + empFirst.get() + " " + empLast.get() +"\n"
    otHours = 0
    worked = 0
    worked += NormalHours()
    otHours = OverTime()
    wage = HourlyRate
    totalPay = round((OverTime() * OverTimeWage()) + (NormalHours() * HourlyRate()),2)
    labelGross.config(text = Name + "Gross Pay: " + str(totalPay))

def Clear():
    empFirst.delete(0,END)
    empLast.delete(0,END)
    empHours.delete(0,END)
    empWage.delete(0,END)
    labelGross.config(text = "")

def Save():
    fileName = str(empFirst.get()) + str(empLast.get())+".txt"
    file = open(fileName, "w")
    file.write("Employee: " + str(empFirst.get())+ " " + str(empLast.get()) + "\n")
    file.write("Hours Worked: " + str(empHours.get())+ "_hrs" + "\n")
    file.write("Hours of OT: " + str(OverTime())+ "_hrs" + "\n")
    file.write("Hourly Wage: " + str(empWage.get())+ "_per/hr" + "\n")
    file.write("Gross Pay: " + "$"+ str(round((OverTime() * OverTimeWage()) + (NormalHours() * HourlyRate()),2)) + "\n")
    file.close()
    



#Define Entry Fields
empFirst = Entry(root, text = "First Name")
empFirst.grid(row = 0, column = 1, columnspan = 3)

empLast = Entry(root, text = "Last Name")
empLast.grid(row =1, column = 1, columnspan = 3)

empHours = Entry(root, text = "Hours Worked")
empHours.grid(row = 2, column =1, columnspan = 3)

empWage = Entry(root, text = "Hourly Wage")
empWage.grid(row=3, column=1, columnspan = 3)

#Define Buttons
button_Calculate = Button(root, text = "Calculate", command = calculate)
button_Calculate.grid(row=4, column = 0,padx = 2, pady = 3)

button_Save = Button(root, text = "Save To File", command = Save)
button_Save.grid(row = 4, column = 1,padx = 2, pady = 3)

button_Clear = Button(root, text ="Clear", command = Clear)
button_Clear.grid(row = 4, column = 2,padx = 2, pady = 3)

button_Close = Button(root, text = "Close", command = root.destroy)
button_Close.grid(row =4, column= 3 ,padx = 2, pady = 3)

#Define Labels
labelFirst = Label(root, text = "First Name")
labelFirst.grid(row = 0, column = 0)

labelLast = Label(root, text = "Last Name")
labelLast.grid(row = 1, column = 0)

labelHours = Label(root, text = "Hours Worked")
labelHours.grid(row = 2, column = 0)

labelWage = Label(root, text = "Hourly Wage")
labelWage.grid(row = 3, column = 0)

labelGross = Label(root)
labelGross.grid(row = 5, column = 1, columnspan = 3)

root.mainloop

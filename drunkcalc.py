from Tkinter import *
import Backend

window = Tk()

window.title("BAC Calculator")
window.geometry("300x300")

name = Label(window, text="Name")
E1 = Entry(window, bd = 3)

weight = Label(window, text="Weight")
E2 = Entry(window, bd = 3)

drink = Label(window, text="Number of Drinks")
E3 = Entry(window, bd = 3)

hours = Label(window, text="Hours")
E4 = Entry(window, bd = 3)

gender = Label(window, text="Gender")
# E5 = Entry(window, bd = 3)
variable = StringVar(window)
variable.set("Male") # default value
E5 = OptionMenu(window, variable, "Male", "Female")

string1 = ''
string2 = ''
string3 = ''
string4 = ''
string5 = ''

def getInfo():
    string1 = E1.get()
    string2 = E2.get()
    string3 = E3.get()
    string4 = E4.get()
    string5 = variable.get()
    person = Backend.Alcoholic(string1, string2, string3, string4, string5)
    results = person.calc_bac()
    print results

submit = Button(window, text ="Submit", command = getInfo)

name.pack()
E1.pack()
weight.pack()
E2.pack()
drink.pack()
E3.pack()
hours.pack()
E4.pack()
gender.pack()
E5.pack()
submit.pack(side = BOTTOM)
window.mainloop()
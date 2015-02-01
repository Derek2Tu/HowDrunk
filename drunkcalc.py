import time
import Tkinter


window = Tkinter.Tk()

window.title("BAC Calculator")
window.geometry("300x300")

lbl = Tkinter.Label(window, text="Calculate Your BAC")
ent = Tkinter.Entry(window)
btn = Tkinter.Button(window, text="GO!")

lbl.pack()
ent.pack()
btn.pack()

window.mainloop()

"""
print "Welcome to the alcohol calculator"
print " " 
time.sleep(1)

def getInfo():
		weight = raw_input("Enter your weight in pounds: ")
		#drink_type = raw_input("Enter the type of drink you've had: ")
		drink_quant = raw_input("Enter the number of (standard size) drink amounts you've had: ")
		print "Thank you for the information. Currently processing how drunk you are..."
		#drunkCalculator()
		time.sleep(3)
		print " "
		print "Since you weigh " + weight + " pounds, and you've had " + drink_quant + " drinks, your blood alcohol level is: "

getInfo()

"""
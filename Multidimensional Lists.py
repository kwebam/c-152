from tkinter import *
root = Tk()

root.title("Multidimensional Lists")
root.geometry("500x500")

label = Label(root)

arrays_1d = ["Jonh", "James", "Thomesbond"]
print( arrays_1d[0] )

arrays_2d = [["Jonh", "A"], ["James", "B"], ["Thomesbond", "C"]]
print( arrays_2d[0][1] )

arrays_3d = [["Jonh", "A+", "Excellent"], ["James", "A", "Very Good"], ["Thomesbond", "B", "Good"]]
print( arrays_3d[0][0][2] )

def report():
    label['text'] = arrays_3d[0][1][0] + "got grade " + arrays_3d[0][1][1] + "and he is doing " + arrays_3d[0][1][2]

btn = Button(root, text="Show Report", command=report)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

label.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()
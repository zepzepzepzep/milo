import tkinter as tk
from tkinter import Canvas, Frame, filedialog, Text 
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():

    for widget in Frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("Executables", "*.exe"), ("All", "*.*"))) 
    
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(Frame, text= app, bg="green")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

def closeapp():
    for j in Frame:
        apps.clear()    

Canvas = tk.Canvas(root, height=500, width=600, bg='#000000')
Canvas.pack()

Frame = tk.Frame(root, bg="white")
Frame.place(relheight=0.7, relwidth=0.8, relx=0.1, rely=0.1)

closeApp = tk.Button(root, text="Close App", padx=5, pady=2, bg="green")
closeApp.pack()

openFile = tk.Button(root, text="Open App", padx=10, pady=5, fg="white", bg="#000000", command=addApp)
openFile.pack()

runFile = tk.Button(root, text="Run App", padx=10, pady=5, fg="white", bg="#000000", command=runApps)
runFile.pack()

for app in apps:
    label = tk.Label(Frame, text=app) 
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ', ')

from tkinter import *
from tkinter import Tk, scrolledtext, Menu, filedialog, messagebox
from pathlib import Path
import os
import webbrowser

# Default filename at start 
file = Path("Untitled.txt")

# All the command functions [newFile, openFile, saveFile, saveAs, exitRoot, preferences, about, and help]
# Ever messy (saveFile and saveAs are basically the same function)
def newFile():
	if len(text.get('1.0', END+'-1c')) > 0:
		if messagebox.askyesno("Save?", "Do you wish to save?"):
			saveAs()
		
		else:
			text.delete('1.0', END)
	
	root.title(os.path.basename("Untitled.txt") + " - LeakeyEditor - A simple Text Editor")

def openFile():
	file = filedialog.askopenfile(parent=root, title='Select a text file', filetypes=(("Text file", "*.txt"), ("All files", "*.*")))
	
	root.title(os.path.basename(file.name) + " - LeakeyEditor - A simple Text Editor")
	text.delete('1.0', END)
	
	if file != None:
		contents = file.read()
		text.insert(1.0, contents)	
		
def saveFile():
    if not file.exists():
        saveAs()
        return
    data = workArea.get(0.0, END)
    with open(file, "w") as f:
        f.write(data)
	
def saveAs():
	file = filedialog.asksaveasfile(mode='w')

	if file != None:
		data = text.get(1.0, END+'-1c')
		file.write(data)
		file.close()

def exitRoot():
	if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
		root.destroy()

def preferences():
	label = messagebox.showinfo("Preferences", "Coming Soon...")
		
def about():
	label = messagebox.showinfo("About", "LeakeyEditor is a simple text editor scripted in Python, along with the Tkinter module. This application was scripted by ChampionLeake")

def help():
	label = messagebox.showinfo("Help", "If you're having trouble with anything in this program or want to submit a bug, go to https://github.com/ChampionLeake/LeakeyEditor/issues")

# Main properties of the program itself
root = Tk()
root.resizable(False, False)
root.title("LeakeyEditor - A simple Text Editor")

text = scrolledtext.ScrolledText(root)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=exitRoot)
menubar.add_cascade(label="File", menu=filemenu)

settingsmenu = Menu(menubar)
settingsmenu.add_command(label="Preferences...", command=preferences)

menubar.add_cascade(label="Settings", menu=settingsmenu)
menubar.add_cascade(label="About", command=about)
menubar.add_cascade(label="Help", command=help)

root.config(menu=menubar)
root.mainloop()
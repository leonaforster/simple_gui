import tkinter as tk

#----------------------------- define button behaviour: --------------------------------#

root = tk.Tk()

def start_reading():
    print("analyzing images...")






#window properties:
root.title("demo")
root.configure(background="yellow")
#works, mostly deals with rescaling LATER:
#root.minsize(900, 500)
#root.maxsize(500, 500)
#works, this one here sets the actual size IN THE BEGINNING, optionally the position as well:
#the string we pass here has its own, funky format. 
root.geometry("2850x1350")

#here we essentially determine the size of each row and column through the "weight" parameter (only integers btw)
#caveat: weight only distributes free spaces after a first distribution pass where each widget was assigned its minimal necessary space
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(1, weight=1)

#we use multiple grids inside multiple frames, so we can split different columns differently, octree style
#one grid for each column -> left and right col.
#here we make two empty frame instances. we dont yet specify which column is left and which one is right. they dont differ in terms of placement so far
lc = tk.Frame(root)
rc = tk.Frame(root)

#If you ever struggle with labels not filling out, make sure both col and row configure are done correctly
lc.grid_rowconfigure(0, weight=4)#15
lc.grid_rowconfigure(1, weight=1)
#each of these rows will become a frame of its own later. but their size relaive to eachother must always be determined at the parent(!) level
rc.grid_rowconfigure(0, weight=5)#the weight 5 here even though it's 4 on the other side and the layout is symmetrical due to tkinter eccentricities
#which ones? Well, tkinter-widgets first get the minimal necessary size to fit their contents and only then does the weight-paramter distribute the free space
rc.grid_rowconfigure(1, weight=1)
lc.grid_columnconfigure(0, weight=1)
rc.grid_columnconfigure(0, weight=1)

#here is the point where the frame instances start to differ meaningfully, i.e. in a way that makes one left and the other right
lc.grid(row=0,column=0,sticky="nsew")
rc.grid(row=0,column=1,sticky="nsew")


"""l1=tk.Label(lc, text="mais dans le calme\n il est coupable de tout le bien qu’il ne fait pas.")"""
#finding a font that is actually supported is fairly tricky
#seriously, if the buttons and labels are a mess, it's probably because the font name is wrong and it wrecks the entire font-object creation
#thus your element will simply be initialized with default parameters, including size. That's why u can't resize it. 
"""l1.config(font=("liberation sans", 40),bg="cyan")
l1.grid(row=0,column=0,sticky="nsew")"""

#left column:
lcwindow=tk.Frame(lc)
lcbuttons=tk.Frame(lc)

#lc=left column, rc=right column
lcwindow.grid_rowconfigure(0, weight=1)
lcwindow.grid_columnconfigure(0, weight=1)
lcbuttons.grid_rowconfigure(0, weight=1)
lcbuttons.grid_columnconfigure(0, weight=1)
lcbuttons.grid_columnconfigure(1, weight=1)

lcwindow.grid(row=0,column=0,sticky="nsew")
lcbuttons.grid(row=1,column=0,sticky="nsew")

#a label with a photo
image=tk.PhotoImage(file="photo.png")
l1=tk.Label(lcwindow, image=image)
#l1=tk.Label(lc, text="mais dans le calme\n il est coupable de tout le bien qu’il ne fait pas.")
l1.config(font=("liberation sans", 40),bg="white")
l1.grid(row=0,column=0,sticky="nsew")


#here we make the next label
l2=tk.Label(lcbuttons, text="il est coupable de tout le bien\n qu'il ne fait pas.")
l2.config(font=("liberation sans", 40),bg="cyan")
l2.grid(row=0,column=0,sticky="nsew")

#a button in the left column
b=tk.Button(lcbuttons, text="Click")
b.config(font=("liberation sans", 40),bg="white")
b.grid(row=0,column=1,sticky="nsew")

#right column:
rcwindow = tk.Frame(rc)
rcbuttons = tk.Frame(rc)
rcwindow.grid(row=0,column=0,sticky="nsew")
rcbuttons.grid(row=1,column=0,sticky="nsew")
rcwindow.grid_rowconfigure(0, weight=1)#15
rcwindow.grid_columnconfigure(0, weight=30)
rcbuttons.grid_rowconfigure(0, weight=1)#15
rcbuttons.grid_columnconfigure(0, weight=1)

#here we create a canvas so we have something scrollable and call it "window"
window=tk.Canvas(rcwindow)
scrollbar=tk.Scrollbar(rcwindow,orient="vertical",command=window.yview)
window.configure(yscrollcommand=scrollbar.set)
window.config(bg="magenta")
window.grid(row=0,column=0,sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="nsew")
#but we also need to add this:
rcwindow.grid_columnconfigure(1, weight=1)

window.create_text(
    500,300,#200, 100,              # x, y position
    text="mais\n dans\n le\n calme\n\n\n\n il\n est\n coupable\n de\n tout\n le\n bien\n qu’il\n ne\n fait\n pas.",
    font=("liberation sans", 40),
    fill="black"
)



b1=tk.Button(rcbuttons, text="Undo\n Delete")
b1.config(font=("liberation sans", 40),bg="white")
#this is the type of line that actually adds new rows/columns:
b1.grid(row=0,column=0,sticky="nsew")

b2=tk.Button(rcbuttons, text="Delete")
b2.config(font=("liberation sans", 40),bg="white")
b2.grid(row=0,column=1,sticky="nsew")
rcbuttons.grid_columnconfigure(1, weight=1)

#Warning: we pass a function here without calling it! So "command=start_reading" not "command=start_reading()"
b3=tk.Button(rcbuttons, text="Start\n Reading", command=start_reading)
b3.config(font=("liberation sans", 40),bg="lime")
b3.grid(row=0,column=2,sticky="nsew")
rcbuttons.grid_columnconfigure(2, weight=1)


root.mainloop()


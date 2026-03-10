import tkinter as tk

root = tk.Tk()

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
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(1, weight=1)

#we use multiple grids inside multiple frames, so we can split different columns differently, octree style
#one grid for each column -> left and right col.
#here we make two empty frame instances. we dont yet specify which column is left and which one is right. they dont differ in terms of placement so far
lc = tk.Frame(root)
rc = tk.Frame(root)

#If you ever struggle with labels not filling out, make sure both col and row configure are done correctly
lc.grid_rowconfigure(0, weight=3)#15
rc.grid_rowconfigure(0, weight=1)
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

#a label
image = tk.PhotoImage(file="photo.png")
l1=tk.Label(lc, image=image)
#l1=tk.Label(lc, text="mais dans le calme\n il est coupable de tout le bien qu’il ne fait pas.")
l1.config(font=("liberation sans", 40),bg="white")
l1.grid(row=0,column=0,sticky="nsew")

#here we make the next label
l2=tk.Label(lc, text="il est coupable de tout le bien\n qu'il ne fait pas.")
l2.config(font=("liberation sans", 40),bg="cyan")
l2.grid(row=1,column=0,sticky="nsew")
#but we also need to add this:
lc.grid_rowconfigure(1, weight=1)


#here we make the next label
l3=tk.Label(rc, text="mais dans le calme\n il est coupable\n de tout le bien qu’il ne fait pas.")
l3.config(font=("liberation sans", 40),bg="magenta")
#this is the type of line that actually adds new rows/columns
l3.grid(row=0,column=0,sticky="nsew")


root.mainloop()

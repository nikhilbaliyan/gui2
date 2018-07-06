from tkinter import *
root = Tk()
d={"nikhil": 7300704200, "akash": 7300704300, "ankit": 7300704100, "unknown":7894561230}
sb=Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)
dbox=Listbox(root, yscrollcommand=sb.set)
for key in d:
   	dbox.insert(END, key )
   	dbox.pack(side=LEFT, fill=Y)
sb.configure(command=dbox.yview)
root.mainloop()

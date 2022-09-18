import tkinter as tk
root=tk.Tk()
# setting the windows size
root.geometry("600x400")
# declaring string variable
# for storing name and password
a = tk.StringVar()
b = tk.StringVar()
c = tk.StringVar()
d = tk.StringVar()
e = tk.StringVar()

bg = tk.PhotoImage(file = 'fun stuff/plop.png')
 
# Show image using label
label1 = tk.Label( root, image = bg)
label1.place(x = 0, y = 0)

# defining a function that will
# get the name and password and
# print them on thoe screen
def submit():
    first = a.get()
    last = b.get()
    email = c.get()
    aadhar = d.get()
    pin = e.get()
    print("The name is : "+ first.title() + " "+ last.title())
    print("The email is : "+ email)
    print("The Aadhar number : ", aadhar)
    print("The account pin set to : ", pin)
    
    a.set("")
    
    b.set("")
    c.set("")
    d.set("")
    e.set("")

p = tk.Label(root,text = "",bg = "#b5245f",fg = "white",font="Calibri").grid(row= 0,column=0)
a2 = tk.Label(root ,text = "First Name",bg = "#b5245f",fg = "white").grid(row = 1,column = 1)
b2 = tk.Label(root ,text = "Last Name",bg = "#b5245f",fg = "white").grid(row = 2,column = 1)
c2 = tk.Label(root ,text = "Email Id",bg = "#b5245f",fg = "white").grid(row = 3,column = 1)
d2 = tk.Label(root ,text = "Aadhar Number",bg = "#b5245f",fg = "white").grid(row = 4,column = 1)


e2 = tk.Label(root ,text = "set account pin",bg = "#b5245f",fg = "white").grid(row = 5,column = 1)

a1 = tk.Entry(root,textvariable= a).grid(row = 1,column = 2)
b1 = tk.Entry(root,textvariable= b).grid(row = 2,column = 2)
c1 = tk.Entry(root,textvariable= c).grid(row = 3,column = 2)
d1 = tk.Entry(root,textvariable= d).grid(row = 4,column = 2)
e1 = tk.Entry(root, textvariable= e, show = "*").grid(row = 5,column=2)

j = tk.Label(root,text = "",bg = "#b5245f",fg = "white").grid(row= 6,column=1)
sub_btn = tk.Button(root,text = "Submit",command = submit)

sub_btn.grid(row = 7,column=2)

root.mainloop()

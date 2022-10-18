####MENU

"""MENU:It is used to create all kinds of menus used by the application."""
from tkinter import *

import sqlite3


def d_triangle():
  
    canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
    canvas.pack(fill=BOTH, expand=1)
def d_square():
    
    canvas.create_line(55, 85, 155, 85, 155, 180, 55, 180,55,85)
    canvas.pack(fill=BOTH, expand=1)
def cle():
    canvas.delete("all")
    canvas.pack()


    #calling function Loginform
#def open_win():


def login():
    import sqlite3
    #getting form data
    uname=username.get()
    pwd=password.get()
    #applying empty validation
    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
    #open database
        conn = sqlite3.connect('student.db')
        #select query
        cursor = conn.execute('SELECT * from ADMIN2 where USERNAME="%s" and PASSWORD="%s"'%(uname,pwd))
        #fetch data
        if cursor.fetchone():
            message.set("Login success")
        else:
            message.set("Wrong username or password!!!")

def login_screen():
    global login_screen
    login_screen = Toplevel(root)

    global message
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    #Setting title of screen
    #setting height and width of screen
    login_screen.geometry("350x250")
    login_screen["bg"]="#1C2833"
    #declaring variable
    #Creating layout of login form
    Label(login_screen,width="300", text="Login From", bg="#0E6655",fg="white",font=("Arial",12,"bold")).pack()
    #Username Label
    Label(login_screen, text="Username * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=40)
    #Username textbox
    Entry(login_screen, textvariable=username,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=42)
    #Password Label
    Label(login_screen, text="Password * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=80)
    #Password textbox
    Entry(login_screen, textvariable=password ,show="*",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=82)
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=95,y=120)
    #Login button
    Button(login_screen, text="Login", width=10, height=1, command=login, bg="#0E6655",fg="white",font=("Arial",12,"bold")).place(x=125,y=170)

    login_screen.mainloop()
#Create a label
#STEP 5:
from tkinter import *
#import library
import sqlite3
#open databse
#defining login function
root = Tk()

menu = Menu(root)
root.config(menu=menu)

canvas = Canvas()
root.geometry("400x250+300+300")
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='1CMS')
filemenu.add_command(label='2CMS')
filemenu.add_command(label='3CMS')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

formatmenu = Menu(menu)
menu.add_cascade(label='Format', menu=formatmenu)
formatmenu.add_command(label='square',command = d_square)
formatmenu.add_command(label = 'triangle',command= d_triangle)
formatmenu.add_command(label = 'clear screen',command= cle)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Password and username',command=login_screen)


root.config(menu=menu)
root.mainloop()
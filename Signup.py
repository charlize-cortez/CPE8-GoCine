from tkinter import *
from tkinter import messagebox
import ast

import pymysql
window = Tk()
window.title('GoCine')
window.iconbitmap('logo.ico')
window.geometry('1200x673+80+10')
window.configure(bg="#944E63")
window.resizable(False, False)

frame = Frame(window, width=1200, height=673, bg="#944E63")
frame.place(x=0, y=0)

frame2 = Frame(window, width=600, height=473, bg="#B47B84")
frame2.place(x=315, y=100)

signup_label = Label(frame2, text="Sign up", bg='#B47B84', font=("Microsoft YaHei UI Light", 20, "bold"), fg="white")
signup_label.place(x=250, y=75)


###########Database
def signup():
    if user.get() == '' or code.get() == '' or conform_code.get() == '':
        messagebox.showerror('Error', 'All Fields are required')
    elif code.get() != conform_code.get():
        messagebox.showerror('Invalid', 'Passwords do not match')
    else:
        try:
            connection = pymysql.connect(
                host='localhost',
                user='root',
                password='1234',
                database='gocine_database'
            )
            cur = connection.cursor()
            cur.execute("SELECT * FROM employee_info WHERE username=%s", (user.get(),))
            row = cur.fetchone()

            if row is not None:
                messagebox.showerror("Error", "Username already exists")
                email.delete(0, 'end')
                code.delete(0, 'end')
                conform_code.delete(0, 'end')
            else:
                cur.execute(
                    "INSERT INTO employee_info (username, email) VALUES (%s, %s)",
                    (user.get(), code.get())
                )
                connection.commit()
                messagebox.showinfo("Success", "Registration successful")
                user.delete(0, 'end')
                email.delete(0, 'end')
                code.delete(0, 'end')
                conform_code.delete(0, 'end')

        except Exception as es:
            messagebox.showerror("Error", f"Error due to {str(es)}")
        finally:
            connection.close()


#########for Username
def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    if user.get() == '':
        user.insert(0, 'Enter your Username')


user_label = Label(frame2, text="Username:", bg='#B47B84', font=("Microsoft YaHei UI Light", 11, "bold"), fg="white")
user_label.place(x=100, y=150)

user = Entry(frame2, width=25, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 12))
user.place(x=250, y=150)
user.insert(0, 'Enter your Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)


###############

#########EMAIL
def on_enter(e):
    email.delete(0, 'end')


def on_leave(e):
    if email.get() == '':
        email.insert(0, 'Enter your Email')


email_label = Label(frame2, text="Email:", bg='#B47B84', font=("Microsoft YaHei UI Light", 11, "bold"), fg="white")
email_label.place(x=100, y=200)

email = Entry(frame2, width=25, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 12))
email.place(x=250, y=200)
email.insert(0, 'Enter your Email')
email.bind('<FocusIn>', on_enter)
email.bind('<FocusOut>', on_leave)


###############


#########For Password
def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    if code.get() == '':
        code.insert(0, 'Enter your Password')


pass_label = Label(frame2, text="Password:", bg='#B47B84', font=("Microsoft YaHei UI Light", 11, "bold"), fg="white")
pass_label.place(x=100, y=250)

code = Entry(frame2, width=25, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 12))
code.place(x=250, y=250)
code.insert(0, 'Enter your Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)


######################################


#########For Password
def on_enter(e):
    conform_code.delete(0, 'end')


def on_leave(e):
    if conform_code.get() == '':
        conform_code.insert(0, 'Confirm your Password')


conPass_label = Label(frame2, text="Re-enter:", bg='#B47B84', font=("Microsoft YaHei UI Light", 12, "bold"), fg="white")
conPass_label.place(x=100, y=300)

conform_code = Entry(frame2, width=25, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 12))
conform_code.place(x=250, y=300)
conform_code.insert(0, 'Confirm your Password')
conform_code.bind('<FocusIn>', on_enter)
conform_code.bind('<FocusOut>', on_leave)

#########button
Button(frame2, width=10, pady=7, text="Sign up", bg="white", fg="black", border=2, command=signup).place(x=275, y=350)

#########Button Signup
signin_label = Label(frame2, text="Already have an account?", bg='#B47B84',
                     font=("Microsoft YaHei UI Light", 10, "bold"), fg="black")
signin_label.place(x=200, y=400)
signin_button = Button(frame2, text="Login", width=6, border=0, bg="#B47B84", cursor="hand2", fg="white",
                       font=("Microsoft YaHei UI Light", 10, "bold"))
signin_button.place(x=380, y=397)

window.mainloop()

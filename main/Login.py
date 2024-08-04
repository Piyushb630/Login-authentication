import tkinter as tk
import customtkinter

users = {"admin": "password"}  # Initialize globally for access in both functions
customtkinter.set_appearance_mode('light')

def register():
    register_window = tk.Toplevel()
    register_window.geometry('400x300')
    register_window.title("Register")

    email_label = tk.Label(register_window, text="Enter your email id:")
    email_label.grid(row=0, column=0, padx=5, pady=5)

    email_textbox = tk.Entry(register_window)
    email_textbox.grid(row=0, column=1, padx=5, pady=5)


    username_label = tk.Label(register_window, text="Enter your username")
    username_label.grid(row=1, column=0, padx=5, pady=5)

    username_textbox = tk.Entry(register_window)
    username_textbox.grid(row=1, column=1, padx=5, pady=5)

    password_label = tk.Label(register_window, text="Enter password")
    password_label.grid(row=2, column=0, padx=5, pady=5)

    password_textbox = tk.Entry(register_window, show="*")
    password_textbox.grid(row=2, column=1, padx=5, pady=5)

    passwordverify_label = tk.Label(register_window, text="Re-enter your password")
    passwordverify_label.grid(row=3, column=0, padx=5, pady=5)

    passwordverify_textbox = tk.Entry(register_window, show="*")
    passwordverify_textbox.grid(row=3, column=1, padx=5, pady=5)

    register_button = tk.Button(register_window, text="Register", command=lambda: register_user(email_textbox.get(), username_textbox.get(), password_textbox.get(), passwordverify_textbox.get()))
    register_button.grid(row=4, column=1, padx=5, pady=5)


def register_user(email, username, password, passwordverify):
    if password == passwordverify:
        users[username] = password  # Update global users dictionary
        register_successful()
    else:
        print("Passwords do not match!")

def register_successful():
    register_successful_window = tk.Toplevel()
    register_successful_window.geometry('250x50')
    register_successful_window.title("Registration Successful")

    register_successful_label = tk.Label(register_successful_window, text="Registration is successful!")
    register_successful_label.pack()
    register_successful.after(5000, incorrect_window.destroy)

def thumbsup():
    thumbsup_window = tk.Toplevel()
    thumbsup_window.geometry('400x300')
    thumbsup_window.title("Thumbs Up!")
    thumbsup_label = tk.Label(thumbsup_window, text="Thank you for your feedback!❤️")
    thumbsup_label.pack()

def thumbsdown():
    thumbsdown_window = tk.Toplevel()
    thumbsdown_window.geometry('400x300')
    thumbsdown_window.title("Thumbs Down!")
    thumbsdown_label = tk.Label(thumbsdown_window, text="Thank you for your feedback!, will try to improve🤜🏻")
    thumbsdown_label.pack()


def login():
    username = username_textbox.get()
    password = password_textbox.get()

    if username in users and users[username] == password:
        print("Login successful!")

        inital_window = tk.Tk()
        inital_window.geometry('300x200')
        inital_window.title('Home Page')

        inital_window.configure(bg='white')
        inital_window.resizable(False, False)
        
        first = tk.Label(inital_window, text = "My first application")
        first.grid(row= 0,column=2)

        second = tk.Label(inital_window, text = "Give a thumps up")
        second.grid(row=1, column=2)

        button1 = tk.Button(inital_window, text = "👍🏻", command = thumbsup)
        button1.grid(row=2,column=1)

        button2 = tk.Button(inital_window, text = "👎🏻", command = thumbsdown)
        button2.grid(row=2, column=2)







    else:
        print("Invalid username or password")
        
        incorrect_window = tk.Tk()
        incorrect_window.geometry('300x100')
        incorrect_window.title('Incorrect')
        
        incorrect_label = tk.Label(incorrect_window, text = "Username or password is incorrect")
        incorrect_label.pack()

        incorrect_button = tk.Button(incorrect_window, text = "Retry",command=incorrect_window.destroy)
        incorrect_button.pack()


    

window = tk.Tk()
window.geometry('400x200')
window.title("Login Page")

window.resizable(False, False)

username_label = tk.Label(window, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)

username_textbox = tk.Entry(window)
username_textbox.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(window, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)

password_textbox = tk.Entry(window, show="*")
password_textbox.grid(row=1, column=1, padx=5, pady=5)

login_button = tk.Button(window, text="Login", command=login)
login_button.configure(bg="green")
  # Bind login function to the login button
login_button.grid(row=2, column=1, columnspan=2, padx=5, pady=5)


register_button = tk.Button(window, text="Register", command=register)
register_button.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

window.mainloop()
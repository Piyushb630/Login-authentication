Login authentication

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
        register_button = tk.Button(register_window, text="Register", command=lambda: register_user(email_textbox.get(), username_textbox.get(), password_textbox.get(), passwordverify_textbox.get(), register_window))
        register_button.grid(row=4, column=1, padx=5, pady=5)
    
    
    def register_user(email, username, password, passwordverify):
        if password == passwordverify:
            users[username] = password  # Update global users dictionary
            register_successful()
        else:
            print("Passwords do not match!")
    
    def register_successful():
        register_successful_window = tk.Toplevel()
        register_successful_window.geometry('400x300')
        register_successful_window.title("Registration Successful")
        register_successful_label = tk.Label(register_successful_window, text="Registration is successful!")
        register_successful_label.pack()
        register_successful.after(5000, incorrect_window.destroy)
    
    
    def login():
        username = username_textbox.get()
        password = password_textbox.get()
        if username in users and users[username] == password:
            print("Login successful!")
            inital_window = tk.Tk()
            inital_window.geometry('800x800')
            inital_window.title('Home Page')
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
    
    username_label = tk.Label(window, text="Username:")
    username_label.grid(row=0, column=0, padx=5, pady=5)
    
    username_textbox = tk.Entry(window)
    username_textbox.grid(row=0, column=1, padx=5, pady=5)
    
    password_label = tk.Label(window, text="Password:")
    password_label.grid(row=1, column=0, padx=5, pady=5)
    
    password_textbox = tk.Entry(window, show="*")
    password_textbox.grid(row=1, column=1, padx=5, pady=5)
    
    login_button = tk.Button(window, text="Login", command=login)  # Bind login function to the login button
    login_button.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
    
    register_button = tk.Button(window, text="Register", command=register)
    register_button.grid(row=3, column=1, columnspan=2, padx=5, pady=5)
    
    window.mainloop()

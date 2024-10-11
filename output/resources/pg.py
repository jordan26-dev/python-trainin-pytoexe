# Create a new Python file, e.g., login_form.py, and import the necessary libraries:

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk



# Set up the main window for the application:

root = tk.Tk()
root.title("Login Form")
root.geometry("300x350")

 
#logo
logo = Image.open("resources/images/login.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.pack()


# Create a function to handle the login logic:

def login():
    username = entry_username.get()
    password = entry_password.get()
    
   

    # Predefined username and password
    if username == "admin" and password == "password123":
        messagebox.showinfo("Access Granted", "Welcome!")               
    else:
        messagebox.showerror("Access Denied", "Invalid username or password.")
         
      
    # Create and place the labels and entry fields
   

        


# Create and place the labels and entry fields
label_username = tk.Label(root, text="Username")
label_username.pack(pady=5)

entry_username = tk.Entry(root, width=40)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Password")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show='*', width=40)
entry_password.pack(pady=5)

# Create and place the login button
button_login = tk.Button(root, text="Login", command=login, width=20)
button_login.pack(pady=20)


# Start the application
root.mainloop()


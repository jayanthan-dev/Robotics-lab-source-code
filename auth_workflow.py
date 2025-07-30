# gui_auth_workflow.py
import tkinter as tk
from tkinter import simpledialog, messagebox

# Predefined password
stored_password = "admin123"

# Initialize GUI root
root = tk.Tk()
root.withdraw()  # Hide main window

# Ask for username and password
username = simpledialog.askstring("User Authentication", "Enter your username:")
password = simpledialog.askstring("User Authentication", "Enter your password:", show='*')

# Check the password
if password == stored_password:
    messagebox.showinfo("Success", f"Welcome, {username}!")
else:
    messagebox.showerror("Failed", "Authentication Failed. Incorrect Password.")

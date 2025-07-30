import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Snack Ordering System")
root.geometry("400x400")
root.resizable(False, False)

# Title label
tk.Label(root, text="Snack Ordering System", font=("Arial", 16, "bold")).pack(pady=10)

# Frame for the form
form_frame = tk.Frame(root)
form_frame.pack(pady=10)

# User name entry
tk.Label(form_frame, text="Enter your name:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=10, pady=5)
name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, pady=5)

# Snack entries
snacks = {
    "Chips": tk.IntVar(),
    "Sandwich": tk.IntVar(),
    "Juice": tk.IntVar()
}

row_num = 1
for snack, var in snacks.items():
    tk.Label(form_frame, text=f"{snack} Quantity:", font=("Arial", 12)).grid(row=row_num, column=0, sticky="w", padx=10, pady=5)
    tk.Entry(form_frame, textvariable=var, width=10).grid(row=row_num, column=1, pady=5, sticky="w")
    row_num += 1

# Submit button logic
def submit_order():
    name = name_entry.get().strip()
    if not name:
        messagebox.showwarning("Input Error", "Please enter your name.")
        return

    total = sum(var.get() for var in snacks.values())
    summary = f"Order Summary for {name}:\n\n"
    for snack, var in snacks.items():
        qty = var.get()
        if qty > 0:
            summary += f"{snack}: {qty}\n"
    summary += f"\nTotal snacks ordered: {total}"

    messagebox.showinfo("Order Summary", summary)

# Clear button logic
def clear_form():
    name_entry.delete(0, tk.END)
    for var in snacks.values():
        var.set(0)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

tk.Button(button_frame, text="Submit Order", command=submit_order, width=15, bg="green", fg="white").grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Clear", command=clear_form, width=10, bg="red", fg="white").grid(row=0, column=1, padx=10)

# Run the application
root.mainloop()

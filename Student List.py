import tkinter as t
from tkinter import messagebox
import csv
import os

# File path (Changed to std.csv)
path = r"C:\Users\ADMIN\Desktop\CSV_files\std.csv"

# Initialize Window
r = t.Tk()
r.title("Student List")
r.geometry("800x800")
r.configure(bg="#f0f0f0")

# Title Heading
title = t.Label(r, text="Student List", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#004080", padx=10, pady=5)
title.pack(pady=10)

# Underline for Title
canvas = t.Canvas(r, width=250, height=2, bg="#004080", highlightthickness=0)
canvas.pack()

# Student Input Headings (Attractive Labels)
frame_input = t.Frame(r, bg="#f0f0f0")
frame_input.pack(pady=15)

t.Label(frame_input, text="Student Name", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="black").grid(row=0, column=0, sticky="w", padx=20)
e1 = t.Entry(frame_input, font=("Arial", 12), width=30)
e1.grid(row=1, column=0, padx=20, pady=(0, 10))

t.Label(frame_input, text="Roll Number", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="black").grid(row=0, column=1, sticky="w", padx=20)
e2 = t.Entry(frame_input, font=("Arial", 12), width=30)
e2.grid(row=1, column=1, padx=20, pady=(0, 10))

# Listbox Frame
frame = t.Frame(r)
frame.pack(pady=10)

# Scrollbar
scrollbar = t.Scrollbar(frame, orient=t.VERTICAL)

# Listbox with Header Row
lb = t.Listbox(frame, yscrollcommand=scrollbar.set, height=20, width=50, font=("Courier", 12, "bold"))
lb.pack(side=t.LEFT, fill=t.BOTH, expand=True)
scrollbar.config(command=lb.yview)
scrollbar.pack(side=t.RIGHT, fill=t.Y)

# Add Table Column Headers
lb.insert(t.END, f"{'Student Name':<30} | {'Roll Number':<15}")
lb.insert(t.END, "-" * 50)

# Function to Load Existing Students from CSV
def load_students():
    if os.path.exists(path):  # Check if file exists
        with open(path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Ensure the row is not empty
                    lb.insert(t.END, f"{row[0]:<30} | {row[1]:<15}")

# Function to Add Student
def add_std():
    name = e1.get().strip()
    roll_number = e2.get().strip()

    if name and roll_number:
        lb.insert(t.END, f"{name:<30} | {roll_number:<15}")  # Add to Listbox

        # Save to CSV
        with open(path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, roll_number])

        # Clear Input Fields
        e1.delete(0, t.END)
        e2.delete(0, t.END)
    else:
        messagebox.showwarning("Input Error", "Both Name and Roll Number are required!")

# Load students on startup
load_students()

# Add Student Button
btn = t.Button(r, text="Add Student", font=("Arial", 14, "bold"), bg="green", fg="white", padx=15, pady=5, command=add_std)
btn.pack(pady=10)

# Run the Application
r.mainloop()

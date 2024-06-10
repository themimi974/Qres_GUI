import tkinter as tk
from tkinter import messagebox
import pickle

def add_resolution():
    resolution = resolution_entry.get()
    if resolution:
        try:
            x, y = map(int, resolution.split('x'))
            resolutions.append((x, y))
            update_resolution_listbox()
            resolution_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Resolution added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid resolution format. Please use 'width x height' format (e.g., '1920x1080').")

def remove_resolution():
    try:
        index = resolution_listbox.curselection()[0]
        del resolutions[index]
        update_resolution_listbox()
        messagebox.showinfo("Success", "Resolution removed successfully!")
    except IndexError:
        messagebox.showerror("Error", "Please select a resolution to remove.")

def update_resolution_listbox():
    resolution_listbox.delete(0, tk.END)
    for resolution in resolutions:
        resolution_listbox.insert(tk.END, f"{resolution[0]}x{resolution[1]}")

def save_resolutions():
    with open('resolutions.pkl', 'wb') as file:
        pickle.dump(resolutions, file)
    messagebox.showinfo("Success", "Resolutions saved successfully!")

def load_resolutions():
    try:
        with open('resolutions.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "Resolutions file not found!")
        return []

def reset_resolutions():
    global resolutions
    resolutions = [
        (1920, 1080),
        (1440, 900),
        (1280, 720),
        (1024, 768)
    ]
    update_resolution_listbox()
    messagebox.showinfo("Success", "Resolutions reset to default!")

# Create main window
root = tk.Tk()
root.title("Resolution Manager")

# Load resolutions
resolutions = load_resolutions()

# Resolution Entry
resolution_entry_label = tk.Label(root, text="Add Resolution (e.g., 1920x1080):")
resolution_entry_label.grid(row=0, column=0, padx=5, pady=5)
resolution_entry = tk.Entry(root)
resolution_entry.grid(row=0, column=1, padx=5, pady=5)

# Add Resolution Button
add_resolution_button = tk.Button(root, text="Add Resolution", command=add_resolution)
add_resolution_button.grid(row=0, column=2, padx=5, pady=5)

# Resolution Listbox
resolution_listbox_label = tk.Label(root, text="Resolutions:")
resolution_listbox_label.grid(row=1, column=0, padx=5, pady=5)
resolution_listbox = tk.Listbox(root, width=20, height=10)
resolution_listbox.grid(row=1, column=1, padx=5, pady=5)
update_resolution_listbox()

# Remove Resolution Button
remove_resolution_button = tk.Button(root, text="Remove Resolution", command=remove_resolution)
remove_resolution_button.grid(row=1, column=2, padx=5, pady=5)

# Save Resolutions Button
save_resolutions_button = tk.Button(root, text="Save Resolutions", command=save_resolutions)
save_resolutions_button.grid(row=2, column=1, padx=5, pady=5)

# Reset Resolutions Button
reset_resolutions_button = tk.Button(root, text="Reset Resolutions", command=reset_resolutions)
reset_resolutions_button.grid(row=2, column=2, padx=5, pady=5)

root.mainloop()

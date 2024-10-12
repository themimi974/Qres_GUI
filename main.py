import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from screeninfo import get_monitors
import subprocess
import pickle

def set_resolution(x, y, refresh_rate=None):
    try:
        cmd = ['QRes.exe', '-x:' + str(x), '-y:' + str(y)]
        if refresh_rate:
            cmd.append('-r:' + str(refresh_rate))
        subprocess.run(cmd, shell=True)
        messagebox.showinfo("Success", f"Resolution set to {x}x{y}{' at ' + str(refresh_rate) + 'Hz' if refresh_rate else ''}!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def set_refresh_rate(refresh_rate):
    try:
        current_resolution = get_current_resolution()
        if current_resolution:
            set_resolution(current_resolution[0], current_resolution[1], refresh_rate)
        else:
            messagebox.showerror("Error", "Unable to determine current resolution.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while setting refresh rate: {str(e)}")

def switch_to_extended_mode():
    try:
        subprocess.run(['displayswitch.exe', '/extend'], shell=True)
        messagebox.showinfo("Success", "Switched to extended mode!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def switch_to_internal_mode():
    try:
        subprocess.run(['displayswitch.exe', '/internal'], shell=True)
        messagebox.showinfo("Success", "Switched to internal mode!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def get_current_resolution():
    try:
        monitor = get_monitors()[0]  # We assume there is only one monitor
        return monitor.width, monitor.height
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while fetching current resolution: {str(e)}")
        return None

def load_resolutions():
    try:
        with open('resolutions.pkl', 'rb') as file:
            resolutions = pickle.load(file)
        return resolutions
    except FileNotFoundError:
        messagebox.showerror("Error", "Resolutions file not found!")
        return []

def create_window():
    window = tk.Tk()
    window.title("Screen Layout Editor")
    window.configure(bg="#2b2b2b")  # Background color for dark theme

    def on_resolution_button_click(x, y, refresh_rate=None):
        set_resolution(x, y, refresh_rate)

    def on_extended_mode_button_click():
        switch_to_extended_mode()

    def on_internal_mode_button_click():
        switch_to_internal_mode()

    def on_refresh_rate_button_click(refresh_rate):
        set_refresh_rate(refresh_rate)

    resolutions = load_resolutions()

    def create_ctkbutton(*args, **kwargs):
        button = ctk.CTkButton(
            *args,
            **kwargs,
            fg_color="#3c3c3c",  # Button background color
            text_color="white"   # Button text color
        )
        return button

    for x, y in resolutions:
        button = create_ctkbutton(window, text=f"{x}x{y}", command=lambda x=x, y=y: on_resolution_button_click(x, y))
        button.pack(pady=5)

    extended_mode_button = create_ctkbutton(window, text="Extended Mode", command=on_extended_mode_button_click)
    extended_mode_button.pack(pady=5)

    internal_mode_button = create_ctkbutton(window, text="Internal Mode", command=on_internal_mode_button_click)
    internal_mode_button.pack(pady=5)

    refresh_rate_60_button = create_ctkbutton(window, text="Set to 60Hz", command=lambda: on_refresh_rate_button_click(60))
    refresh_rate_60_button.pack(pady=5)

    refresh_rate_120_button = create_ctkbutton(window, text="Set to 120Hz", command=lambda: on_refresh_rate_button_click(120))
    refresh_rate_120_button.pack(pady=5)

    refresh_rate_144_button = create_ctkbutton(window, text="Set to 144Hz", command=lambda: on_refresh_rate_button_click(144))
    refresh_rate_144_button.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    create_window()

import pystray
from pystray import MenuItem as item
from PIL import Image
import subprocess


def open_main_app(icon):
    subprocess.Popen(["python", "main.py"])

def open_settings_app(icon):
    subprocess.Popen(["pythonw", "settings.py"])

def open_reset_app(icon):
    subprocess.Popen(["pythonw", "reset.py"])

def exit_app(icon):
    icon.stop()

def main():
    image = Image.open("icons.png")
    menu = (item('Résolutions', open_main_app),
            item('Settings', open_settings_app),
            item('Reset Settings', open_reset_app),
            item('Exit', exit_app))
    icon = pystray.Icon("name", image, "ResManager", menu)
    icon.run()

if __name__ == "__main__":
    main()

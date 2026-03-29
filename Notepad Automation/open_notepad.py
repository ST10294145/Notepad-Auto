import pyautogui
import time
import os

# Step 0: Where to save the file
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "MyTestFile.txt"
full_path = os.path.join(desktop_path, file_name)


# Step 1: Open Notepad
os.system("notepad.exe")  # opens Notepad
time.sleep(1)  # wait 1 second for Notepad to open

# Step 2: Type your message
text_to_write = "Hello! This text was typed automatically by Python. 😎"
pyautogui.write(text_to_write, interval=0.05)  # types text slowly

# Step 3: Save the file
pyautogui.hotkey('ctrl', 's')  # opens Save dialog
time.sleep(0.5)
pyautogui.write(full_path)  # types the full path + filename
time.sleep(0.5)
pyautogui.press('enter')  # presses Enter to save

#test
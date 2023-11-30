import time
import pyautogui

# Function to simulate pressing a key combination
def press_key_combination(keys):
    pyautogui.hotkey(*keys)
    time.sleep(1)

# Function to simulate pressing a single key
def press_single_key(key):
    pyautogui.press(key)
    time.sleep(1)

# Example usage
# Mute
press_key_combination(['fn', 'f1'])

# Full Volume
press_key_combination(['fn', 'f2'])

# Volume Down
press_key_combination(['fn', 'f3'])

# Volume Up
press_key_combination(['fn', 'f4'])

# Play/Pause
press_key_combination(['fn', 'f5'])

# Keyboard Slide (Assuming there's a dedicated key for this)
# Replace 'SlideKey' with the actual key for keyboard slide
press_single_key('SlideKey')

# Brightness Down
press_key_combination(['fn', 'f6'])

# Brightness Up
press_key_combination(['fn', 'f7'])

# Screenshot
press_key_combination(['winleft', 'shift', 's'])  # Windows 11 shortcut for snipping tool

# Home Button
press_key_combination(['fn', 'left arrow'])

# Delete
press_single_key('delete')

# Insert
press_single_key('insert')

# Select All
press_key_combination(['ctrl', 'a'])

# Save
press_key_combination(['ctrl', 's'])

# Save As
press_key_combination(['ctrl', 'shift', 's'])

# New Folder
press_key_combination(['ctrl', 'shift', 'n'])

# Open File
press_key_combination(['ctrl', 'o'])

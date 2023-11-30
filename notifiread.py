from plyer import notification
import win32gui
import pyautogui
import time

def get_active_window_title():
    try:
        active_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        return active_window if active_window else None
    except Exception as e:
        print(f"Error getting active window title: {e}")
        return None

def read_whatsapp_messages():
    try:
        while True:
            current_title = get_active_window_title()

            if "WhatsApp" in current_title:
                screenshot = pyautogui.screenshot()
                # Perform image recognition or text extraction on the screenshot here
                # You may want to use additional libraries for more advanced processing

                # Example: Print a placeholder message for demonstration
                print("New WhatsApp message detected!")

            time.sleep(5)  # Adjust the interval as needed
    except KeyboardInterrupt:
        print("Notification reader stopped.")

# Example usage
read_whatsapp_messages()

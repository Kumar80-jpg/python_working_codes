import pyautogui
import time
import webbrowser

# Step 1: Open Google
webbrowser.open("https://www.google.com")

time.sleep(5)  # wait for browser to open

# Step 2: Click search bar (adjust coordinates if needed)
pyautogui.click(298, 506)

time.sleep(1)

# Step 3: Type search query
pyautogui.write("England vs India score", interval=0.05)

# Step 4: Press Enter
pyautogui.press("enter")

time.sleep(5)  # wait for results

# Step 5: Click first result (adjust coordinates)
pyautogui.click(500, 650)
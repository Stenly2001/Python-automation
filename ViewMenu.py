import pyautogui
import time

print("SalesMate + Backup Menu Test")

# Open the Start menu using the Windows key
print("Opening the Start menu...")
pyautogui.press("win")
time.sleep(1)

# Type the application name
print("Selecting SalesMate + Application")
pyautogui.write("SalesMate +")

# Press Enter to launch the application
print("Press Enter to Launch SalesMate + Application and Wait for 10 Sec")
pyautogui.press("enter")
time.sleep(10)  # Wait for the application to load

# Get actual coordinates
time.sleep(5)
print(pyautogui.position())
pyautogui.click(x=1220, y=830)

# Close "Tip of the Day" dialog
print("Closing 'Tip of the Day' dialog")
pyautogui.press("enter")

print("Running View Menu Test Cases...")

# Define toolbar menu navigation positions
toolbar_options = [
    ("Main Toolbar", 0),
    ("Right Toolbar", 1),
    ("Left Toolbar", 2),
    ("SMP Point Of Sale Addin", 3)
]

# Loop through the options twice 
for _ in range(2):  # Toggle ON and then OFF
    for name, steps_down in toolbar_options:
        print(f"Toggling {name}")
        
        # Open View menu
        pyautogui.press(['alt', 'v'])
        time.sleep(1)
        
        # Select "Toolbar" and navigate down to the correct option
        pyautogui.press("t")  
        time.sleep(1)
        
        if steps_down > 0:
            pyautogui.press("down", presses=steps_down, interval=0.3)
            time.sleep(1)
        
        pyautogui.press("enter")  # Toggle the option
        time.sleep(1)  # Wait before moving to the next option


pyautogui.press(['alt', 'v'])     
pyautogui.press("down") 
pyautogui.press("enter") 
time.sleep(1)   
pyautogui.press(['alt', 'v'])     
pyautogui.press("down", presses=2, interval=0.5) 
pyautogui.press("enter")  
time.sleep(1) 
pyautogui.press(['alt', 'v'])     
pyautogui.press("down", presses=2, interval=0.5) 
pyautogui.press("enter")
time.sleep(1)









 
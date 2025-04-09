import pyautogui
import time

print("Running Customer Menu Test Cases...")

# Sample data
customers = [
    {"id": "100", "first_name": "Sachin"},
    {"id": "101", "first_name": "Bobby"},
    {"id": "102", "first_name": "Salt"}
]

# Coordinates of the actual positions
customer_id_coords = (1001, 279)
first_name_coords = (971, 313)
save_button_coords = (1060, 849)
add_customer_button_coords = (1074, 574)

# Loop through each customer
for customer in customers:
    # Open Add Customer 
    pyautogui.press(['alt', 'c'])
    time.sleep(1)
    pyautogui.press("a")
    time.sleep(1)

    # Fill Customer ID
    pyautogui.click(customer_id_coords)
    pyautogui.press('backspace')
    pyautogui.write(customer["id"])
    time.sleep(1)

    # Fill First Name
    pyautogui.click(first_name_coords)
    pyautogui.press('backspace')
    pyautogui.write(customer["first_name"])
    time.sleep(1)

    # Click Save
    pyautogui.click(save_button_coords)
    time.sleep(1)

    # Confirm save and return 
    pyautogui.click(add_customer_button_coords)
    time.sleep(1)

# Edit customer
pyautogui.press(['alt', 'c'])
time.sleep(1)
pyautogui.press("e")
time.sleep(1)

# Get actual coordinates
time.sleep(5)
print(pyautogui.position())
pyautogui.click(x=769, y=284)
pyautogui.write("102")


# Get actual coordinates for edit button
time.sleep(5)
print(pyautogui.position())
pyautogui.click(x=1168, y=793)


# Click the dropdown
category_dropdown_coords = (1014, 561)  
pyautogui.click(category_dropdown_coords)
time.sleep(1)

# Navigate to "Regular"
for _ in range(3):
    pyautogui.press('up')
    time.sleep(0.2)
pyautogui.press('enter')    


# Get actual coordinates for update button
time.sleep(5)
print(pyautogui.position())
pyautogui.click(x=1066, y=845) 

# Get actual coordinates for pop up button
time.sleep(5)
print(pyautogui.position())
pyautogui.click(x=1066, y=565) 

# Get actual coordinates for cancel button
time.sleep(5)
print(pyautogui.position())
pyautogui.click(x=1283, y=797) 
   
# Delete customer   
pyautogui.press(['alt', 'c'])
time.sleep(1)
pyautogui.press("d")
time.sleep(1)


# Get actual coordinates
time.sleep(5)
print(pyautogui.position())
pyautogui.click(x=769, y=284)
pyautogui.write("101")

# Get actual coordinates for delete button
time.sleep(5)
print(pyautogui.position())
pyautogui.click(x=1168, y=793)

# Get actual coordinates for delete button
time.sleep(5)
print(pyautogui.position())
pyautogui.click(x=1066, y=845) 

# Get actual coordinates for pop up button
time.sleep(5)
print(pyautogui.position())
pyautogui.click(x=1066, y=565) 
# Get actual coordinates for cancel button
time.sleep(5)
print(pyautogui.position())
pyautogui.click(x=1066, y=565) 

# Get actual coordinates for cancel button
time.sleep(5)
print(pyautogui.position())
pyautogui.click(x=1283, y=797) 

# Find the customer
pyautogui.press(['alt', 'c'])
time.sleep(1)
pyautogui.press("f")
time.sleep(1)


# Get actual coordinates
time.sleep(5)
print(pyautogui.position())
pyautogui.click(x=769, y=284)
pyautogui.write("102")

# Get actual coordinates for find button
time.sleep(5)
print(pyautogui.position())
pyautogui.click(x=1168, y=793) 




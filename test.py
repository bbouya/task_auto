import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def submit_form():
    email = email_entry.get()
    password = password_entry.get()
    url = url_entry.get()
    
    # Perform some action with the submitted data
    # Here, we simply print the data to the console
    print("Email:", email)
    print("Password:", password)
    print("URL:", url)
    
    try:
        # initialize the Chrome driver
        with webdriver.Chrome("chromedriver") as driver:
            # head to the login page
            driver.get(url)
            
            try:
                # find username/email field and send the username itself to the input field
                username_field = driver.find_element("id", "login_field")
                username_field.send_keys(email)
            except NoSuchElementException:
                print("Username/Email field not found. Skipping username entry.")
            
            try:
                # find password input field and insert password as well
                password_field = driver.find_element("id", "password")
                password_field.send_keys(password)
            except NoSuchElementException:
                print("Password field not found. Skipping password entry.")
            
            try:
                # click login button
                login_button = driver.find_element("name", "commit")
                login_button.click()
            except NoSuchElementException:
                print("Login button not found. Skipping login.")
            
            # wait for the ready state to be complete
            #WebDriverWait(driver=driver, timeout=10).until(
            #    lambda x: x.execute_script("return document.readyState === 'complete'")
            #)
            # wait for the ready state to be complete
            WebDriverWait(driver=driver, timeout=10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )
            
    except TimeoutException:
        print("Timeout occurred while waiting for the page to load.")
    except Exception as e:
        print("An error occurred:", str(e))

root = tk.Tk()
root.title("Python Application Form")

# Create a style object
style = ttk.Style(root)
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

# Form Frame
form_frame = ttk.Frame(root, padding=20)
form_frame.pack()

# Email label and entry
email_label = ttk.Label(form_frame, text="Email:")
email_label.grid(row=0, column=0, sticky=tk.W)
email_entry = ttk.Entry(form_frame)
email_entry.grid(row=0, column=1)

# Password label and entry
password_label = ttk.Label(form_frame, text="Password:")
password_label.grid(row=1, column=0, sticky=tk.W)
password_entry = ttk.Entry(form_frame, show="*")
password_entry.grid(row=1, column=1)

# URL label and entry
url_label = ttk.Label(form_frame, text="URL:")
url_label.grid(row=2, column=0, sticky=tk.W)
url_entry = ttk.Entry(form_frame)
url_entry.grid(row=2, column=1)

# Submit button
submit_button = ttk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=10)

root.mainloop()

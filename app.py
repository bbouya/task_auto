import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def submit_form():
    email = email_entry.get()
    password = password_entry.get()
    url = url_entry.get()
    
    # print the eamil ...
    print("Email:", email)
    print("Password:", password)
    print("URL:", url)
    

    # init chrome driver
    driver = webdriver.Chrome("chromedriver")
    
    
    
    # open the url
    driver.get(url)
    # find username
    driver.find_element("id", "login_field").send_keys(email)
    # find password
    driver.find_element("id", "password").send_keys(password)
    # click login button
    driver.find_element("name", "commit").click()
    
    
    # wait the ready state to be complete
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )

    # Keep the browser window open until the user closes it
    input("Press Enter to close the browser...")
    
    # Close the browser window
    driver.quit()

root = tk.Tk()
# add title of app
root.title("Python Application Form")

# Create a style object
style = ttk.Style(root)
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

# Form Frame
form_frame = ttk.Frame(root, padding=20)
form_frame.pack()

# Email label entry
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

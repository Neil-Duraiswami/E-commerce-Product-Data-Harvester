# Import necessary modules
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import tkinter as tk
from tkinter import simpledialog, messagebox

# Define the function to fetch top products from Amazon and eBay
def fetch_top_products(product_name, num_items):
    # Initialize the WebDriver (assuming you're using Chrome)
    driver = webdriver.Chrome()
    
    # Initialize empty lists to store products
    amazon_products = []
    ebay_products = []
    
    try:
        # Navigate to Amazon's homepage
        driver.get("https://www.amazon.com")
        
        # Find the search bar and input the specific product name
        search_bar = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        search_bar.clear()
        search_bar.send_keys(product_name)
        
        # Submit the search
        search_bar.submit()
        
        # Wait for search results to load
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")))
        
        # Extract the names and prices of the top products from Amazon
        product_names = driver.find_elements(By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")
        price_elements = driver.find_elements(By.CSS_SELECTOR, "span.a-price")
        
        for i in range(min(num_items, len(product_names))):
            name = product_names[i].text.strip()
            price = price_elements[i].text.strip()
            amazon_products.append((name, price, "Amazon"))
        
        # Navigate to eBay's homepage
        driver.get("https://www.ebay.com")
        
        # Find the search bar and input the specific product name
        search_bar = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "gh-ac")))
        search_bar.clear()
        search_bar.send_keys(product_name)
        
        # Submit the search
        search_bar.submit()
        
        # Wait for search results to load
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-item__info")))
        
        # Extract the names and prices of the top products from eBay
        product_names = driver.find_elements(By.CSS_SELECTOR, "div.s-item__title > span")
        product_prices = driver.find_elements(By.CSS_SELECTOR, "div.s-item__detail > span.s-item__price")
        for i in range(min(num_items, len(product_names))):
            name = product_names[i].text.strip()
            price = product_prices[i].text.strip()
            if name:
                ebay_products.append((name, price, "eBay"))
        
        # Combine products from both websites
        all_products = amazon_products + ebay_products
        
        # Write the products to a CSV file (excluding the header row)
        with open('product_comparison.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Product Name", "Price", "Website"])
            writer.writerows(all_products)
        
        # Open the CSV file after it's been generated
        os.system('start product_comparison.csv')
    
    finally:
        # Close the browser
        driver.quit()
        # Show a message box indicating that the CSV file has been generated
        messagebox.showinfo("CSV File Generated", "The CSV file has been generated successfully!")

# Create a tkinter dialog box to get the product name and number of items
root = tk.Tk()
root.withdraw()  # Hide the root window

# Prompt the user to input the product name and number of items to search for
product_name = simpledialog.askstring("Product Name", "Enter the product name to search:")
num_items = simpledialog.askinteger("Number of Items", "Enter the number of items to search for on each site:")

# Call the function with the specified product name and number of items
fetch_top_products(product_name, num_items)

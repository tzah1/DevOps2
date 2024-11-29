from selenium import webdriver

# Example using Chrome; specify path if not added to PATH
driver = webdriver.Chrome()  # Or webdriver.Chrome('path/to/chromedriver')

# Open a webpage
driver.get("https://www.example.com")

# Print the page title
print("Page title:", driver.title)

# Close the browser
driver.quit()

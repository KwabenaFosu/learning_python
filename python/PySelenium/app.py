from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://twitter.com")
sign_in = browser.find_element_by_link_text("Sign in")

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager





def driver():
    driver = webdriver.Chrome(CromeDriverManager().install())
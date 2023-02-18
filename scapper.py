# %%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

#%%
## set webdriver using chromedriver
service = Service(executable_path="./chromedriver")

## setup chrome options
options = ChromeOptions()
options.add_argument("--headless=new") ### comment to show chrome 


## setup webdriver
driver = webdriver.Chrome(service=service,options=options)
wait = WebDriverWait(driver, timeout=5)
# %%
url = 'https://finance.yahoo.com/topic/stock-market-news/'
driver.get(url)

new_stream = wait.until(lambda d: d.find_element(By.ID,"Fin-Stream"))
news = new_stream.find_elements(By.CSS_SELECTOR, '.js-stream-content')
count = len(news)
print(f"Found {count} news")
print()

page_html = driver.page_source
driver.quit()


# %%
soup = BeautifulSoup(page_html,'lxml')
newsLinks = soup.select('#Fin-Stream .js-content-viewer')
for link in newsLinks:
    print(link.attrs['href'])
    print(link.text)
    print()


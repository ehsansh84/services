from selenium import webdriver
from selenium.webdriver.common.keys import Keys

source_link = 'http://www.ncbi.nlm.nih.gov/pubmed/?term=cancer'


driver = webdriver.Firefox()
a = driver.get(source_link)
print(a)
assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
#this is for testing purposes
# to be used only by Oscar for testing
# <3 Oscar

from backend import webscraper

driver = webscraper.ScrapeEngine()

driver.driver.get('https://eli.thegreenplace.net/2009/06/12/safely-using-destructors-in-python/')

print(driver.driver.title)

del driver

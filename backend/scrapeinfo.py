from bs4 import BeautifulSoup
import urllib.request as ul


'''def init_scrape_info(scrapename: str, url: str, *args):
    fout = open('scraping_configs/' + scrapename + '.txt', 'w')
    fout.write(url + '\n')
    page = ul.urlopen(url)
    soup = BeautifulSoup(page, features='html.parser')
    for i in args:
        found = soup.find_all("div", text=i)
        fout.write(' '.join(found[0]['class']))
        fout.write('\n')
    fout.close()


def scrape_info(scrape_config_file: str):
    fin = open('scraping_configs/' + scrape_config_file + '.txt', 'r')
    lines = fin.read().split('\n')
    url = lines[0]
    page = ul.urlopen(url)
    soup = BeautifulSoup(page, features='html.parser')
    for line in lines[1:]:
        text = soup.find(class_=line).text
        print(text)
    fin.close()'''

import codecs
import time
import pandas as pd

from bs4 import BeautifulSoup, BeautifulStoneSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# headers = {'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Mobile Safari/537.36 Edg/95.0.1020.40'}

def parse_html(html_code):
    parsed_html = BeautifulSoup(html_code, 'html.parser')
    return parsed_html

def find_elements_in_parsed_html(parsed_html, tag_name, class_name):
    result = parsed_html.find_all(tag_name, class_name)
    return result

def store_data_in_list(dataset):
    items = []
    for item in dataset:
        items.append(item['data-val'])
    return items

def list_top_music_from_letras_mus(artist):
    pass

def get_html_from_browser(url):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    time.sleep(8)
    html = driver.find_element_by_xpath("//div[@class='spikewrap']").get_attribute('outerHTML')
    driver.quit()
    return html

def write_file(filename, content):
    path = fix_file_name(filename)
    file = codecs.open(path, "w", "utf-8")
    file.write("Artistas em destaque do Last.fm nessa semana: \n\n")
    for item in content:
        file.write(item+"\n")
    file.close()

def fix_file_name(filename):
    if (filename.endswith(".txt")):
        return filename
    return filename + ".txt"

def main():
    url = "https://www.last.fm/pt/"
    html_without_parsing = get_html_from_browser(url)
    parsed_html = parse_html(html_without_parsing)
    elements = find_elements_in_parsed_html(parsed_html, "div", "bubble")
    artists = store_data_in_list(elements)
    write_file("resultado", artists)

if __name__ == "__main__":
    main()

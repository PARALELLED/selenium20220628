import requests
from bs4 import BeautifulSoup


url2 = "https://reurl.cc/448na3"

def find_a_tag():
    result_list = []
    url1 ='https://tw.news.yahoo.com/'
    html = requests.get(url1)
    html.encoding = 'UTF-8'
    sp = BeautifulSoup(html.text, 'lxml')

    results = sp.find_all("a")
    for result in results[1:]:
        result_list.append(result.text)
    print("\n".join(result_list))
    return "\n".join(result_list)

    

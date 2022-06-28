import requests
from bs4 import BeautifulSoup as bs
import re


def IT_helper():
    pattern = "[[Day].*"
    title_list = []

    for page in range(1,4):
        url = "https://ithelp.ithome.com.tw/users/20121176/ironman/3023?page="+str(page)
        res = requests.get(url)
        soup = bs(res.text,"html.parser")
        titles = soup.find_all("h3")

        for title in titles[1:]:
            title_list.append(title.text.replace(' ','').replace("\n",''))
    print("\n".join(title_list))
    return "\n".join(title_list)

"""
https://ithelp.ithome.com.tw/articles/10214448
首先\n是特殊字元，代表換行的意思，
因此用\n換行字元把列表裡的字串接起來，
自然就可以換行印囉。
"""

# tldextract
import tldextract

def find_tld(url):
    result = tldextract.extract(url)
    return str(result)
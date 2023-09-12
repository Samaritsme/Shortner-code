import requests
import pyshorteners
from cloudscraper import create_scraper
from urllib.parse import quote
from urllib3 import disable_warnings
  
def shortx_url(longurl, shortener, api):
    cget = create_scraper().request
    disable_warnings()
    if "shorte.st" in shortener:
        disable_warnings()
        return requests.get(f'http://api.shorte.st/stxt/{api}/{longurl}', verify=False).text
    elif "linkvertise" in shortener:
        url = quote(base64.b64encode(longurl.encode("utf-8")))
        linkvertise = [
            f"https://link-to.net/{api}/{random.random() * 1000}/dynamic?r={url}",
            f"https://up-to-down.net/{api}/{random.random() * 1000}/dynamic?r={url}",
            f"https://direct-link.net/{api}/{random.random() * 1000}/dynamic?r={url}",
            f"https://file-link.net/{api}/{random.random() * 1000}/dynamic?r={url}"]
        return random.choice(linkvertise)
    elif "bitly.com" in shortener:
        s = pyshorteners.Shortener(api_key=api)
        return s.bitly.short(longurl)
    elif "ouo.io" in shortener:
        disable_warnings()
        return requests.get(f'http://ouo.io/api/{api}?s={longurl}', verify=False).text
    elif "tnshort.net" in shortener:
        params = {'api': api, 'url': longurl}
        duli= f'https://tnshort.net/api'
        get_url = requests.get(duli,params)
        get_url = get_url.json()['shortenedUrl']
        return get_url
    else:
        return requests.get(f'https://{shortener}/api?api={api}&url={longurl}&format=text').text

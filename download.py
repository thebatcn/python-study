import urllib.request
from urllib.error import URLError,HTTPError,ContentTooShortError

def download(url,user_agent ='wswp',num_retries=2):
    print("Downloading {}".format(url))
    request = urllib.request.Request(url)
    request.add_header("User-agent",user_agent)

    try:
       html =  urllib.request.urlopen(url).read()
    except (URLError,HTTPError,ConnectionAbortedError)as e:
        print("Download error: ",e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e,'code') and 500<=e.code<=600:
            #recursively retry 5xx HTTP errors
                download(url,'wswp',num_retries-1) 
    return html

    
url = 'https://www.baidu.com'

print(download(url))


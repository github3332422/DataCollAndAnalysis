import requests

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

html = requests.get('https://www.zhipin.com/c101010100-p100599/?page=2&ka=page-2').text
print(html)
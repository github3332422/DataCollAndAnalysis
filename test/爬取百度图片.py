#coding=utf-8
import urllib.request
import re
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    html = html.decode('utf-8')
    # reg = r'src="(.+?\.jpg)" pic_ext'
    reg = r'<div class="threadlist_video"><img src="(.*?)"/>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '../picture/%s.jpg' % x)
        x += 1
        print('Getting the %s picture' % x)
    reg = r'<a rel="noreferrer"  class="thumbnail vpic_wrap"><img .*? data-original="(.*?)"'
    # reg = r'data-original="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    # print(imglist)
    # for im in imglist:
    #     print(im)
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'../picture/%s.jpg' % x)
        x+=1
        print('Getting the %s picture' % x)
html = getHtml("https://tieba.baidu.com/p/2460150866?pn=3")
# print(html)
getImg(html)

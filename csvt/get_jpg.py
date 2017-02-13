import re
import urllib

def get_html(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getimg(html):
    reg = r'src="(.*?\.jpg)" size'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 1
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1
html_page = get_html("http://tieba.baidu.com/p/4590324632")
getimg(html_page)


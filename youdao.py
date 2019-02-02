import requests
import re

def init():
    url = "https://www.youdao.com/w/"
    word = input("输入: ")
    r = requests.get(url+word)
    page = r.text
    return page
def loc_dic(page):
    if "<div id=\"phrsListTab\" class=\"trans-wrapper clearfix\">" in page: #有词典结果
        container = re.search("<div class=\"trans-container\">.*?<ul>(.*?)</ul>.*?</div>",page,re.S).group(1)
        if 'wordGroup' in container:
            word_groups = re.findall("<p.class=\"wordGroup\">.*?</p>",container,re.S)
            res =  ["".join(re.sub("<.*?>","",word_group).split()) for word_group in word_groups]
            return res
        else:
            res = ["".join(re.sub("<.*?>","",container).split())]
            return res
    else:
        return ["没有结果"]
# if __name__ == "__main__":
page = init()
result = loc_dic(page)
print(result)

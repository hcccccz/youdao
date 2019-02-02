import requests
import re
import os

def init(word):
    url = "https://www.youdao.com/w/"
    r = requests.get(url+word)
    page = r.text
    return page
def loc_dic(page):
    if "<div id=\"phrsListTab\" class=\"trans-wrapper clearfix\">" in page: #有词典结果
        container = re.search("<div class=\"trans-container\">.*?<ul>(.*?)</ul>.*?</div>",page,re.S).group(1)
        if 'wordGroup' in container: #中文
            word_groups = re.findall("<p.class=\"wordGroup\">.*?</p>",container,re.S)
            res = []
            for word_group in word_groups:
                word = re.sub("<.*?>","",word_group)
                tar = re.search(r"\w\s\w",word)
                if tar:
                    tar = tar.group()
                    tar = tar.replace(" ","+")
                    word = re.sub(r"\w\s\w",tar,word)
                    word = "".join(word.split())
                    word = word.replace("+"," ")
                else:
                    word = re.sub("<.*?>","",word_group)
                    word = "".join(word.split())


                res.append(word)
            return res
        else: #英文
            word_groups = re.findall("<li>.*?</li>",container,re.S)
            res = ["".join(re.sub("<.*?>","",word_group).split()) for word_group in word_groups]
            return res
    else:
        return ["没有结果"]
def output(res):
    for r in res:
        print(r)
if __name__ == "__main__":
    word = input("输入(!Q退出): ")
    print("_"*8)
    while word != "!Q":
        if word == "!Q":
            pass
        elif word == "clear":
            os.system("clear")
        else:
            page = init(word)
            res = loc_dic(page)
            output(res)
        print("_"*8)
        word = input("输入(!Q退出): ")
        print("_"*8)

import requests
import re
import os

def init(word): #获取页面
    url = "https://www.youdao.com/w/"
    r = requests.get(url+word)
    page = r.text
    return page

def plain_exp(page): #获取直接释义直接释义
    res = ""
    if "<div id=\"phrsListTab\" class=\"trans-wrapper clearfix\">" in page: #有词典结果
        container = re.search("<div class=\"trans-container\">.*?<ul>(.*?)</ul>.*?</div>",page,re.S).group(1)
        if 'wordGroup' in container: #中文
            word_groups = re.findall("<p.class=\"wordGroup\">.*?</p>",container,re.S)
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
                res += word+"\n"
        else: #英文
            word_groups = re.findall("<li>.*?</li>",container,re.S)
            for word_group in word_groups:
                rep = re.sub("<.*?>","",word_group)
                rep_l = rep.split()
                rep_s = "".join(rep_l)
                res += rep_s+"\n"

        return res
    else:
        return ("没有结果")

#------------------------------分割-------------------------------------------------------------------




if __name__ == "__main__":
    r = init("结果")
    word = plain_exp(r)
    print(word)

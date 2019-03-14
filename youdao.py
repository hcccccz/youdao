import requests
import re
import os
import bs4

def init(word): #获取页面
    url = "https://www.youdao.com/w/"
    r = requests.get(url+word)
    page = r.text
    return page

def plain_exp(page): #获取直接释义直接释义
    res = "【有道释义】\n\n"
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

        print(res)


#------------------------------分割-------------------------------------------------------------------
def one(page):
    exp = "【网络释义】\n\n"
    bs = bs4.BeautifulSoup(page,"html.parser")
    webtrans = bs.find('div',{"id":"webTransToggle"})
    if webtrans:
        title = webtrans.find_all("div",{"class":"title"})
        for t in title[:-1]:
            t = t.get_text().strip()
            if t.startswith("["):
                t = " ".join(t.split())
            exp += t
            exp += "\n"
        exp += "\n\n【网络短语】\n\n"
        webphrase = webtrans.find_all('p',{"class":"wordGroup"})
        for phrase in webphrase:
            text = phrase.get_text()
            text = re.sub("\n"," ",text)
            text = " ".join(text.split())
            exp += text+"\n"

    print(exp)

#-----------------------------分割--------------------------------------------------------------------
def two(page):
    exp = "【专业释义】\n\n"
    bs = bs4.BeautifulSoup(page,"html.parser")
    tpetrans = bs.find('div',{"id":"tPETrans"})
    if tpetrans:
        ptypes = tpetrans.find_all('a',class_=re.compile("p-type"))
        for i in range(len(ptypes)):
            inx = "ptype_" + str(i) + " types"
            lis = tpetrans.find("li",class_=re.compile(inx))
            explains_raw = lis.find_all("span",class_="title")
            explains_raw = [explain_raw.get_text() for explain_raw in explains_raw]
            explain = ptypes[i].get_text() + ": " + ",".join(explains_raw)
            exp += explain + "\n"
        return(exp)
# ---------------------------------分割----------------------------------------------------------------
def three(page):
    exp = "【柯林斯英汉双解大词典】\n\n"
    bs = bs4.BeautifulSoup(page,"html.parser")
    coltrans = bs.find('div',id="collinsResult")
    if coltrans:
        print(coltrans.find_all("span",class_="title"))



if __name__ == "__main__":
    word = input("单词..: ")
    print(type(word))
    r = init(word)
    # plain_exp(r)
    three(r)

import bs4

html = '''<div class = "asd">
  <h1>Soup</h1>
  <p>Beautiful</p>
  <div>
    <a href = "www.baidu.com">baidu</a>
  </div>
</div>'''
soup = bs4.BeautifulSoup(html,"html.parser")
print(soup.a.name)

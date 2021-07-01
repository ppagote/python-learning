import requests
import bs4

response = requests.get("http://quotes.toscrape.com/")

text = bs4.BeautifulSoup(response.text, "lxml")

authorList = set()
for author in text.select(".author"):
    authorList.add(author.getText())

print(authorList)

quoteList = []
for quoteText in text.select('.text'):
    quoteList.append(quoteText.getText())

print(quoteList)

for topTags in text.select('.tag-item'):
    print(topTags.getText())

uniqueAuthors = set()
for i in range(1, 11):
    url = "http://quotes.toscrape.com/page/{}"
    print(url.format(i))
    responseAll = requests.get(url.format(i))
    soup = bs4.BeautifulSoup(responseAll.text, "lxml")

    for author in soup.select(".author"):
        uniqueAuthors.add(author.getText())
print(uniqueAuthors)

page = 1
page_exists = False
while page_exists:
    url = "http://quotes.toscrape.com/page/{}"
    print(url.format(page))
    responseAll = requests.get(url.format(page))

    if "No quotes found!" in responseAll:
        page_exists = False
    else:
        soup = bs4.BeautifulSoup(responseAll.text, "lxml")

        for author in soup.select(".author"):
            uniqueAuthors.add(author.getText())
        page = page + 1

print(uniqueAuthors)
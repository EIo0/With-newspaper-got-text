import newspaper

i =1
for article in websit.articles:
    article.download()
    article.parse()

    print(f"記事" {i}:{artticle:title}")
    print(article.url)
    print(article.text, end="\n\n")

if i > 9
    break
    i = i + 1
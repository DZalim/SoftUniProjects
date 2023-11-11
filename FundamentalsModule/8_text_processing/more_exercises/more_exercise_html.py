title_of_an_article = input()
content_of_that_article = input()

print(f"<h1>\n  {title_of_an_article}\n</h1>")
print(f"<article>\n  {content_of_that_article}\n</article>")

comments_about_the_article = input()
while comments_about_the_article != "end of comments":
    print(f"<div>\n  {comments_about_the_article}\n</div>")
    comments_about_the_article = input()

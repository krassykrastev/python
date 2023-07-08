# You will receive lines of input:
# • On the first line, you will receive a title of an article
# • On the second line, you will receive the content of that article
# • On the following lines, until you receive "end of comments" you will get the comments about the article
# Print the whole information in html format:
# • The title should be in "h1" tag (<h1></h1>)
# • The content in article tag (<article></article>)
# • Each comment should be in div tag (<div></div>)
# For more clarification see the example below.
#
# Input1:
# SoftUni Article
# Some content of the SoftUni article
# some comment
# more comment
# last comment
# end of comments
#
# Output1:
# <h1>
# SoftUni Article
# </h1>
# <article>
# Some content of the SoftUni article
# </article>
# <div>
# some comment
# </div>
# <div>
# more comment
# </div>
# <div>
# last comment
# </div>

article_title = input()
article_context = input()

print("<h1>")
print(f"    {article_title}")
print("</h1>")

print("<article>")
print(f"    {article_context}")
print("</article>")

while True:
    article_comments = input()

    if article_comments == "end of comments":
        break

    print("<div>")
    print(f"    {article_comments}")
    print("</div>")